import { describe, expect, it } from 'vitest';
import type { StoryCase } from './content-types';
import { advanceNarrative, choose, markAssistance, startStorySession } from './story-engine';

const story: StoryCase = {
  id: 'warehouse', qualificationId: 'hazardous-materials', section: 'otsu4-seisho', title: '倉庫', summary: 'summary', durationMinutes: 10,
  dimensions: ['ignition'], recommendedFirst: true,
  variants: [{
    id: 'gasoline-leak', startScene: 'arrival', targetKnowledge: ['class4.gasoline.vapor'],
    scenes: {
      arrival: { kind: 'narrative', text: 'arrive', next: 'decision' },
      decision: {
        kind: 'decision', text: 'what now?', choices: [
          { id: 'stop-ignition', text: 'avoid spark', next: 'resolution', effects: { ignition: 1 }, learning: [{ knowledgeId: 'class4.gasoline.vapor', mode: 'apply', result: 1 }] },
          { id: 'switch-light', text: 'turn on light', next: 'resolution', effects: { ignition: -1 }, learning: [{ knowledgeId: 'class4.gasoline.vapor', mode: 'apply', result: 0 }] },
        ],
      },
      resolution: { kind: 'resolution', text: 'resolved' },
    },
    endings: [
      { id: 'controlled', text: 'safe', when: [{ dimension: 'ignition', operator: 'gte', value: 1 }], default: false },
      { id: 'incident', text: 'incident', when: [], default: true },
    ],
  }],
};

const now = new Date('2026-09-14T00:00:00Z');

describe('story engine', () => {
  it('starts and advances narrative immutably', () => {
    const started = startStorySession(story, 'gasoline-leak', now);
    expect(started.sceneId).toBe('arrival');
    const advanced = advanceNarrative(story, started, new Date('2026-09-14T00:01:00Z'));
    expect(advanced.sceneId).toBe('decision');
    expect(started.sceneId).toBe('arrival');
  });

  it('applies choice effects and emits learning events', () => {
    const started = advanceNarrative(story, startStorySession(story, 'gasoline-leak', now), now);
    const outcome = choose(story, started, 'stop-ignition', now);
    expect(outcome.session.dimensions.ignition).toBe(1);
    expect(outcome.session.endingId).toBe('controlled');
    expect(outcome.learningEvents[0]).toMatchObject({ knowledgeId: 'class4.gasoline.vapor', mode: 'apply', result: 1, assistance: 'none' });
  });

  it('records assistance on subsequent learning events', () => {
    let session = advanceNarrative(story, startStorySession(story, 'gasoline-leak', now), now);
    session = markAssistance(session, ['class4.gasoline.vapor'], 'handbook', now);
    const outcome = choose(story, session, 'stop-ignition', now);
    expect(outcome.learningEvents[0].assistance).toBe('handbook');
  });

  it('rejects a choice that is not present', () => {
    const session = advanceNarrative(story, startStorySession(story, 'gasoline-leak', now), now);
    expect(() => choose(story, session, 'missing', now)).toThrow(/Unknown choice/);
  });
});
