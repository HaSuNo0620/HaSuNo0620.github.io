# Qualification Study Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable, fully static qualification-study application under `/study/` that teaches through replayable branching cases, beginning with three validated 乙4「性質・火災予防・消火」cases.

**Architecture:** Keep the existing Astro 7 static site and mount a React application under `/study/`. Qualification content is authored as YAML and validated at build time; pure Story and Learning engines operate on validated data; IndexedDB stores append-only learning events and resumable sessions. The UI first chooses a qualification, then presents an unordered case library, story player, handbook, debrief, and learning-state views.

**Tech Stack:** Astro 7.3.x, React, TypeScript, Zod, YAML, idb/IndexedDB, Vitest, Testing Library, jsdom, fake-indexeddb, tsx, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-14-qualification-study-platform-design.md`

## Global Constraints

- Preserve the existing Astro static deployment model and GitHub Pages workflow.
- Runtime requires no server, account, API key, or cross-device synchronization.
- Existing `/notes/`, `/topics/`, `/now/`, and `/about/` behavior must remain unchanged.
- Story content, qualification knowledge, Story Engine, Learning Engine, persistence, and UI remain separate modules.
- Persisted learning events are canonical; mastery values are always derived and recomputable.
- During a case, wrong decisions show consequences rather than `正解` / `不正解`, and no decision causes an early game over.
- Initial cases are playable in any order. Recommendation is advisory only.
- Each initial case has at least two authored variants. Runtime LLM-generated cases are excluded.
- Hazardous-material facts and handbook statements require explicit source provenance and a verification date.
- Structural content errors fail validation/build. Missing story coverage remains a visible warning during MVP.
- No XP, coins, leaderboards, login rewards, social features, account system, sync service, or authoring GUI in MVP.

---

## Planned File Boundaries

```text
astro.config.mjs
package.json
package-lock.json
vitest.config.ts
src/test/setup.ts
src/pages/study/index.astro
src/components/SiteHeader.astro
src/styles/study.css

