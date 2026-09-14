import type { QualificationPack } from '../domain/content-types';
import {
  parseHandbookFile,
  parseKnowledgeFile,
  parseManifest,
  parseStoryFile,
} from '../domain/content-schema';

const files = import.meta.glob('/src/study-content/**/*.yaml', {
  eager: true,
  query: '?raw',
  import: 'default',
}) as Record<string, string>;

function qualificationIdFromPath(path: string): string | null {
  const match = path.match(/^\/src\/study-content\/([^/]+)\//);
  return match?.[1] ?? null;
}

export function loadContentPacks(): QualificationPack[] {
  const qualificationIds = new Set<string>();
  for (const path of Object.keys(files)) {
    const id = qualificationIdFromPath(path);
    if (id) qualificationIds.add(id);
  }

  return [...qualificationIds].sort().map((qualificationId) => {
    const root = `/src/study-content/${qualificationId}/`;
    const manifestRaw = files[`${root}manifest.yaml`];
    if (!manifestRaw) throw new Error(`Missing manifest for ${qualificationId}`);

    const knowledge = Object.entries(files)
      .filter(([path]) => path.startsWith(`${root}knowledge/`))
      .flatMap(([, raw]) => parseKnowledgeFile(raw));
    const handbook = Object.entries(files)
      .filter(([path]) => path.startsWith(`${root}handbook/`))
      .flatMap(([, raw]) => parseHandbookFile(raw));
    const stories = Object.entries(files)
      .filter(([path]) => path.startsWith(`${root}stories/`))
      .map(([, raw]) => parseStoryFile(raw));

    return {
      manifest: parseManifest(manifestRaw),
      knowledge,
      handbook,
      stories,
    };
  });
}
