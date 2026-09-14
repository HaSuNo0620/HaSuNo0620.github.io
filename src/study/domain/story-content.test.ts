import { describe, expect, it } from 'vitest';
import { loadContentPacks } from '../content/load-content';
import type { StoryCase, StoryVariant } from './content-types';

function firstChoiceDecisionCount(story: StoryCase, variant: StoryVariant): number {
  let sceneId = variant.startScene;
  let decisions = 0;
  const guard = new Set<string>();
  while (true) {
    if (guard.has(sceneId)) throw new Error(`cycle at ${sceneId}`);
    guard.add(sceneId);
    const scene = variant.scenes[sceneId];
    if (!scene) throw new Error(`missing scene ${sceneId}`);
    if (scene.kind === 'resolution') return decisions;
    if (scene.kind === 'narrative') sceneId = scene.next;
    else {
      decisions += 1;
      sceneId = scene.choices[0].next;
    }
  }
}

describe('initial otsu4 stories', () => {
  const pack = loadContentPacks().find((item) => item.manifest.id === 'hazardous-materials')!;
  const stories = new Map(pack.stories.map((story) => [story.id, story]));

  it('includes the three planned cases and exact initial variants', () => {
    expect([...stories.keys()].sort()).toEqual(['solvent-workplace', 'unknown-liquid', 'warehouse']);
    expect(stories.get('warehouse')!.variants.map((v) => v.id)).toEqual(['gasoline-leak', 'ether-container']);
    expect(stories.get('solvent-workplace')!.variants.map((v) => v.id)).toEqual(['ethanol-spill', 'toluene-spill']);
    expect(stories.get('unknown-liquid')!.variants.map((v) => v.id)).toEqual(['unknown-gasoline', 'unknown-kerosene']);
  });

  it('keeps each case 10-15 minutes and safe first-choice paths 5-8 decisions', () => {
    for (const story of pack.stories) {
      expect(story.durationMinutes).toBeGreaterThanOrEqual(10);
      expect(story.durationMinutes).toBeLessThanOrEqual(15);
      for (const variant of story.variants) {
        const count = firstChoiceDecisionCount(story, variant);
        expect(count).toBeGreaterThanOrEqual(5);
        expect(count).toBeLessThanOrEqual(8);
      }
    }
  });

  it('does not reveal the hidden substance in the first unknown-liquid decision', () => {
    const story = stories.get('unknown-liquid')!;
    for (const variant of story.variants) {
      const first = variant.scenes[variant.startScene];
      expect(first.kind).toBe('decision');
      if (first.kind !== 'decision') continue;
      const text = [first.text, ...first.choices.map((choice) => choice.text)].join(' ');
      expect(text).not.toMatch(/ガソリン|灯油/);
    }
  });

  it('uses apply, discriminate, and recall learning signals without quiz labels', () => {
    const modes = new Set<string>();
    for (const story of pack.stories) for (const variant of story.variants) for (const scene of Object.values(variant.scenes)) {
      const text = scene.kind === 'decision' ? `${scene.text} ${scene.choices.map((choice) => choice.text).join(' ')}` : scene.text;
      expect(text).not.toMatch(/正解|不正解/);
      if (scene.kind === 'decision') for (const choice of scene.choices) for (const signal of choice.learning) modes.add(signal.mode);
    }
    expect(modes).toEqual(new Set(['apply', 'discriminate', 'recall']));
  });
});