src/study/domain/content-types.ts
src/study/domain/content-schema.ts
src/study/domain/validate-pack.ts
src/study/domain/story-engine.ts
src/study/domain/learning-engine.ts
src/study/domain/recommendation.ts
src/study/domain/*.test.ts

src/study/content/load-content.ts

src/study/storage/repository.ts
src/study/storage/memory-repository.ts
src/study/storage/repository.test.ts

src/study/ui/StudyApp.tsx
src/study/ui/QualificationPicker.tsx
src/study/ui/CaseLibrary.tsx
src/study/ui/StoryPlayer.tsx
src/study/ui/HandbookDrawer.tsx
src/study/ui/Debrief.tsx
src/study/ui/KnowledgeView.tsx
src/study/ui/StorageWarning.tsx
src/study/ui/study-app.test.tsx

src/study-content/hazardous-materials/manifest.yaml
src/study-content/hazardous-materials/knowledge/class4-common.yaml
src/study-content/hazardous-materials/knowledge/class4-substances.yaml
src/study-content/hazardous-materials/knowledge/fire-prevention.yaml
src/study-content/hazardous-materials/knowledge/extinguishing.yaml
src/study-content/hazardous-materials/handbook/classification.yaml
src/study-content/hazardous-materials/handbook/fire-response.yaml
src/study-content/hazardous-materials/stories/warehouse.yaml
src/study-content/hazardous-materials/stories/solvent-workplace.yaml
src/study-content/hazardous-materials/stories/unknown-liquid.yaml

docs/study-content/otsu4-seisho-coverage.md
scripts/validate-study-content.ts
```

---

### Task 1: React/Astro integration and test foundation

**Files:**
- Modify: `package.json`
- Modify: `package-lock.json`
- Modify: `astro.config.mjs`
- Create: `vitest.config.ts`
- Create: `src/test/setup.ts`
- Create: `src/pages/study/index.astro`
- Create: `src/study/ui/StudyApp.tsx`
- Create: `src/styles/study.css`
- Create: `src/study/ui/study-app.test.tsx`

**Interfaces:**
- Produces `StudyApp(): JSX.Element`.
- Produces `npm test`, `npm run test:watch`, and `npm run validate:study` commands.
- Preserves the current Astro static build.

- [ ] **Step 1: Install dependencies**

```bash
npm install @astrojs/react react react-dom zod yaml idb
npm install -D vitest @testing-library/react @testing-library/jest-dom jsdom fake-indexeddb tsx @types/react @types/react-dom
```

Add scripts without deleting existing scripts:

```json
{
  "test": "vitest run",
  "test:watch": "vitest",
  "validate:study": "tsx scripts/validate-study-content.ts"
}
```

- [ ] **Step 2: Write a failing mount test**

```tsx
import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import StudyApp from './StudyApp';

describe('StudyApp', () => {
  it('renders the study heading', () => {
    render(<StudyApp />);
    expect(screen.getByRole('heading', { name: '資格学習' })).toBeInTheDocument();
  });
});
```

Run:

```bash
npm test -- src/study/ui/study-app.test.tsx
```

Expected: FAIL because React test/app setup is not present.

- [ ] **Step 3: Configure Astro React and Vitest**

Keep existing Astro options and add React integration:

```js
import react from '@astrojs/react';

export default defineConfig({
  integrations: [react()],
  site: 'https://HaSuNo0620.github.io',
  output: 'static',
  trailingSlash: 'always',
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeMathjaxBrowser],
  },
});
```

Create `vitest.config.ts`:

```ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
  },
});
```

Create `src/test/setup.ts`:

```ts
import '@testing-library/jest-dom/vitest';
import 'fake-indexeddb/auto';
```

- [ ] **Step 4: Mount the initial island**

`StudyApp.tsx`:

```tsx
export default function StudyApp() {
  return (
    <main className="study-shell">
      <h1>資格学習</h1>
      <p>ケースから学ぶ資格学習プラットフォーム</p>
    </main>
  );
}
```

`src/pages/study/index.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import StudyApp from '../../study/ui/StudyApp';
import '../../styles/study.css';
---

<BaseLayout title="資格学習">
  <StudyApp client:load />
</BaseLayout>
```

`study.css` initial rule:

```css
.study-shell {
  width: min(72rem, calc(100% - 2rem));
  margin: 0 auto;
  padding: 2rem 0 4rem;
}
```

- [ ] **Step 5: Verify**

```bash
npm test -- src/study/ui/study-app.test.tsx
npm run build
```

Expected: PASS; `dist/study/index.html` exists.

- [ ] **Step 6: Commit**

```bash
git add package.json package-lock.json astro.config.mjs vitest.config.ts src/test/setup.ts src/pages/study/index.astro src/study/ui/StudyApp.tsx src/styles/study.css src/study/ui/study-app.test.tsx
git commit -m "feat: add study app React surface"
```

---

### Task 2: Domain contracts, YAML schemas, and content loader

**Files:**
- Create: `src/study/domain/content-types.ts`
- Create: `src/study/domain/content-schema.ts`
- Create: `src/study/domain/content-schema.test.ts`
- Create: `src/study/content/load-content.ts`

**Interfaces:**
- Produces `parseManifest`, `parseKnowledgeFile`, `parseHandbookFile`, `parseStoryFile`.
- Produces `loadContentPacks(): QualificationPack[]`.
- No UI/storage imports are allowed in this task.

- [ ] **Step 1: Write failing parser tests**

Test a valid decision story and rejection of a choice lacking `next`:

```ts
const story = parseStoryFile(`
id: warehouse
qualificationId: hazardous-materials
section: otsu4-seisho
title: ガソリン臭のする倉庫
summary: 漏洩した危険物への初動を判断する。
durationMinutes: 12
dimensions: [ignition]
variants:
  - id: gasoline-leak
    startScene: arrival
    targetKnowledge: [class4.gasoline.vapor]
    scenes:
      arrival:
        kind: decision
        text: 倉庫内に強い臭気がある。
        choices:
          - id: stop-ignition
            text: 着火源になり得る操作を避ける
            next: resolution
            effects: { ignition: 1 }
            learning:
              - knowledgeId: class4.gasoline.vapor
                mode: apply
                result: 1
      resolution:
        kind: resolution
        text: 状況を整理する。
    endings:
      - id: controlled
        when:
          - dimension: ignition
            operator: gte
            value: 1
        text: 着火を避けて対応できた。
      - id: incident
        default: true
        text: 着火源への対応が不十分だった。
`);
expect(story.variants[0].id).toBe('gasoline-leak');
```

Run and expect failure:

```bash
npm test -- src/study/domain/content-schema.test.ts
```

- [ ] **Step 2: Define stable types**

Create these exact core types:

```ts
export type LearningMode = 'encounter' | 'apply' | 'discriminate' | 'recall';
export type Assistance = 'none' | 'handbook' | 'hint' | 'other';
export type ComparisonOperator = 'gte' | 'lte' | 'eq';

export interface SourceRef {
  id: string;
  label: string;
  url: string;
  checkedAt: string;
}

export interface QualificationManifest {
  id: string;
  title: string;
  sections: { id: string; title: string }[];
  sources: SourceRef[];
}

export interface KnowledgeNode {
  id: string;
  title: string;
  statement: string;
  examConnection: string | null;
  section: string;
  tags: string[];
  relations: {
    type: 'prerequisite' | 'contrasts_with' | 'example_of' | 'derived_from' | 'used_with';
    target: string;
  }[];
  sources: string[];
}

export interface HandbookEntry {
  id: string;
  title: string;
  body: string;
  knowledgeIds: string[];
  sources: string[];
}

export interface LearningSignalDefinition {
  knowledgeId: string;
  mode: LearningMode;
  result: number;
}

export interface StoryChoice {
  id: string;
  text: string;
  next: string;
  effects: Record<string, number>;
  learning: LearningSignalDefinition[];
}

export type StoryScene =
  | { kind: 'narrative'; text: string; next: string }
  | { kind: 'decision'; text: string; choices: StoryChoice[] }
  | { kind: 'resolution'; text: string };

export interface EndingCondition {
  dimension: string;
  operator: ComparisonOperator;
  value: number;
}

export interface StoryEnding {
  id: string;
  text: string;
  when: EndingCondition[];
  default: boolean;
}

export interface StoryVariant {
  id: string;
  startScene: string;
  targetKnowledge: string[];
  scenes: Record<string, StoryScene>;
  endings: StoryEnding[];
}

export interface StoryCase {
  id: string;
  qualificationId: string;
  section: string;
  title: string;
  summary: string;
  durationMinutes: number;
  dimensions: string[];
  recommendedFirst: boolean;
  variants: StoryVariant[];
}

export interface QualificationPack {
  manifest: QualificationManifest;
  knowledge: KnowledgeNode[];
  handbook: HandbookEntry[];
  stories: StoryCase[];
}
```

- [ ] **Step 3: Implement Zod parsers**

Each parser calls `YAML.parse`, validates with Zod, and normalizes optional collections. Rules:

```text
StoryChoice.effects defaults to {}
StoryCase.recommendedFirst defaults to false
KnowledgeNode.examConnection defaults to null
non-default StoryEnding.when defaults to []
LearningSignalDefinition.result is constrained to 0..1
```

Expose:

```ts
export function parseManifest(raw: string): QualificationManifest;
export function parseKnowledgeFile(raw: string): KnowledgeNode[];
export function parseHandbookFile(raw: string): HandbookEntry[];
export function parseStoryFile(raw: string): StoryCase;
```

- [ ] **Step 4: Implement browser content loading**

Use raw eager Vite globs:

```ts
const files = import.meta.glob('/src/study-content/**/*.yaml', {
  eager: true,
  query: '?raw',
  import: 'default',
}) as Record<string, string>;
```

Group files by qualification directory and expose:

```ts
export function loadContentPacks(): QualificationPack[];
```

This function parses but does not perform graph validation.

- [ ] **Step 5: Verify and commit**

```bash
npm test -- src/study/domain/content-schema.test.ts
git add src/study/domain/content-types.ts src/study/domain/content-schema.ts src/study/domain/content-schema.test.ts src/study/content/load-content.ts
git commit -m "feat: define study content contracts"
```

---

### Task 3: Content graph validator and build gate

**Files:**
- Create: `src/study/domain/validate-pack.ts`
- Create: `src/study/domain/validate-pack.test.ts`
- Create: `scripts/validate-study-content.ts`
- Modify: `package.json`

**Interfaces:**
- Produces `validatePack(pack): ValidationReport`.
- CLI exits `1` for structural errors and `0` when only warnings remain.

- [ ] **Step 1: Write failing validation tests**

Create minimal packs and assert exact codes:

```ts
expect(report.errors).toContainEqual(expect.objectContaining({ code: 'UNKNOWN_KNOWLEDGE_ID' }));
expect(report.errors).toContainEqual(expect.objectContaining({ code: 'UNKNOWN_SCENE_TARGET' }));
expect(report.errors).toContainEqual(expect.objectContaining({ code: 'UNREACHABLE_SCENE' }));
expect(report.errors).toContainEqual(expect.objectContaining({ code: 'INVALID_DEFAULT_ENDING_COUNT' }));
expect(report.warnings).toContainEqual(expect.objectContaining({ code: 'NO_STORY_COVERAGE' }));
```

Run:

```bash
npm test -- src/study/domain/validate-pack.test.ts
```

Expected: FAIL.

- [ ] **Step 2: Implement validation contracts**

```ts
export interface ValidationMessage {
  level: 'error' | 'warning';
  code: string;
  message: string;
  path: string;
}

