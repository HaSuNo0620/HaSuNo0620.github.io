# Qualification Study Platform — Design Specification

Date: 2026-09-14

## 1. Purpose

Build a reusable qualification-study platform inside the existing Astro-based GitHub Pages site. The platform should avoid the typical one-question-one-answer experience and instead teach through short, replayable, branching story cases in which the learner makes decisions, observes consequences, and only later receives a structured debrief.

The platform is intentionally generic enough to support multiple qualifications. The first content pack is the Japanese Hazardous Materials Handler exam, beginning with Class B Group 4 (乙4), specifically the subject area covering properties of hazardous materials, fire prevention, and extinguishing methods.

The first release is not intended to maximize feature count. Its purpose is to test whether the story-based learning experience is genuinely more engaging and conceptually useful than conventional quiz applications.

## 2. Product Principles

1. The primary learning unit is a **case**, not a question.
2. The learner is the protagonist. There is no fixed player-character identity.
3. Cases belong to a shared world and recurring cast, but they are standalone and may be played in any order.
4. Wrong decisions do not produce immediate game-over states. The case continues, and the sequence of decisions changes the ending.
5. During the case, the application normally shows consequences rather than explicit `Correct` / `Incorrect` labels.
6. Detailed explanation is concentrated in the end-of-case debrief so that the story flow remains intact.
7. Replays use authored variants rather than free-form generated content.
8. Coverage of the official exam scope is guaranteed by an explicit knowledge model, not inferred from the story text.
9. Learning history is local to the browser. The initial version has no accounts, server-side database, or cross-device synchronization.
10. The application engine, qualification knowledge, and story content are independent modules.

## 3. Host Architecture

The existing site remains an Astro static site deployed through GitHub Pages. A React-based study application is mounted under `/study/` as an Astro island/application surface.

```text
Astro site
├── existing articles and notes
└── /study/
    └── React study application
        ├── qualification selection
        ├── case library
        ├── story player
        ├── debrief
        ├── handbook
        └── learning-state views
```

The application remains fully static at deployment time. Runtime persistence is handled by IndexedDB in the user's browser.

## 4. Core Domain Separation

The system is divided into five logical layers:

```text
Content
  ↓
Story Engine
  ↓
Learning Engine
  ↓
Storage
  ↓
UI
```

### 4.1 Content Layer

Contains only authored qualification data:

- qualification metadata,
- knowledge nodes and relations,
- story cases,
- case variants,
- handbook/reference material.

The content layer must not contain React-specific behavior.

### 4.2 Story Engine

Responsible for deterministic case progression.

Inputs include current scene, active variant, accumulated case state, and previous choices. Outputs include next scene, story-state effects, learning events, and an ending state when applicable.

The Story Engine does not know what gasoline, flash point, or any qualification-specific concept means. It only processes validated content definitions.

### 4.3 Learning Engine

Consumes learning events emitted by the Story Engine and derives the learner's current knowledge state. It is deliberately separate from Story Engine logic so that learning-model changes do not require rewriting cases.

### 4.4 Storage Layer

IndexedDB stores event history, case history, active sessions, and settings. The browser is the initial user identity boundary. No account system is required.

### 4.5 UI Layer

React renders the case library, story player, debrief, handbook, and learning-state views. Business logic remains outside presentation components wherever practical.

## 5. Story Model

A case is defined as

\[
\mathrm{Case}=\mathrm{StorySkeleton}+\mathrm{Variant}+\mathrm{KnowledgeMapping}.
\]

The basic player flow is:

```text
Situation
  ↓
Decision
  ↓
Consequence
  ↓
Updated situation
  ↓
Decision
  ↓
...
  ↓
Ending
  ↓
Debrief
```

A case is expected to last approximately 10–15 minutes and contain roughly 5–8 meaningful decision points in its first implementation.

### 5.1 Semi-branching Structure

Cases are not fully divergent interactive fiction. Important choices may branch into distinct consequence scenes, after which branches may rejoin the main case structure. This gives the learner meaningful causal feedback without multiplying authoring cost exponentially.

### 5.2 No Early Failure Termination

Poor decisions do not terminate the case. Instead, the engine accumulates dimensions of case performance such as

\[
\mathbf{S}=(S_{identification},S_{ignition},S_{containment},S_{extinguishing}).
\]

The exact dimensions are content-defined rather than hard-coded globally. The ending is selected from accumulated state and decision history.

### 5.3 Replay Variants

Cases contain multiple authored variants. The same narrative skeleton may change the hazardous substance, available observations, hidden/explicit labels, distractor information, decision difficulty, and target knowledge nodes.

Variants are selected according to learning needs, but every variant is authored and validated in advance. The runtime does not generate safety-critical instructional content using an LLM.

## 6. Knowledge Model

Exam coverage is represented as a qualification-specific knowledge graph:

\[
K=\{k_1,k_2,\ldots,k_N\}.
\]

