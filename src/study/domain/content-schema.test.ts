import { describe, expect, it } from 'vitest';
import { parseStoryFile } from './content-schema';

describe('parseStoryFile', () => {
  it('parses a decision and ending rules', () => {
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
    expect(story.recommendedFirst).toBe(false);
  });

  it('rejects a choice without a next scene', () => {
    expect(() => parseStoryFile(`
id: broken
qualificationId: hazardous-materials
section: otsu4-seisho
title: 壊れたケース
summary: 壊れたデータ。
durationMinutes: 10
dimensions: [ignition]
variants:
  - id: broken-v1
    startScene: arrival
    scenes:
      arrival:
        kind: decision
        text: 状況
        choices:
          - id: bad
            text: 選ぶ
    endings:
      - id: end
        default: true
        text: 終了
`)).toThrow();
  });
});