export interface CoverageRow {
  knowledgeId: string;
  encounter: number;
  apply: number;
  discriminate: number;
  recall: number;
}

export interface ValidationReport {
  errors: ValidationMessage[];
  warnings: ValidationMessage[];
  coverage: CoverageRow[];
}
```

Validator checks all of these:

```text
manifest section/source IDs
knowledge source references
knowledge relation targets
handbook source and knowledge references
story section/targetKnowledge/learning references
story start scenes and choice targets
scene reachability
exactly one default ending per variant
all effect dimensions declared by story
resolution reachability
cycles that can avoid every resolution forever
```

Coverage is counted from `learning` definitions, not `targetKnowledge` declarations.

- [ ] **Step 3: Implement CLI**

`scripts/validate-study-content.ts` reads every pack from `src/study-content/`, uses Task 2 parsers, validates, prints errors/warnings/coverage, and sets `process.exitCode = 1` when structural errors exist. Zero content packs is an error.

- [ ] **Step 4: Wire validation before current prebuild commands**

Prefix the existing `prebuild` command with:

```text
npm run validate:study &&
```

Do not remove any existing Python figure-generation commands.

- [ ] **Step 5: Verify and commit**

```bash
npm test -- src/study/domain/validate-pack.test.ts
git add src/study/domain/validate-pack.ts src/study/domain/validate-pack.test.ts scripts/validate-study-content.ts package.json
git commit -m "feat: validate study content at build time"
```

---

### Task 4: Pure Story Engine

**Files:**
- Create: `src/study/domain/story-engine.ts`
- Create: `src/study/domain/story-engine.test.ts`

**Interfaces:**
- Produces immutable story sessions and emitted learning events.

- [ ] **Step 1: Write failing progression tests**

Test start, choice effects, handbook assistance, narrative advance, invalid choice rejection, and ending resolution:

```ts
const session = startStorySession(story, 'gasoline-leak', now);
expect(session.sceneId).toBe('arrival');

