# Qualification Study Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable, fully static qualification-study application under `/study/` that teaches through replayable branching cases, beginning with three validated 乙4「性質・火災予防・消火」cases.

**Architecture:** Keep the existing Astro 7 static site and mount one React application under `/study/`. Qualification content is authored as YAML and compiled into the client bundle; a pure Story Engine and Learning Engine operate on validated content, while IndexedDB stores event history and resumable sessions. A Node-side validator reuses the same schemas and blocks builds on structural content errors.

**Tech Stack:** Astro 7.3.x, React, TypeScript, Zod, YAML, idb/IndexedDB, Vitest, Testing Library, jsdom, fake-indexeddb, tsx, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-14-qualification-study-platform-design.md`

## Global Constraints

- Preserve the existing Astro static deployment model and GitHub Pages workflow.
- Runtime must require no server, account system, API key, or cross-device synchronization.
- `/study/` is the only new application surface; existing notes/topics/about pages remain unaffected.
- Story content, qualification knowledge, engines, persistence, and UI remain separate modules.
- The persisted source of truth for learning is the event log; derived mastery values are recomputable.
- Wrong decisions do not immediately show `Correct` / `Incorrect` and do not terminate a case early.
- Each initial case must contain at least two authored variants; runtime LLM generation is excluded.
- Initial story cases are playable in any order; recommendation is advisory only.
- Hazardous-material facts require explicit provenance metadata and a `checkedAt` date.
- Structural content validation fails the build; incomplete curriculum story coverage is reported but does not fail the MVP build.
- No XP, coins, leaderboards, login streak rewards, social features, or authoring GUI in the MVP.

---

## File Structure

Create or modify the project around these boundaries:

```text
astro.config.mjs                         # add React integration
package.json / package-lock.json         # runtime, test, and validation dependencies/scripts
vitest.config.ts                         # unit/integration test configuration
src/test/setup.ts                        # jest-dom + fake IndexedDB test setup
src/pages/study/index.astro              # Astro host for the React study app
src/components/SiteHeader.astro          # add Study navigation entry
src/styles/study.css                     # study-only responsive visual system

