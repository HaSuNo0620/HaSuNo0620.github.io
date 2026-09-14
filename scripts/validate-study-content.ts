import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';
import {
  parseHandbookFile,
  parseKnowledgeFile,
  parseManifest,
  parseStoryFile,
} from '../src/study/domain/content-schema';
import type { QualificationPack } from '../src/study/domain/content-types';
import { validatePack } from '../src/study/domain/validate-pack';

const root = new URL('../src/study-content/', import.meta.url).pathname;

function yamlFiles(dir: string): string[] {
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name);
    return statSync(path).isDirectory() ? yamlFiles(path) : path.endsWith('.yaml') ? [path] : [];
  });
}

function loadDirectory(dir: string): QualificationPack {
  const files = yamlFiles(dir);
  const manifest = parseManifest(readFileSync(join(dir, 'manifest.yaml'), 'utf8'));
  return {
    manifest,
    knowledge: files.filter((p) => p.includes('/knowledge/')).flatMap((p) => parseKnowledgeFile(readFileSync(p, 'utf8'))),
    handbook: files.filter((p) => p.includes('/handbook/')).flatMap((p) => parseHandbookFile(readFileSync(p, 'utf8'))),
    stories: files.filter((p) => p.includes('/stories/')).map((p) => parseStoryFile(readFileSync(p, 'utf8'))),
  };
}

const qualificationDirs = readdirSync(root)
  .map((name) => join(root, name))
  .filter((path) => statSync(path).isDirectory());

let errorCount = 0;
for (const dir of qualificationDirs) {
  try {
    const pack = loadDirectory(dir);
    const report = validatePack(pack);
    for (const warning of report.warnings) console.warn(`WARN ${warning.code}: ${warning.message}`);
    for (const error of report.errors) console.error(`ERROR ${error.code}: ${error.message}`);
    console.log(`${relative(root, dir)}: ${report.coverage.length} knowledge nodes, ${report.errors.length} errors, ${report.warnings.length} warnings`);
    errorCount += report.errors.length;
  } catch (error) {
    errorCount += 1;
    console.error(`ERROR PARSE: ${relative(root, dir)}:`, error);
  }
}

if (errorCount > 0) process.exit(1);