const outcome = choose(story, session, 'stop-ignition', now);
expect(outcome.session.dimensions.ignition).toBe(1);
expect(outcome.learningEvents[0]).toMatchObject({
  knowledgeId: 'class4.gasoline.vapor',
  mode: 'apply',
  result: 1,
  assistance: 'none',
});
```

- [ ] **Step 2: Define runtime shapes**

```ts
export interface LearningEvent {
  knowledgeId: string;
  mode: LearningMode;
  result: number;
  assistance: Assistance;
  context: string;
  caseId: string;
  variantId: string;
  timestamp: string;
}

export interface StorySession {
  caseId: string;
  variantId: string;
  sceneId: string;
  dimensions: Record<string, number>;
  choiceHistory: { sceneId: string; choiceId: string; timestamp: string }[];
  assistanceByKnowledge: Record<string, Assistance>;
  startedAt: string;
  updatedAt: string;
  endingId: string | null;
}
```

- [ ] **Step 3: Implement pure functions**

```ts
export function startStorySession(story: StoryCase, variantId: string, now: Date): StorySession;
export function advanceNarrative(story: StoryCase, session: StorySession, now: Date): StorySession;
export function markAssistance(session: StorySession, knowledgeIds: string[], assistance: Assistance, now: Date): StorySession;
export function choose(story: StoryCase, session: StorySession, choiceId: string, now: Date): { session: StorySession; learningEvents: LearningEvent[] };
export function resolveEnding(story: StoryCase, session: StorySession): StoryEnding;
```

Ending comparisons are exact:

```ts
const comparisons = {
  gte: (actual: number, expected: number) => actual >= expected,
  lte: (actual: number, expected: number) => actual <= expected,
  eq: (actual: number, expected: number) => actual === expected,
};
```

No function mutates inputs. Entering a `resolution` scene sets `endingId`.

- [ ] **Step 4: Verify and commit**

```bash
npm test -- src/study/domain/story-engine.test.ts
git add src/study/domain/story-engine.ts src/study/domain/story-engine.test.ts
git commit -m "feat: add deterministic story engine"
```

---

### Task 5: Learning Engine and deterministic recommendation

**Files:**
- Create: `src/study/domain/learning-engine.ts`
- Create: `src/study/domain/learning-engine.test.ts`
- Create: `src/study/domain/recommendation.ts`
- Create: `src/study/domain/recommendation.test.ts`

**Interfaces:**
- Does not depend on storage types.
- Produces `deriveKnowledgeState` and `rankVariants`.

- [ ] **Step 1: Write failing mastery tests**

Use fixed time:

```ts
const now = new Date('2026-09-14T00:00:00Z');
const state = deriveKnowledgeState([
  event('apply', 1, 'handbook', '2026-09-13T00:00:00Z'),
  event('apply', 1, 'none', '2026-09-14T00:00:00Z'),
], now);
expect(state.apply).toBeGreaterThan(0.75);
expect(state.helpDependence).toBe(0.5);
```

Also assert empty histories return finite zeros.

- [ ] **Step 2: Implement the MVP learning model**

```ts
const assistanceFactor: Record<Assistance, number> = {
  none: 1,
  handbook: 0.75,
  hint: 0.5,
  other: 0.6,
};

const recencyWeight = (ageDays: number) => Math.exp(-ageDays / 90);
```

For each mode:

```text
weightedScore = sum(result * assistanceFactor * recencyWeight) / sum(recencyWeight)
```

Return:

```ts
export interface KnowledgeState {
  encounter: number;
  apply: number;
  discriminate: number;
  recall: number;
  helpDependence: number;
  eventCount: number;
  lastSeenAt: string | null;
}
```

Rules:

```text
encounter = min(1, eventCount / 3)
apply/discriminate = weighted score or 0
recall = recall weighted score when recall evidence exists
recall fallback = apply * exp(-daysSinceLatestSuccessfulUnaidedApply / 45)
helpDependence = assistedEventCount / eventCount
```

Clamp scores to `[0,1]`.

- [ ] **Step 3: Define recommendation input independent of persistence**

```ts
export interface VariantVisit {
  caseId: string;
  variantId: string;
  completedAt: string;
}