Each node should be small enough to correspond to a usable fact, distinction, principle, or decision rule. Examples for 乙4 include:

- gasoline belongs to Class I petroleum,
- gasoline has a low flash point,
- gasoline vapor is heavier than air,
- gasoline is poorly soluble in water,
- direct water jet extinguishing is unsuitable in relevant conditions.

Knowledge relations may include `prerequisite`, `contrasts_with`, `example_of`, `derived_from`, and `used_with`.

The knowledge graph is the canonical representation of curriculum coverage. Story text and handbook pages reference the graph; they do not independently define the curriculum.

## 7. Learning State

For conceptual display, a knowledge node may be summarized as

\[
K_i=(E_i,A_i,D_i,R_i,H_i),
\]

where:

- \(E_i\): encounter experience,
- \(A_i\): ability to apply the concept in a decision,
- \(D_i\): ability to discriminate it from similar concepts,
- \(R_i\): ability to reuse it after time has passed,
- \(H_i\): dependence on handbook/hints.

These values are derived rather than treated as the primary stored truth.

### 7.1 Event Log as Source of Truth

The persisted canonical record is an event history:

```text
knowledgeId
mode              encounter | apply | discriminate | recall
result
assistance        none | handbook | hint | other supported value
context
caseId
variantId
timestamp
```

The current knowledge state is computed as

\[
K_i=f(\mathcal H_i,t),
\]

where \(\mathcal H_i\) is the event history for node \(i\). This makes future changes to the learning model possible without discarding old learning history.

### 7.2 Learner-Facing Views

Two views are required:

1. **Simple view** — natural-language summary of strengths and areas worth revisiting.
2. **Detailed view** — numerical/graphical inspection of learning dimensions, replay history, assistance use, and recency.

The normal experience should not reduce learning to a single score percentage.

## 8. Handbook and Assistance

During a story, the learner may open a qualification-specific handbook. Handbook use is not treated as failure. Instead, the assistance event is recorded and can influence derived learning state.

The intended progression is from free reference use during early encounters toward more unaided recall in later variants. The application does not artificially prevent reference use unless a future content pack explicitly defines a closed-book mode.

## 9. Recommendation Model

The first version uses a transparent heuristic rather than machine learning. Conceptually, node priority may use terms such as

\[
P_i=w_A(1-A_i)+w_D(1-D_i)+w_R(1-R_i)+w_TF(\Delta t_i).
\]

Case/variant recommendation favors authored variants covering high-priority nodes.

The design principle is: do not repeat a failed question merely because it was failed; prefer a new authored situation that requires the same weak concept to be used again.

All weighting constants are internal implementation details and may evolve after observing actual use.

## 10. Content-Pack Format

Content is authored outside application code, initially in YAML.

```text
src/study-content/
└── hazardous-materials/
    ├── manifest.yaml
    ├── knowledge/
    │   ├── class4-common.yaml
    │   ├── gasoline.yaml
    │   ├── alcohols.yaml
    │   └── ...
    ├── stories/
    │   ├── warehouse.yaml
    │   ├── solvent-workplace.yaml
    │   └── unknown-liquid.yaml
    └── handbook/
        ├── classification.yaml
        ├── extinguishing.yaml
        └── ...
```

The format must support qualification packs beyond hazardous materials without requiring Story Engine changes. Each decision must be able to map to one or more knowledge nodes with a learning mode such as `apply` or `discriminate`.

## 11. Content Provenance and Correctness

Qualification content must carry provenance independently of story prose. Each factual knowledge node must support source metadata containing at minimum:

```text
source title / organization
source URL or bibliographic identifier
source type
verified date
optional note identifying the relevant section/table
```

For regulated or safety-relevant material, official or primary sources are preferred whenever available. Story text must derive factual claims from the canonical knowledge/handbook data rather than duplicating untracked facts in multiple locations.

The validator must require source metadata for factual nodes in the hazardous-materials pack. This makes later review possible when regulations, official terminology, or exam scope change.

## 12. Build-Time Validation

Because instructional correctness and structural integrity are more important than permissive authoring, content validation is mandatory during development/build.

The validator must detect at minimum:

- unknown knowledge IDs,
- unknown scene targets,
- unreachable scenes,
- missing endings,
- unintended non-terminating cycles,
- malformed variants,
- references to missing handbook entries,
- required factual nodes without provenance,
- knowledge nodes with no story coverage,
- knowledge nodes with encounter-only coverage and no apply/discriminate use where such use is required.

Validation should also produce machine-readable coverage reports for encounter, apply, discriminate, and per-case knowledge coverage.

A build must fail for structural errors or missing required provenance. Coverage gaps may remain warnings during the MVP because the full knowledge map intentionally precedes complete story coverage.

## 13. Storage Model

Initial IndexedDB stores:

```text
study-db
├── learning-events
├── case-history
├── active-sessions
└── settings
```

`active-sessions` enables resuming a partially completed case after tab/browser closure.