src/study/domain/content-types.ts        # stable TypeScript domain interfaces
src/study/domain/content-schema.ts       # Zod schemas and YAML parsing contracts
src/study/domain/validate-pack.ts        # graph/content validation and coverage report
src/study/domain/story-engine.ts         # pure case progression
src/study/domain/learning-engine.ts      # event -> derived knowledge state
src/study/domain/recommendation.ts       # next case/variant ranking
src/study/domain/*.test.ts               # pure-engine tests

src/study/content/load-content.ts        # Vite raw YAML loading + validated pack assembly
src/study/storage/repository.ts           # storage interface + IndexedDB implementation
src/study/storage/memory-repository.ts    # non-persistent fallback
src/study/storage/repository.test.ts      # persistence/migration/resume tests

src/study/ui/StudyApp.tsx                # top-level application state
src/study/ui/CaseLibrary.tsx             # case selection/recommendation
src/study/ui/StoryPlayer.tsx             # narrative + decisions
src/study/ui/HandbookDrawer.tsx          # in-case references
src/study/ui/Debrief.tsx                 # consequence-to-knowledge review
src/study/ui/KnowledgeView.tsx            # simple + detailed learning state
src/study/ui/StorageWarning.tsx          # memory fallback warning
src/study/ui/study-app.test.tsx          # user-flow integration tests

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

docs/study-content/otsu4-seisho-coverage.md   # human-reviewable curriculum/source checklist
scripts/validate-study-content.ts             # CLI used by local checks and build
```

---

### Task 1: Add the React study surface and test foundation

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
- Produces: default React component `StudyApp(): JSX.Element`.
- Produces: `npm test`, `npm run test:watch`, and a jsdom environment with jest-dom and fake IndexedDB.
- Consumes: existing `BaseLayout.astro` and static Astro configuration.

- [ ] **Step 1: Install runtime and test dependencies**

Run:

```bash
npm install @astrojs/react react react-dom zod yaml idb
npm install -D vitest @testing-library/react @testing-library/jest-dom jsdom fake-indexeddb tsx @types/react @types/react-dom
```

Then add these scripts to `package.json` without removing the existing build/figure scripts:

```json
{
  "test": "vitest run",
  "test:watch": "vitest",
  "validate:study": "tsx scripts/validate-study-content.ts"
}
```

- [ ] **Step 2: Write the failing mount test**

Create `src/study/ui/study-app.test.tsx`:

```tsx
import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import StudyApp from './StudyApp';

describe('StudyApp', () => {
  it('renders the study application heading', () => {
    render(<StudyApp />);
    expect(screen.getByRole('heading', { name: '資格学習' })).toBeInTheDocument();
  });
});
```

- [ ] **Step 3: Run the test and verify the expected failure**

Run:

```bash
npm test -- src/study/ui/study-app.test.tsx
```

Expected: FAIL because `StudyApp.tsx` and the test environment are not configured yet.

- [ ] **Step 4: Configure React, Vitest, and the minimum application shell**

Update `astro.config.mjs` to include the React integration while preserving `site`, `output`, `trailingSlash`, and markdown plugins:

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

Create `src/study/ui/StudyApp.tsx`:

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

Create `src/pages/study/index.astro` using the existing base layout:

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

Create `src/styles/study.css` with only the first layout primitives:

```css
.study-shell {
  width: min(72rem, calc(100% - 2rem));
  margin: 0 auto;
  padding: 2rem 0 4rem;
}
```

- [ ] **Step 5: Verify test and production build**

Run:

```bash
npm test -- src/study/ui/study-app.test.tsx
npm run build
```

Expected: both PASS; `dist/study/index.html` exists.

- [ ] **Step 6: Commit**

```bash
git add package.json package-lock.json astro.config.mjs vitest.config.ts src/test/setup.ts src/pages/study/index.astro src/study/ui/StudyApp.tsx src/styles/study.css src/study/ui/study-app.test.tsx
git commit -m "feat: add study app React surface"
```

---

### Task 2: Define the qualification-content contracts and YAML parser

**Files:**
- Create: `src/study/domain/content-types.ts`
- Create: `src/study/domain/content-schema.ts`
- Create: `src/study/domain/content-schema.test.ts`
- Create: `src/study/content/load-content.ts`

**Interfaces:**
- Produces: `parseManifest(raw: string): QualificationManifest`.
- Produces: `parseKnowledgeFile(raw: string): KnowledgeNode[]`.
- Produces: `parseHandbookFile(raw: string): HandbookEntry[]`.
- Produces: `parseStoryFile(raw: string): StoryCase`.
- Produces: `loadContentPacks(): QualificationPack[]` for the React app.

- [ ] **Step 1: Write schema tests for a minimal valid case and an invalid knowledge reference shape**

Create `src/study/domain/content-schema.test.ts`:

```ts
import { describe, expect, it } from 'vitest';
import { parseStoryFile } from './content-schema';

describe('parseStoryFile', () => {
  it('parses a decision and explicit ending rule', () => {
    const story = parseStoryFile(`
id: warehouse
qualificationId: hazardous-materials
section: otsu4-seisho
title: ガソリン臭のする倉庫
durationMinutes: 12
dimensions: [identification, ignition]
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
    expect(story.variants[0].endings[0].id).toBe('controlled');
  });

  it('rejects a decision choice without a next scene', () => {
    expect(() => parseStoryFile(`
id: broken
qualificationId: hazardous-materials
section: otsu4-seisho
title: 壊れたケース
durationMinutes: 10
dimensions: [ignition]
variants:
  - id: broken-v1
    startScene: arrival
    targetKnowledge: []
    scenes:
      arrival:
        kind: decision
        text: 状況
        choices:
          - id: bad
            text: 選ぶ
            learning: []
    endings:
      - id: end
        default: true
        text: 終了
`)).toThrow();
  });
});
```

- [ ] **Step 2: Run the test and verify it fails**

```bash
npm test -- src/study/domain/content-schema.test.ts
```

Expected: FAIL because parser/types do not exist.

- [ ] **Step 3: Define the stable TypeScript domain interfaces**

Create `src/study/domain/content-types.ts` with these exported interfaces and unions:

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
  section: string;
  tags: string[];
  relations: { type: 'prerequisite' | 'contrasts_with' | 'example_of' | 'derived_from' | 'used_with'; target: string }[];
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

- [ ] **Step 4: Implement Zod schemas and parsers**

Create `src/study/domain/content-schema.ts`. Each YAML parser must call `YAML.parse`, validate with Zod, and normalize omitted optional collections to empty arrays/objects. For story choices, `effects` defaults to `{}`; for story cases, `recommendedFirst` defaults to `false`; for non-default endings, `when` defaults to `[]`; exactly one default ending is checked later by pack validation.

Expose exactly:

```ts
export function parseManifest(raw: string): QualificationManifest;
export function parseKnowledgeFile(raw: string): KnowledgeNode[];
export function parseHandbookFile(raw: string): HandbookEntry[];
export function parseStoryFile(raw: string): StoryCase;
```

For every `LearningSignalDefinition.result`, enforce `0 <= result <= 1`.

- [ ] **Step 5: Implement the browser bundle loader**

Create `src/study/content/load-content.ts` using raw eager Vite globs:

```ts
const files = import.meta.glob('/src/study-content/**/*.yaml', {
  eager: true,
  query: '?raw',
  import: 'default',
}) as Record<string, string>;
```

Group files by qualification directory, parse the one `manifest.yaml`, all `knowledge/*.yaml`, all `handbook/*.yaml`, and all `stories/*.yaml`, then return `QualificationPack[]` from:

```ts
export function loadContentPacks(): QualificationPack[];
```

Do not perform graph validation here; Task 3 provides reusable pack validation.

- [ ] **Step 6: Run tests**

```bash
npm test -- src/study/domain/content-schema.test.ts
```

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add src/study/domain/content-types.ts src/study/domain/content-schema.ts src/study/domain/content-schema.test.ts src/study/content/load-content.ts
git commit -m "feat: define study content contracts"
```

---

### Task 3: Build reusable content validation and fail-fast build integration

**Files:**
- Create: `src/study/domain/validate-pack.ts`
- Create: `src/study/domain/validate-pack.test.ts`
- Create: `scripts/validate-study-content.ts`
- Modify: `package.json`

**Interfaces:**
- Consumes: `QualificationPack` from Task 2.
- Produces: `validatePack(pack: QualificationPack): ValidationReport`.
- Produces: CLI command `npm run validate:study` with exit code `1` on structural errors.

- [ ] **Step 1: Write failing validation tests**

Create `src/study/domain/validate-pack.test.ts` with a helper that builds a minimal valid pack, then assert these exact failures independently:

```ts
expect(validatePack(packWithUnknownKnowledge).errors).toContainEqual(
  expect.objectContaining({ code: 'UNKNOWN_KNOWLEDGE_ID' }),
);
expect(validatePack(packWithMissingScene).errors).toContainEqual(
  expect.objectContaining({ code: 'UNKNOWN_SCENE_TARGET' }),
);
expect(validatePack(packWithUnreachableScene).errors).toContainEqual(
  expect.objectContaining({ code: 'UNREACHABLE_SCENE' }),
);
expect(validatePack(packWithNoDefaultEnding).errors).toContainEqual(
  expect.objectContaining({ code: 'INVALID_DEFAULT_ENDING_COUNT' }),
);
```

Also assert a knowledge node with no story reference produces a warning with code `NO_STORY_COVERAGE`, not an error.

- [ ] **Step 2: Run the test and verify failure**

```bash
npm test -- src/study/domain/validate-pack.test.ts
```

Expected: FAIL because `validatePack` does not exist.

- [ ] **Step 3: Implement graph validation and coverage reporting**

Define:

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

export function validatePack(pack: QualificationPack): ValidationReport;
```

Validation must check:

```text
manifest/source references exist
knowledge relation targets exist
handbook knowledge/source references exist
story targetKnowledge references exist
learning knowledge IDs exist
choice next scene targets exist
startScene exists
all scenes are reachable from startScene
resolution scenes can select an ending
exactly one default ending per variant
no graph cycle can avoid every resolution scene
all content section IDs exist in manifest
all story dimensions referenced by effects exist in story.dimensions
```

Coverage counts are computed from `learning` definitions; a `targetKnowledge` listing alone does not count as encounter/apply/discriminate/recall coverage.

- [ ] **Step 4: Implement the CLI**

`scripts/validate-study-content.ts` must read `src/study-content/*` from the filesystem, call the Task 2 parsers, run `validatePack`, print one compact report per qualification, and set `process.exitCode = 1` if any errors exist.

On success, print a line in this form:

```text
hazardous-materials: 0 errors, 12 warnings, 42 knowledge nodes
```

The numbers come from the actual report; do not hard-code them.

- [ ] **Step 5: Wire validator before existing prebuild work**

Modify `package.json` so the existing `prebuild` command begins with:

```text
npm run validate:study &&
```

Keep every existing Python figure-generation command after it and preserve `build: astro build`.

- [ ] **Step 6: Verify tests and CLI behavior against a temporary invalid fixture created inside the test only**

Run:

```bash
npm test -- src/study/domain/validate-pack.test.ts
```

Expected: PASS.

At this point `npm run validate:study` may report that no production content packs exist; the CLI should treat zero packs as an error with code `NO_CONTENT_PACKS` so deployment cannot silently ship an empty study app.

- [ ] **Step 7: Commit**

```bash
git add src/study/domain/validate-pack.ts src/study/domain/validate-pack.test.ts scripts/validate-study-content.ts package.json
git commit -m "feat: validate study content at build time"
```

---

### Task 4: Implement the pure Story Engine

**Files:**
- Create: `src/study/domain/story-engine.ts`
- Create: `src/study/domain/story-engine.test.ts`

**Interfaces:**
- Consumes: `StoryCase`, `StoryVariant`, `Assistance`, `LearningSignalDefinition`.
- Produces: `startStorySession`, `advanceNarrative`, `choose`, `markAssistance`, `resolveEnding`.
- Later tasks persist the returned `StorySession` unchanged.

- [ ] **Step 1: Write failing progression tests**

Define a two-decision test story. Assert:

```ts
const session = startStorySession(story, 'gasoline-leak', now);
expect(session.sceneId).toBe('arrival');

const afterChoice = choose(story, session, 'stop-ignition', now);
expect(afterChoice.session.dimensions.ignition).toBe(1);
expect(afterChoice.learningEvents[0]).toMatchObject({
  knowledgeId: 'class4.gasoline.vapor',
  mode: 'apply',
  result: 1,
  assistance: 'none',
});
```

Also test that a handbook mark applied before the choice changes emitted assistance to `handbook`, and that a resolution scene selects the first matching non-default ending before the default ending.

- [ ] **Step 2: Run and verify failure**

```bash
npm test -- src/study/domain/story-engine.test.ts
```

Expected: FAIL because the engine does not exist.

- [ ] **Step 3: Define session/event contracts in `story-engine.ts`**

Use these exact runtime shapes:

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

- [ ] **Step 4: Implement deterministic pure functions**

Expose:

```ts
export function startStorySession(story: StoryCase, variantId: string, now: Date): StorySession;
export function advanceNarrative(story: StoryCase, session: StorySession, now: Date): StorySession;
export function markAssistance(session: StorySession, knowledgeIds: string[], assistance: Assistance, now: Date): StorySession;
export function choose(story: StoryCase, session: StorySession, choiceId: string, now: Date): { session: StorySession; learningEvents: LearningEvent[] };
export function resolveEnding(story: StoryCase, session: StorySession): StoryEnding;
```

`choose` must reject choice IDs not present in the current decision scene. `advanceNarrative` must only advance `narrative` scenes. On entering a `resolution` scene, set `endingId` from `resolveEnding`. No function mutates its input object.

Comparison behavior for ending conditions is exact:

```ts
const comparisons = {
  gte: (actual: number, expected: number) => actual >= expected,
  lte: (actual: number, expected: number) => actual <= expected,
  eq: (actual: number, expected: number) => actual === expected,
};
```

- [ ] **Step 5: Run tests**

```bash
npm test -- src/study/domain/story-engine.test.ts
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/study/domain/story-engine.ts src/study/domain/story-engine.test.ts
git commit -m "feat: add deterministic story engine"
```

---

### Task 5: Implement learning-state derivation and variant recommendation

**Files:**
- Create: `src/study/domain/learning-engine.ts`
- Create: `src/study/domain/learning-engine.test.ts`
- Create: `src/study/domain/recommendation.ts`
- Create: `src/study/domain/recommendation.test.ts`

**Interfaces:**
- Consumes: `LearningEvent[]`, knowledge nodes, story variants, case history.
- Produces: `deriveKnowledgeState(events, now)` and `rankVariants(pack, events, caseHistory, now)`.

- [ ] **Step 1: Write failing learning-state tests with fixed dates**

Assert an unaided success scores higher than a handbook-assisted success and that old evidence has lower weight than recent evidence:

```ts
const now = new Date('2026-09-14T00:00:00Z');
const state = deriveKnowledgeState([
  event('apply', 1, 'handbook', '2026-09-13T00:00:00Z'),
  event('apply', 1, 'none', '2026-09-14T00:00:00Z'),
], now);
expect(state.apply).toBeGreaterThan(0.75);
expect(state.helpDependence).toBe(0.5);
```

Also test empty history returns zeros and never produces `NaN`.

- [ ] **Step 2: Implement the transparent MVP learning model**

Use these exact factors:

```ts
const assistanceFactor: Record<Assistance, number> = {
  none: 1,
  handbook: 0.75,
  hint: 0.5,
  other: 0.6,
};

const recencyWeight = (ageDays: number) => Math.exp(-ageDays / 90);
```

For a given mode, compute:

```text
weightedScore = sum(result * assistanceFactor * recencyWeight) / sum(recencyWeight)
```

Derive:

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
encounter = min(1, total events / 3)
apply = weightedScore(apply events), or 0
 discriminate = weightedScore(discriminate events), or 0
recall = weightedScore(recall events) when recall events exist
recall fallback = apply * exp(-days since latest successful unaided apply / 45)
helpDependence = assisted event count / total event count
```

Clamp every score to `[0, 1]`.

- [ ] **Step 3: Write failing recommendation tests**

Construct two variants where one targets a weak knowledge node and one targets a strong node. Assert the weak-target variant ranks first. Assert ties are broken by `caseId` then `variantId` so recommendations are deterministic.

- [ ] **Step 4: Implement recommendation**

For each knowledge node:

```text
priority = 0.35*(1-apply) + 0.25*(1-discriminate) + 0.25*(1-recall) + 0.15*recencyGap
recencyGap = min(1, daysSinceLastSeen / 30), or 1 when never seen
```

Variant score is the arithmetic mean priority of its `targetKnowledge` nodes. Subtract `0.05` if that exact `(caseId, variantId)` was the learner's most recent completed variant; do not make the penalty cumulative.

Expose:

```ts
export interface RankedVariant {
  caseId: string;
  variantId: string;
  score: number;
}

export function rankVariants(
  pack: QualificationPack,
  events: LearningEvent[],
  caseHistory: CaseHistoryEntry[],
  now: Date,
): RankedVariant[];
```

- [ ] **Step 5: Run tests**

```bash
npm test -- src/study/domain/learning-engine.test.ts src/study/domain/recommendation.test.ts
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/study/domain/learning-engine.ts src/study/domain/learning-engine.test.ts src/study/domain/recommendation.ts src/study/domain/recommendation.test.ts
git commit -m "feat: derive mastery and recommend variants"
```

---

### Task 6: Add IndexedDB persistence with an in-memory fallback

**Files:**
- Create: `src/study/storage/repository.ts`
- Create: `src/study/storage/memory-repository.ts`
- Create: `src/study/storage/repository.test.ts`

**Interfaces:**
- Consumes: `LearningEvent`, `StorySession`.
- Produces: a common `StudyRepository` used by UI code.
- Produces: `createStudyRepository(): Promise<{ repository: StudyRepository; persistent: boolean }>`.

- [ ] **Step 1: Write failing persistence tests**

Test the following exact behavior:

```ts
await repo.appendLearningEvents([learningEvent]);
expect(await repo.listLearningEvents()).toEqual([expect.objectContaining({ knowledgeId: learningEvent.knowledgeId })]);

await repo.saveActiveSession(session);
expect(await repo.loadActiveSession(session.caseId)).toMatchObject({ variantId: session.variantId });

await repo.completeSession(session, 'controlled', completedAt);
expect(await repo.loadActiveSession(session.caseId)).toBeNull();
expect(await repo.listCaseHistory()).toHaveLength(1);
```

- [ ] **Step 2: Define storage contracts**

Add:

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

export interface StudyRepository {
  appendLearningEvents(events: LearningEvent[]): Promise<void>;
  listLearningEvents(): Promise<LearningEvent[]>;
  saveActiveSession(session: StorySession): Promise<void>;
  loadActiveSession(caseId: string): Promise<StorySession | null>;
  listActiveSessions(): Promise<StorySession[]>;
  completeSession(session: StorySession, endingId: string, completedAt: Date): Promise<void>;
  listCaseHistory(): Promise<CaseHistoryEntry[]>;
}
```

- [ ] **Step 3: Implement IndexedDB schema version 1**

Use database name `qualification-study` and these stores:

```text
learning-events  keyPath: id, autoIncrement
case-history     keyPath: id
active-sessions  keyPath: caseId
settings         keyPath: key
```

`completeSession` must write case history and delete the matching active session in one readwrite transaction.

- [ ] **Step 4: Implement memory fallback**

`MemoryStudyRepository` implements the same interface using arrays/maps. `createStudyRepository()` tries opening IndexedDB; on open failure it returns `{ repository: new MemoryStudyRepository(), persistent: false }` without throwing.

- [ ] **Step 5: Run persistence tests**

```bash
npm test -- src/study/storage/repository.test.ts
```

Expected: PASS using fake IndexedDB.

- [ ] **Step 6: Commit**

```bash
git add src/study/storage/repository.ts src/study/storage/memory-repository.ts src/study/storage/repository.test.ts
git commit -m "feat: persist study progress locally"
```

---

### Task 7: Author the 乙4 性消 knowledge catalog, provenance, and handbook

**Files:**
- Create: `src/study-content/hazardous-materials/manifest.yaml`
- Create: `src/study-content/hazardous-materials/knowledge/class4-common.yaml`
- Create: `src/study-content/hazardous-materials/knowledge/class4-substances.yaml`
- Create: `src/study-content/hazardous-materials/knowledge/fire-prevention.yaml`
- Create: `src/study-content/hazardous-materials/knowledge/extinguishing.yaml`
- Create: `src/study-content/hazardous-materials/handbook/classification.yaml`
- Create: `src/study-content/hazardous-materials/handbook/fire-response.yaml`
- Create: `docs/study-content/otsu4-seisho-coverage.md`
- Modify: `src/study/domain/validate-pack.test.ts`

**Interfaces:**
- Produces: the canonical curriculum graph for the initial qualification section.
- Produces: source IDs consumed by every factual knowledge and handbook entry.
- Consumes: Task 2 schemas and Task 3 validator.

- [ ] **Step 1: Establish authoritative source policy in the manifest**

`manifest.yaml` must define qualification ID `hazardous-materials`, section ID `otsu4-seisho`, and source entries. Use primary or official public sources for claims: the Fire and Disaster Management Agency, the Institute of Scientific Approaches for Fire & Disaster, e-Gov statutes/regulations, the Fire Safety & Disaster Preparedness Institute where applicable, and official manufacturer/government SDS documents for substance properties. Every source entry has `id`, `label`, exact `https` URL, and `checkedAt: 2026-09-14` or the actual later verification date used during implementation.

Do not cite third-party exam-prep blogs as factual provenance.

- [ ] **Step 2: Add a failing provenance validation test**

Extend validator tests so a knowledge node with `sources: []` or an unknown source ID produces structural error code `MISSING_PROVENANCE` or `UNKNOWN_SOURCE_ID` respectively. Handbook entries follow the same rule.

Run:

```bash
npm test -- src/study/domain/validate-pack.test.ts
```

Expected: FAIL until Task 3 validation is extended.

- [ ] **Step 3: Extend validation for provenance and pass the test**

Every production knowledge node and handbook entry must have at least one valid source reference. A source URL must parse as HTTPS and `checkedAt` must match `YYYY-MM-DD`.

Run the same validator test and expect PASS.

- [ ] **Step 4: Author the curriculum graph by explicit section checklist**

`docs/study-content/otsu4-seisho-coverage.md` must contain these headings and list the knowledge IDs implemented under each:

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

For every knowledge node, write one atomic `statement`, tags, relevant relations, and source IDs. Avoid embedding exam-question wording in the knowledge node; the node represents the underlying fact or rule.

- [ ] **Step 5: Author the initial handbook as a reference tool, not a second textbook**

`classification.yaml` summarizes classification and identification cues linked to knowledge IDs. `fire-response.yaml` summarizes fire-prevention and extinguishing decision cues linked to knowledge IDs. Keep each entry short enough to consult during a case.

- [ ] **Step 6: Validate the pack**

```bash
npm run validate:study
```

Expected: `0 errors`; `NO_STORY_COVERAGE` warnings are expected because story files are added in Tasks 8–10.

- [ ] **Step 7: Commit**

```bash
git add src/study-content/hazardous-materials docs/study-content/otsu4-seisho-coverage.md src/study/domain/validate-pack.test.ts src/study/domain/validate-pack.ts
git commit -m "feat: add sourced otsu4 knowledge catalog"
```

---

### Task 8: Author and engine-test 「ガソリン臭のする倉庫」

**Files:**
- Create: `src/study-content/hazardous-materials/stories/warehouse.yaml`
- Create: `src/study/domain/warehouse-story.test.ts`

**Interfaces:**
- Produces case ID: `warehouse`.
- Produces variant IDs: `gasoline-leak` and `ether-container`.
- Targets: common Class 4 behavior, vapor behavior, ignition-source control, spill/fire response.

- [ ] **Step 1: Write the engine-level acceptance test before the YAML exists**

The test loads the content pack and asserts:

```ts
const warehouse = pack.stories.find((story) => story.id === 'warehouse');
expect(warehouse?.variants.map((variant) => variant.id)).toEqual([
  'gasoline-leak',
  'ether-container',
]);
expect(warehouse?.durationMinutes).toBeGreaterThanOrEqual(10);
expect(warehouse?.durationMinutes).toBeLessThanOrEqual(15);
```

Then follow one safe path through each variant and assert it reaches a non-null ending in no fewer than 5 decision choices and no more than 8 decision choices.

- [ ] **Step 2: Run and verify failure**

```bash
npm test -- src/study/domain/warehouse-story.test.ts
```

Expected: FAIL because `warehouse.yaml` does not exist.

- [ ] **Step 3: Author the case with consequence-first feedback**

Both variants use the same broad narrative setting but change substance/evidence. Required decision themes:

```text
1. first action on noticing odor/leak evidence
2. avoid or create an ignition-source risk
3. reason about where vapor may accumulate
4. choose containment/ventilation action from provided context
5. choose an appropriate fire-response action
```

At least one branch must demonstrate a plausible adverse consequence without displaying a `wrong answer` label. Branches may rejoin after the consequence scene. Every factual learning signal references existing knowledge IDs.

- [ ] **Step 4: Add ending rules that reflect multiple dimensions**

Use at least `identification`, `ignition`, and `containment` dimensions. Include at least three endings per variant: controlled response, partial containment with a remaining hazard, and incident escalation. Exactly one ending is default.

- [ ] **Step 5: Run case and validation tests**

```bash
npm test -- src/study/domain/warehouse-story.test.ts
npm run validate:study
```

Expected: PASS and `0 errors`.

- [ ] **Step 6: Commit**

```bash
git add src/study-content/hazardous-materials/stories/warehouse.yaml src/study/domain/warehouse-story.test.ts
git commit -m "feat: add warehouse hazardous materials case"
```

---

### Task 9: Author and engine-test 「溶剤を扱う作業場」

**Files:**
- Create: `src/study-content/hazardous-materials/stories/solvent-workplace.yaml`
- Create: `src/study/domain/solvent-story.test.ts`

**Interfaces:**
- Produces case ID: `solvent-workplace`.
- Produces variant IDs: `ethanol-spill` and `toluene-spill`.
- Targets: water-solubility distinction, alcohol/non-alcohol identification cues, vapor/fire prevention, extinguishing choice.

- [ ] **Step 1: Write the failing content acceptance test**

Assert both variant IDs exist, each has 5–8 decision points along the authored safe path, and the union of learning signals contains at least one `discriminate` event for a water-solubility-related knowledge node.

- [ ] **Step 2: Run and verify failure**

```bash
npm test -- src/study/domain/solvent-story.test.ts
```

Expected: FAIL because the story does not exist.

- [ ] **Step 3: Author both variants around the same workplace incident**

The learner receives observations rather than a lecture, uses the handbook if desired, and must distinguish the response implications of the two authored substances. No choice text should include the words `正解` or `不正解`.

Required decision themes:

```text
1. identify which information is relevant
2. distinguish water-solubility behavior
3. avoid ignition-source creation
4. select spill/fire response based on properties
5. reassess after a consequence adds new information
```

- [ ] **Step 4: Validate endings and learning mappings**

Use dimensions `identification`, `ignition`, `extinguishing`. At least one outcome must show that preventing ignition can succeed even when substance identification was imperfect, so the ending is not a disguised total score.

- [ ] **Step 5: Run tests and validator**

```bash
npm test -- src/study/domain/solvent-story.test.ts
npm run validate:study
```

Expected: PASS and `0 errors`.

- [ ] **Step 6: Commit**

```bash
git add src/study-content/hazardous-materials/stories/solvent-workplace.yaml src/study/domain/solvent-story.test.ts
git commit -m "feat: add solvent workplace case"
```

---

### Task 10: Author and engine-test 「正体不明の液体」

**Files:**
- Create: `src/study-content/hazardous-materials/stories/unknown-liquid.yaml`
- Create: `src/study/domain/unknown-liquid-story.test.ts`

**Interfaces:**
- Produces case ID: `unknown-liquid`.
- Produces variant IDs: `unknown-gasoline` and `unknown-kerosene`.
- Targets: transfer from observed properties to classification and safe handling without relying on name recognition.

- [ ] **Step 1: Write the failing transfer test**

Assert neither variant reveals the substance name in the first decision scene text or choice labels, and both variants emit at least one `discriminate` and one `recall` learning signal before resolution.

- [ ] **Step 2: Run and verify failure**

```bash
npm test -- src/study/domain/unknown-liquid-story.test.ts
```

Expected: FAIL because the story does not exist.

- [ ] **Step 3: Author evidence-driven variants**

The learner should receive property clues gradually. Required decision themes:

```text
1. decide which observation or document to inspect first
2. infer risk from flash-point/classification information supplied in-world
3. reason about vapor/fire behavior
4. choose a handling response
5. choose a fire-response action
6. state the most plausible classification at the end
```

The substance identity may be revealed only in the final narrative/debrief phase.

- [ ] **Step 4: Use multiple dimensions and distinct outcomes**

Use `identification`, `ignition`, `extinguishing`, and `evidence` dimensions. At least one ending must represent a safe operational response despite incomplete identification, reinforcing that safe reasoning is not equivalent to memorizing a label.

- [ ] **Step 5: Run tests, validator, and coverage report**

```bash
npm test -- src/study/domain/unknown-liquid-story.test.ts
npm run validate:study
```

Expected: PASS and `0 errors`. Review remaining `NO_STORY_COVERAGE` warnings against `docs/study-content/otsu4-seisho-coverage.md`; they are allowed in MVP because three cases do not claim complete story coverage.

- [ ] **Step 6: Commit**

```bash
git add src/study-content/hazardous-materials/stories/unknown-liquid.yaml src/study/domain/unknown-liquid-story.test.ts
git commit -m "feat: add unknown liquid transfer case"
```

---

### Task 11: Build Case Library, variant recommendation, and resume entry points

**Files:**
- Modify: `src/study/ui/StudyApp.tsx`
- Create: `src/study/ui/CaseLibrary.tsx`
- Create: `src/study/ui/StorageWarning.tsx`
- Modify: `src/study/ui/study-app.test.tsx`
- Modify: `src/styles/study.css`

**Interfaces:**
- Consumes: `loadContentPacks`, `createStudyRepository`, `rankVariants`.
- Produces: selectable case cards, one advisory recommendation, and `resume` action for active sessions.

- [ ] **Step 1: Replace the shell test with a failing case-library flow test**

Render `StudyApp`, await content load, and assert these three case titles are visible:

```text
ガソリン臭のする倉庫
溶剤を扱う作業場
正体不明の液体
```

Assert all three have enabled start buttons, proving recommendation does not lock other cases.

- [ ] **Step 2: Implement repository/content bootstrap in `StudyApp`**

On mount:

```text
load validated content packs
create repository
load learning events
load case history
load active sessions
compute ranked variants
```

Store a small discriminated UI state:

```ts
type ScreenState =
  | { screen: 'library' }
  | { screen: 'story'; caseId: string; session: StorySession }
  | { screen: 'debrief'; caseId: string; historyId: string }
  | { screen: 'knowledge' };
```

- [ ] **Step 3: Implement `CaseLibrary`**

Each card shows title, approximate duration, a short premise taken from story metadata added to the schema as `summary: string`, completion count, and recommendation badge when its highest-ranked variant is first overall. Add `summary` to Task 2 story schema/type and all three YAML stories in this same commit.

For an active session, show `続きから` rather than creating a new session.

- [ ] **Step 4: Implement storage fallback warning**

When repository bootstrap returns `persistent: false`, show:

```text
このブラウザでは学習履歴を保存できません。現在のセッションはこのページを閉じると失われます。
```

Do not prevent play.

- [ ] **Step 5: Add responsive layout rules**

Use the site's existing typography/colors via inherited CSS. Add only study-specific card/grid/button states in `study.css`. Mobile layout must remain usable at 360px viewport width with one-column cards and buttons at least 44px high.

- [ ] **Step 6: Run UI tests**

```bash
npm test -- src/study/ui/study-app.test.tsx
```

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add src/study/ui/StudyApp.tsx src/study/ui/CaseLibrary.tsx src/study/ui/StorageWarning.tsx src/study/ui/study-app.test.tsx src/styles/study.css src/study/domain/content-types.ts src/study/domain/content-schema.ts src/study-content/hazardous-materials/stories
git commit -m "feat: add study case library"
```

---

### Task 12: Build Story Player, handbook assistance, and autosave

**Files:**
- Create: `src/study/ui/StoryPlayer.tsx`
- Create: `src/study/ui/HandbookDrawer.tsx`
- Modify: `src/study/ui/StudyApp.tsx`
- Modify: `src/study/ui/study-app.test.tsx`
- Modify: `src/styles/study.css`

**Interfaces:**
- Consumes: Story Engine, handbook entries, `StudyRepository`.
- Produces: consequence-first interactive play and resumable progress.

- [ ] **Step 1: Write the failing interactive-flow test**

Open `warehouse`, choose a decision, and assert the next narrative/consequence text appears while neither `正解` nor `不正解` appears anywhere. Open the handbook, click one entry, then choose a decision mapped to that entry's knowledge node and verify the persisted learning event has `assistance: 'handbook'`.

- [ ] **Step 2: Implement scene rendering by discriminated scene type**

`StoryPlayer` behavior:

```text
narrative -> text + one 続ける button
 decision -> text + choice buttons
resolution -> ending text + ケースを振り返る button
```

Do not show internal dimensions, learning event scores, or correct/incorrect labels during play.

- [ ] **Step 3: Implement handbook drawer**

`HandbookDrawer` lists handbook entries for the active qualification. Opening an entry calls `markAssistance` for its `knowledgeIds` and persists the updated active session immediately. Merely opening the drawer without an entry does not count as assistance.

- [ ] **Step 4: Persist every meaningful transition**

After `advanceNarrative`, `choose`, or `markAssistance`:

```text
save updated active session
append emitted learning events, if any
```

When a resolution ending is reached, do not call `completeSession` until the learner selects `ケースを振り返る`; this guarantees the ending remains resumable after a tab close.

- [ ] **Step 5: Run UI and engine tests**

```bash
npm test -- src/study/ui/study-app.test.tsx src/study/domain/story-engine.test.ts
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/study/ui/StoryPlayer.tsx src/study/ui/HandbookDrawer.tsx src/study/ui/StudyApp.tsx src/study/ui/study-app.test.tsx src/styles/study.css
git commit -m "feat: add branching story player"
```

---

### Task 13: Build Debrief and simple/detailed Knowledge View

**Files:**
- Create: `src/study/ui/Debrief.tsx`
- Create: `src/study/ui/KnowledgeView.tsx`
- Modify: `src/study/ui/StudyApp.tsx`
- Modify: `src/study/ui/study-app.test.tsx`
- Modify: `src/styles/study.css`

**Interfaces:**
- Consumes: completed `StorySession`, learning events, `deriveKnowledgeState`, knowledge nodes, handbook entries.
- Produces: narrative consequence review and inspectable learning-state views.

- [ ] **Step 1: Write failing debrief test**

Complete a short case in the UI test, click `ケースを振り返る`, and assert the debrief contains:

```text
あなたの判断
起きたこと
関係する知識
試験ではどう問われるか
```

Also assert at least one relevant knowledge-node title is shown.

- [ ] **Step 2: Implement session completion handoff**

When entering Debrief:

```text
repository.completeSession(session, endingId, now)
reload case history
recompute recommendations
```

The debrief derives its decision list from `choiceHistory` and story data rather than storing duplicate prose in history.

- [ ] **Step 3: Implement `Debrief` without turning it into a score page**

For each major decision, show choice text, resulting consequence scene/ending context, linked knowledge statements, and handbook links. Add an `examConnection` optional string field to `KnowledgeNode` schema/type and author concise exam-style connection notes only where useful; this is explanatory prose, not a full bank of quiz questions.

- [ ] **Step 4: Implement simple Knowledge View**

Default view groups nodes by curriculum section and converts derived state to these text bands:

```text
apply >= 0.8 and recall >= 0.7 -> 安定して使えている
apply >= 0.55 -> 使える場面が増えている
encounter > 0 -> もう一度別の状況で使いたい
encounter == 0 -> まだケースで扱っていない
```

Add one sentence when `helpDependence >= 0.5`: `資料を参照しながら使った経験が多い。`

- [ ] **Step 5: Implement detailed Knowledge View**

A toggle labelled `詳細を見る` exposes numeric `encounter`, `apply`, `discriminate`, `recall`, `helpDependence`, `eventCount`, and `lastSeenAt`. Use accessible HTML progress bars/tables; do not add a charting library for MVP.

- [ ] **Step 6: Run UI tests**

```bash
npm test -- src/study/ui/study-app.test.tsx
```

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add src/study/ui/Debrief.tsx src/study/ui/KnowledgeView.tsx src/study/ui/StudyApp.tsx src/study/ui/study-app.test.tsx src/styles/study.css src/study/domain/content-types.ts src/study/domain/content-schema.ts src/study-content/hazardous-materials/knowledge
git commit -m "feat: add debrief and knowledge views"
```

---

### Task 14: Integrate navigation, end-to-end checks, and deployment gate

**Files:**
- Modify: `src/components/SiteHeader.astro`
- Modify: `src/study/ui/study-app.test.tsx`
- Modify: `package.json`
- Modify: `README.md`

**Interfaces:**
- Consumes all preceding tasks.
- Produces a discoverable `/study/` application that cannot deploy with broken content or failing tests.

- [ ] **Step 1: Add Study to the site header**

Insert before `About`:

```astro
<a href="/study/" aria-current={path.startsWith('/study') ? 'page' : undefined}>Study</a>
```

- [ ] **Step 2: Add one complete UI integration test**

The test must:

```text
render app
open warehouse case
make at least five decisions
open one handbook entry
reach an ending
open debrief
return to case library
verify completion count increased
open Knowledge View
verify one detailed mastery row can be displayed
```

Use deterministic variant selection by injecting a fixed `now` and a repository seeded with no history; `warehouse/gasoline-leak` should be marked `recommendedFirst: true` in content and win the initial tie.

- [ ] **Step 3: Add a single CI-quality check script**

Add to `package.json`:

```json
{
  "check:study": "npm run validate:study && vitest run && astro check"
}
```

Install `@astrojs/check` and `typescript` as dev dependencies if not already present:

```bash
npm install -D @astrojs/check typescript
```

Do not add a second GitHub Actions workflow. The existing Pages workflow remains the deployment mechanism; `prebuild` already runs the content validator.

- [ ] **Step 4: Document local development and content commands**

Add a `Study app` section to `README.md` with exactly these commands and purposes:

```bash
npm run dev
npm test
npm run validate:study
npm run check:study
npm run build
```

Document that learning history is browser-local IndexedDB and that deleting site data resets it.

- [ ] **Step 5: Run the full verification suite**

Run:

```bash
npm run validate:study
npm test
npx astro check
npm run build
```

Expected:

```text
validator: 0 structural errors
Vitest: all tests pass
Astro check: 0 errors
Astro build: exits 0 and emits dist/study/index.html
```

Coverage warnings are allowed only when they correspond to nodes listed as not yet story-covered in `docs/study-content/otsu4-seisho-coverage.md`.

- [ ] **Step 6: Manually smoke-test the production build**

Run:

```bash
npm run preview
```

Verify in a browser:

```text
/study/ loads directly
all three cases can be started in any order
refresh during a case resumes it
handbook remains usable on mobile width
ending does not stop before the final debrief action
learning state changes after completion
existing /notes/, /topics/, /now/, and /about/ still render
```

- [ ] **Step 7: Commit**

```bash
git add src/components/SiteHeader.astro src/study/ui/study-app.test.tsx package.json package-lock.json README.md
git commit -m "feat: integrate study platform into site"
```

---

## Final Verification Gate

Before declaring the MVP complete, run all of the following from a clean checkout with dependencies installed:

```bash
npm run validate:study
npm test
npx astro check
npm run build
```

Then verify the implementation against the design spec section by section:

```text
Product principles: consequence-first, no early game over, cases unordered
Architecture: Astro + React + YAML + IndexedDB + validator
Knowledge model: provenance + relations + coverage report
Learning state: event log is canonical, E/A/D/R/H derived
Handbook: use is recorded but not blocked or scored as failure
Recommendation: weak concepts select new authored variants
MVP content: 3 cases, >=2 variants each
Debrief: decisions -> consequences -> knowledge -> exam connection
Storage: resume, history, memory fallback
Extensibility: qualification-specific data does not enter Story Engine
```

If any item is not demonstrably satisfied by code/tests/content, fix it before opening or merging the implementation PR.