export interface RankedVariant {
  caseId: string;
  variantId: string;
  score: number;
}
```

`rankVariants` signature:

```ts
export function rankVariants(
  pack: QualificationPack,
  events: LearningEvent[],
  visits: VariantVisit[],
  now: Date,
): RankedVariant[];
```

- [ ] **Step 4: Write failing recommendation tests and implement ranking**

Priority per node:

```text
0.35*(1-apply) + 0.25*(1-discriminate) + 0.25*(1-recall) + 0.15*recencyGap
recencyGap = min(1, daysSinceLastSeen/30), or 1 if unseen
```

Variant score is mean priority of its `targetKnowledge`. Subtract `0.05` only if the exact variant is the most recent completed visit. Break ties by `caseId`, then `variantId`.

- [ ] **Step 5: Verify and commit**

```bash
npm test -- src/study/domain/learning-engine.test.ts src/study/domain/recommendation.test.ts
git add src/study/domain/learning-engine.ts src/study/domain/learning-engine.test.ts src/study/domain/recommendation.ts src/study/domain/recommendation.test.ts
git commit -m "feat: derive mastery and recommend variants"
```

---

### Task 6: IndexedDB repository, resume support, and safe recovery

**Files:**
- Create: `src/study/storage/repository.ts`
- Create: `src/study/storage/memory-repository.ts`
- Create: `src/study/storage/repository.test.ts`

**Interfaces:**
- Produces `StudyRepository` and `createStudyRepository`.
- Storage converts `CaseHistoryEntry[]` to Task 5 `VariantVisit[]` at the UI boundary; recommendation never imports repository types.

- [ ] **Step 1: Write failing persistence tests**

Test append/list events, save/load session, atomic completion, and history:

```ts
await repo.appendLearningEvents([learningEvent]);
expect(await repo.listLearningEvents()).toHaveLength(1);
await repo.saveActiveSession(session);
expect(await repo.loadActiveSession(session.caseId)).toMatchObject({ variantId: session.variantId });
await repo.completeSession(session, 'controlled', completedAt);
expect(await repo.loadActiveSession(session.caseId)).toBeNull();
expect(await repo.listCaseHistory()).toHaveLength(1);
```

- [ ] **Step 2: Define storage contracts**

```ts
export interface CaseHistoryEntry {
  id: string;
  caseId: string;
  variantId: string;
  endingId: string;
  startedAt: string;
  completedAt: string;
  choiceHistory: StorySession['choiceHistory'];
}

export interface StudySnapshot {
  schemaVersion: number;
  learningEvents: LearningEvent[];
  caseHistory: CaseHistoryEntry[];
  activeSessions: StorySession[];
}

export interface StudyRepository {
  appendLearningEvents(events: LearningEvent[]): Promise<void>;
  listLearningEvents(): Promise<LearningEvent[]>;
  saveActiveSession(session: StorySession): Promise<void>;
  loadActiveSession(caseId: string): Promise<StorySession | null>;
  listActiveSessions(): Promise<StorySession[]>;
  completeSession(session: StorySession, endingId: string, completedAt: Date): Promise<void>;
  listCaseHistory(): Promise<CaseHistoryEntry[]>;
  exportSnapshot(): Promise<StudySnapshot>;
}

export interface RepositoryBootstrap {
  repository: StudyRepository;
  persistent: boolean;
  warning: 'none' | 'unavailable' | 'incompatible-schema';
  recoverySnapshot: StudySnapshot | null;
}
```

- [ ] **Step 3: Implement IndexedDB v1**

Database: `qualification-study`, version `1`.

Stores:

```text
learning-events  keyPath id, autoIncrement
case-history     keyPath id
active-sessions  keyPath caseId
settings         keyPath key
```

Write `{ key: 'schema-version', value: 1 }` during upgrade. `completeSession` writes history and removes the active session in one transaction.

- [ ] **Step 4: Implement memory fallback and incompatible-version recovery**

Normal IndexedDB open failure returns an empty `MemoryStudyRepository`, `persistent:false`, `warning:'unavailable'`.

For `VersionError`, open the existing DB without specifying a version, read recognized stores if present, create a `StudySnapshot`, close it without writes, then return:

```ts
{
  repository: new MemoryStudyRepository(),
  persistent: false,
  warning: 'incompatible-schema',
  recoverySnapshot,
}
```

Never delete or downgrade the existing database.

- [ ] **Step 5: Test incompatible DB preservation**

In fake IndexedDB, create `qualification-study` version `2` containing recognized v1 stores, insert one event, then call `createStudyRepository()`. Assert `warning === 'incompatible-schema'`, `recoverySnapshot.learningEvents.length === 1`, and the original version-2 DB still exists.

- [ ] **Step 6: Verify and commit**

```bash
npm test -- src/study/storage/repository.test.ts
git add src/study/storage/repository.ts src/study/storage/memory-repository.ts src/study/storage/repository.test.ts
git commit -m "feat: persist and recover study progress"
```

---

### Task 7: Sourced 乙4 性消 knowledge catalog and handbook

**Files:**
- Create: `src/study-content/hazardous-materials/manifest.yaml`
- Create: `src/study-content/hazardous-materials/knowledge/class4-common.yaml`
- Create: `src/study-content/hazardous-materials/knowledge/class4-substances.yaml`
- Create: `src/study-content/hazardous-materials/knowledge/fire-prevention.yaml`
- Create: `src/study-content/hazardous-materials/knowledge/extinguishing.yaml`
- Create: `src/study-content/hazardous-materials/handbook/classification.yaml`
- Create: `src/study-content/hazardous-materials/handbook/fire-response.yaml`
- Create: `docs/study-content/otsu4-seisho-coverage.md`
- Modify: `src/study/domain/validate-pack.ts`
- Modify: `src/study/domain/validate-pack.test.ts`

**Interfaces:**
- Produces the canonical curriculum/source graph for initial 乙4 content.

- [ ] **Step 1: Add failing provenance tests**

Assert knowledge/handbook entries with empty `sources` fail `MISSING_PROVENANCE`, unknown source IDs fail `UNKNOWN_SOURCE_ID`, non-HTTPS source URLs fail `INVALID_SOURCE_URL`, and malformed dates fail `INVALID_SOURCE_DATE`.

- [ ] **Step 2: Implement provenance validation**

Every knowledge node and handbook entry needs at least one manifest source. Source URL must be HTTPS; `checkedAt` must match `YYYY-MM-DD`.

- [ ] **Step 3: Author source registry from authoritative material**

Use current primary/official sources available at implementation time: Fire and Disaster Management Agency resources, e-Gov statutes/regulations, official fire-science/government publications, and official SDS documents for substance-specific physical properties. Do not use exam-prep blogs as factual provenance.

The manifest must include:

```yaml
id: hazardous-materials
title: 危険物取扱者
sections:
  - id: otsu4-seisho
    title: 乙種第4類・性質／火災予防／消火