No cross-device synchronization is included in the MVP. Stable IDs and versioned schemas are required so that JSON export/import or later cloud sync can be added without redesigning content IDs.

## 14. Initial Navigation and Screens

```text
/study/
  ↓
Qualification selection
  ↓
Hazardous Materials Handler
  ↓
Case Library
  ↓
Story Player
  ↓
Debrief
```

The Handbook and Knowledge View remain reachable as secondary views.

### 14.1 Case Library

Cases are displayed as scenarios rather than numbered chapters, for example:

- ガソリン臭のする倉庫
- 溶剤を扱う作業場
- 正体不明の液体

Cases are never sequence-locked. The application may mark one as recommended or suitable as a first case, but the learner may enter any available case.

## 15. Debrief

The debrief bridges narrative experience and exam preparation. It shows:

1. major decisions made,
2. consequences produced by those decisions,
3. the knowledge principles behind those consequences,
4. concepts used successfully or weakly,
5. relevant handbook links,
6. how the same concept may appear in actual exam-style questioning.

Exam-style questions are a confirmation layer, not the primary learning interface.

## 16. MVP Scope

The MVP validates the learning format before attempting complete qualification coverage in story count.

### Included

- `/study/` React application inside the existing Astro site,
- generic Story Engine,
- generic Learning Engine,
- IndexedDB persistence,
- YAML content-pack loader,
- build-time validator,
- 乙4 knowledge map for the `properties / fire prevention / extinguishing` subject area,
- provenance metadata for the 乙4 factual knowledge nodes,
- handbook content needed by the initial cases,
- three complete story cases,
- **a minimum of two authored variants for each of the three initial cases**,
- debrief screen,
- simple and detailed learning-state views,
- recommendation of a useful next case/variant.

Initial cases:

1. **ガソリン臭のする倉庫** — Class 4 common properties, gasoline, vapor behavior, ignition sources.
2. **溶剤を扱う作業場** — water-solubility distinctions, alcohol-related behavior, extinguishing choices.
3. **正体不明の液体** — infer properties and handling from evidence rather than relying on substance-name recall.

### Explicitly excluded from MVP

- user accounts,
- server-side database,
- cross-device synchronization,
- social features,
- leaderboards,
- coins/XP/login rewards,
- authoring GUI,
- runtime LLM-generated cases,
- complete story coverage for 乙4 law and physics/chemistry,
- all 乙1–6 / 甲種 / 丙種 content,
- Basic Information Technology Engineer content.

These exclusions preserve focus on validating the story-learning mechanism.

## 17. Testing Strategy

### 17.1 Story Engine Unit Tests

Given a session state and choice, tests verify the expected next scene, state effects, emitted learning events, and ending selection.

### 17.2 Learning Engine Unit Tests

Tests verify that equivalent event histories derive stable expected learning-state outputs, including assistance and time-dependent behavior.

### 17.3 Content Validation Tests

Every content pack is validated structurally, for provenance requirements, and for curriculum coverage.

### 17.4 Persistence Tests

Test creation, update, migration, interrupted-session resume, and corrupt/unknown-version fallback behavior.

### 17.5 UI Integration Tests

At minimum, cover opening a case, making a decision, branching and rejoining, opening the handbook, finishing a case, viewing the debrief, replaying with another variant, and resuming an interrupted case.

## 18. Error Handling

Content validation should prevent most runtime structural failures. Runtime behavior should nevertheless fail safely:

- invalid/missing case content: show an actionable content error rather than silently skipping,
- IndexedDB unavailable: permit an in-memory session with a clear warning that progress will not persist,
- incompatible stored schema with no supported migration: leave the existing database untouched, disable writes for that database, and show a clear compatibility error; never reset or delete learner history automatically,
- interrupted story: restore the latest valid persisted scene and state.

No learner history should be silently discarded.

## 19. Extensibility

Future qualification packs should be able to add directories such as:

```text
hazardous-materials/
fundamental-information-technology-engineer/
statistics/
bookkeeping/
```

without changing the Story Engine or Learning Engine for ordinary use.

The qualification manifest may define pack-specific terminology, handbook categories, case-state dimensions, and curriculum metadata while relying on the same runtime interfaces.

## 20. MVP Success Criteria

The MVP is considered successful only if the story-learning mechanism works as a learning experience, not merely if the software runs.

1. A learner completing the three cases experiences a meaningful causal chain rather than a sequence of disguised multiple-choice questions.
2. A poor decision is understood through its consequence before formal explanation is shown.
3. The debrief makes clear why the relevant hazardous-material property mattered.
4. Replay with another variant requires transfer of knowledge rather than memorization of the previous answer.
5. The knowledge map and validation tooling can demonstrate exactly which curriculum nodes are and are not covered.
6. Factual hazardous-material content is traceable to stored provenance metadata.
7. The architecture supports adding another qualification pack without redesigning the core engines.

Only after these criteria are met should the project expand toward complete 乙4 story coverage and then additional qualifications.