```

Every source stores its exact URL and actual verification date.

- [ ] **Step 4: Build the human-auditable curriculum checklist**

`docs/study-content/otsu4-seisho-coverage.md` headings:

```text
第4類共通の性質
特殊引火物
第一石油類
アルコール類
第二石油類
第三石油類
第四石油類
動植物油類
代表物質の識別
火災予防
消火原理・消火方法
水溶性／非水溶性の区別
蒸気・静電気・着火源に関する判断
```

Under each heading list the implemented knowledge IDs and their source IDs. Each knowledge node is atomic enough to be applied or discriminated in a decision.

- [ ] **Step 5: Author the handbook**

`classification.yaml` contains concise classification/identification references; `fire-response.yaml` contains concise fire-prevention/extinguishing decision references. Each entry links existing knowledge IDs and source IDs.

- [ ] **Step 6: Validate**

```bash
npm run validate:study
```

Expected: `0 errors`; `NO_STORY_COVERAGE` warnings are expected before Tasks 8–10.

- [ ] **Step 7: Commit**

```bash
git add src/study-content/hazardous-materials docs/study-content/otsu4-seisho-coverage.md src/study/domain/validate-pack.ts src/study/domain/validate-pack.test.ts
git commit -m "feat: add sourced otsu4 knowledge catalog"
```

---

### Task 8: Author three replayable story cases with two variants each

**Files:**
- Create: `src/study-content/hazardous-materials/stories/warehouse.yaml`
- Create: `src/study-content/hazardous-materials/stories/solvent-workplace.yaml`
- Create: `src/study-content/hazardous-materials/stories/unknown-liquid.yaml`
- Create: `src/study/domain/story-content.test.ts`

**Interfaces:**
- Produces case IDs `warehouse`, `solvent-workplace`, `unknown-liquid`.
- Produces exactly these initial variant IDs:
  - `warehouse`: `gasoline-leak`, `ether-container`
  - `solvent-workplace`: `ethanol-spill`, `toluene-spill`
  - `unknown-liquid`: `unknown-gasoline`, `unknown-kerosene`

- [ ] **Step 1: Write failing content acceptance tests**

Assert all three cases exist, duration is 10–15 minutes, each has at least two variants, and each authored safe path has 5–8 decisions before resolution.

Assert `unknown-liquid` first decision text/choices do not reveal the hidden substance name.

Assert the union of learning signals includes `apply`, `discriminate`, and `recall` modes.

- [ ] **Step 2: Author `warehouse.yaml`**

Required decision themes:

```text
initial response to odor/leak
action that may create/avoid ignition source
vapor accumulation reasoning
containment/ventilation choice
fire-response choice
```

Use at least dimensions `identification`, `ignition`, `containment`. At least three endings per variant: controlled, partial containment/remaining hazard, escalation. Exactly one default ending.

- [ ] **Step 3: Author `solvent-workplace.yaml`**

Required themes:

```text
select relevant evidence
distinguish water-solubility implications
avoid ignition source
choose spill/fire response
reassess after new consequence information
```

Use dimensions `identification`, `ignition`, `extinguishing`. Include an ending where ignition prevention succeeds despite imperfect identification.

- [ ] **Step 4: Author `unknown-liquid.yaml`**

Required themes:

```text
choose useful evidence first
infer risk from provided property information
reason about vapor/fire behavior
choose handling response
choose fire response
make final classification inference
```

Use dimensions `identification`, `ignition`, `extinguishing`, `evidence`. At least one ending must be operationally safe despite incomplete identification.

- [ ] **Step 5: Enforce consequence-first wording**

No choice/consequence text may contain `正解` or `不正解`. Factual claims must map to sourced knowledge IDs; do not duplicate unsupported facts only in prose.

- [ ] **Step 6: Verify**

```bash
npm test -- src/study/domain/story-content.test.ts
npm run validate:study
```

Expected: PASS, `0 structural errors`. Remaining coverage warnings are compared with `docs/study-content/otsu4-seisho-coverage.md` and are allowed in MVP.

- [ ] **Step 7: Commit**

```bash
git add src/study-content/hazardous-materials/stories src/study/domain/story-content.test.ts
git commit -m "feat: add initial otsu4 story cases"
```

---

### Task 9: Qualification picker, case library, recommendation, and storage warnings

**Files:**
- Modify: `src/study/ui/StudyApp.tsx`
- Create: `src/study/ui/QualificationPicker.tsx`
- Create: `src/study/ui/CaseLibrary.tsx`
- Create: `src/study/ui/StorageWarning.tsx`
- Modify: `src/study/ui/study-app.test.tsx`
- Modify: `src/styles/study.css`

**Interfaces:**
- Consumes content packs, repository bootstrap, learning events/history, Task 5 recommendation.
- Produces qualification selection before case selection.

- [ ] **Step 1: Write failing navigation test**

Test flow:

```text
render StudyApp
see 危険物取扱者 qualification card
select it
see the three case titles
all three start buttons are enabled
one case has a recommendation indicator
```

- [ ] **Step 2: Implement application bootstrap**

On mount:

```text
load content packs
create repository
load events
load case history
load active sessions
```

Use UI state:

```ts
type ScreenState =
  | { screen: 'qualifications' }
  | { screen: 'library'; qualificationId: string }
  | { screen: 'story'; qualificationId: string; caseId: string; session: StorySession }
  | { screen: 'debrief'; qualificationId: string; caseId: string; historyId: string }
  | { screen: 'knowledge'; qualificationId: string };
```

- [ ] **Step 3: Implement QualificationPicker and CaseLibrary**

QualificationPicker shows `manifest.title`. CaseLibrary shows title, summary, 10–15 minute estimate, completion count, optional recommendation badge, and `続きから` for active sessions.

Convert history to recommendation input without importing storage types into recommendation:

```ts
const visits = history.map(({ caseId, variantId, completedAt }) => ({
  caseId,
  variantId,
  completedAt,
}));
```

All cases remain selectable regardless of recommendation.

- [ ] **Step 4: Implement storage warning/recovery UI**

For `unavailable` show:

```text
このブラウザでは学習履歴を保存できません。現在のセッションはページを閉じると失われます。
```

For `incompatible-schema`, show that existing data was left untouched and expose a `既存データを書き出す` button that serializes `recoverySnapshot` as JSON using `Blob` + object URL. This is emergency recovery only; import/sync remain excluded.

- [ ] **Step 5: Responsive CSS**

Use inherited site typography/colors. Cards become one column at 360px; interactive controls have minimum height 44px.

- [ ] **Step 6: Verify and commit**

```bash
npm test -- src/study/ui/study-app.test.tsx
git add src/study/ui/StudyApp.tsx src/study/ui/QualificationPicker.tsx src/study/ui/CaseLibrary.tsx src/study/ui/StorageWarning.tsx src/study/ui/study-app.test.tsx src/styles/study.css
git commit -m "feat: add qualification and case selection"
```

---

### Task 10: Story Player, handbook assistance, autosave, and resume

**Files:**
- Create: `src/study/ui/StoryPlayer.tsx`
- Create: `src/study/ui/HandbookDrawer.tsx`
- Modify: `src/study/ui/StudyApp.tsx`
- Modify: `src/study/ui/study-app.test.tsx`
- Modify: `src/styles/study.css`

**Interfaces:**
- Consumes Story Engine, handbook entries, StudyRepository.
- Produces consequence-first play with persisted progress.

- [ ] **Step 1: Write failing interaction test**

Open `warehouse`, choose a decision, assert consequence text appears, and assert the document does not contain `正解` or `不正解`. Open a handbook entry linked to the next decision's knowledge node, choose that decision, and verify the stored learning event has `assistance:'handbook'`.

- [ ] **Step 2: Implement scene rendering**

```text
narrative -> text + 続ける
decision -> text + choice buttons
resolution -> ending text + ケースを振り返る
```

Do not display internal dimensions/mastery during the case.

- [ ] **Step 3: Implement handbook tracking**

Opening a specific handbook entry calls:

```ts
markAssistance(session, entry.knowledgeIds, 'handbook', now)
```

Opening/closing the drawer alone does not count as assistance.

- [ ] **Step 4: Autosave every state transition**

After narrative advance, choice, or assistance mark:

```text
save active session
append any emitted learning events
```

When resolution is reached, leave the ended session active until `ケースを振り返る` is selected so a refresh on the ending screen can resume safely.

- [ ] **Step 5: Resume test**

Start a case, make two choices, unmount the app, remount with the same fake IndexedDB, enter the same qualification/case, click `続きから`, and assert the previously persisted scene is restored.

- [ ] **Step 6: Verify and commit**

```bash
npm test -- src/study/ui/study-app.test.tsx src/study/domain/story-engine.test.ts
git add src/study/ui/StoryPlayer.tsx src/study/ui/HandbookDrawer.tsx src/study/ui/StudyApp.tsx src/study/ui/study-app.test.tsx src/styles/study.css
git commit -m "feat: add branching story player"
```

---

### Task 11: Debrief and simple/detailed learning-state views

**Files:**
- Create: `src/study/ui/Debrief.tsx`
- Create: `src/study/ui/KnowledgeView.tsx`
- Modify: `src/study/ui/StudyApp.tsx`
- Modify: `src/study/ui/study-app.test.tsx`
- Modify: `src/styles/study.css`

**Interfaces:**
- Consumes ended StorySession, case data, knowledge graph, events, Learning Engine.
- Produces debrief and both learner-facing mastery views.

- [ ] **Step 1: Write failing debrief test**

Complete a case and assert debrief includes:

```text
あなたの判断
起きたこと
関係する知識
試験ではどう問われるか
```

At least one related knowledge title must be visible.

- [ ] **Step 2: Implement completion handoff**

When `ケースを振り返る` is selected:

```text
completeSession(session, endingId, now)
reload history/events
recompute recommendation
navigate to debrief
```

Debrief reconstructs choice labels/consequence context from story data plus `choiceHistory`; it does not store duplicate story prose in IndexedDB.

- [ ] **Step 3: Implement consequence-to-knowledge debrief**

Show major choice, observed consequence, linked atomic knowledge statements, handbook links, and `examConnection` when present. Do not show a single overall percentage score.

- [ ] **Step 4: Implement simple Knowledge View**

Text bands:

```text
apply >= 0.8 and recall >= 0.7 -> 安定して使えている
apply >= 0.55 -> 使える場面が増えている
encounter > 0 -> もう一度別の状況で使いたい
encounter == 0 -> まだケースで扱っていない
```

If `helpDependence >= 0.5`, append `資料を参照しながら使った経験が多い。`

- [ ] **Step 5: Implement detailed Knowledge View**

`詳細を見る` reveals numeric `encounter`, `apply`, `discriminate`, `recall`, `helpDependence`, `eventCount`, and `lastSeenAt`. Use accessible progress/table elements; do not add a chart library.

- [ ] **Step 6: Verify and commit**

```bash
npm test -- src/study/ui/study-app.test.tsx
git add src/study/ui/Debrief.tsx src/study/ui/KnowledgeView.tsx src/study/ui/StudyApp.tsx src/study/ui/study-app.test.tsx src/styles/study.css
git commit -m "feat: add debrief and knowledge views"
```

---

### Task 12: Site integration, full checks, and deployment readiness

**Files:**
- Modify: `src/components/SiteHeader.astro`
- Modify: `src/study/ui/study-app.test.tsx`
- Modify: `package.json`
- Modify: `package-lock.json`
- Modify: `README.md`

**Interfaces:**
- Produces a discoverable `/study/` application and one repeatable verification command.

- [ ] **Step 1: Add Study navigation**

Before `About` in `SiteHeader.astro`:

```astro
<a href="/study/" aria-current={path.startsWith('/study') ? 'page' : undefined}>Study</a>
```

- [ ] **Step 2: Add one full UI integration flow**

The test must execute:

```text
qualification picker
warehouse case selection
>=5 decisions
one handbook entry opened
ending reached
debrief opened
return to case library
completion count increased
Knowledge View opened
detailed mastery row displayed
```

Seed an empty repository and fixed clock. Mark `warehouse` as `recommendedFirst:true`; initial deterministic tie behavior must choose `warehouse/gasoline-leak`.

- [ ] **Step 3: Add Astro type checking and combined study check**

```bash
npm install -D @astrojs/check typescript
```

Add:

```json
{
  "check:study": "npm run validate:study && vitest run && astro check"
}
```

Do not add another deployment workflow. Existing Pages deployment remains authoritative; `prebuild` already runs content validation.

- [ ] **Step 4: Document development and storage behavior**

README `Study app` section documents:

```bash
npm run dev
npm test
npm run validate:study
npm run check:study
npm run build
```

Also state that normal learning history is browser-local IndexedDB, clearing site data resets it, and emergency JSON export appears only when an incompatible stored schema is detected.

- [ ] **Step 5: Run automated verification**

```bash
npm run validate:study
npm test
npx astro check
npm run build
```

Expected:

```text
0 structural content errors
all Vitest tests pass
Astro check exits 0
Astro build exits 0
dist/study/index.html exists
```

Coverage warnings are acceptable only when the corresponding nodes are explicitly listed as not yet story-covered in `docs/study-content/otsu4-seisho-coverage.md`.

- [ ] **Step 6: Smoke-test production preview**

```bash
npm run preview
```

Verify:

```text
/study/ direct load works
qualification picker opens 危険物取扱者
all three cases are selectable in any order
refresh during a case resumes progress
handbook is usable at mobile width
ending waits for explicit debrief transition
completion changes learning state/recommendation
/notes/, /topics/, /now/, /about/ still render
```

- [ ] **Step 7: Commit**

```bash
git add src/components/SiteHeader.astro src/study/ui/study-app.test.tsx package.json package-lock.json README.md
git commit -m "feat: integrate study platform into site"
```

---

## Final Verification Gate

Run from a clean checkout after dependency installation:

```bash
npm run validate:study
npm test
npx astro check
npm run build
```

Then confirm every spec requirement has evidence:

```text
Qualification selection exists before case library.
Cases are unordered and recommendation never locks content.
Story decisions show consequences, not immediate correct/incorrect labels.
No early failure termination exists.
Each of 3 cases has >=2 authored variants.
Handbook use is recorded as assistance, not failure.
Learning events are persisted as canonical history.
E/A/D/R/H state is derived and inspectable in simple + detailed forms.
Variant recommendation targets weak concepts rather than failed question IDs.
Knowledge nodes and handbook entries have authoritative provenance.
Validator reports encounter/apply/discriminate/recall coverage.
Interrupted cases resume.
IndexedDB failure falls back to memory without blocking play.
Incompatible future DB versions are not deleted and known data is recoverable as JSON.
Debrief connects decisions -> consequences -> knowledge -> exam framing.
Story/learning engines contain no 乙4-specific logic.
Existing Astro pages still build and render.
```

If any line above cannot be demonstrated by test, validator output, source data, or manual smoke check, fix it before opening or merging the implementation PR.
