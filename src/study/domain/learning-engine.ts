import type { Assistance, LearningMode } from './content-types';
import type { LearningEvent } from './story-engine';

export interface KnowledgeState {
  encounter: number;
  apply: number;
  discriminate: number;
  recall: number;
  helpDependence: number;
  eventCount: number;
  lastSeenAt: string | null;
}

const assistanceFactor: Record<Assistance, number> = {
  none: 1,
  handbook: 0.75,
  hint: 0.5,
  other: 0.6,
};

const clamp01 = (value: number) => Math.max(0, Math.min(1, Number.isFinite(value) ? value : 0));
const daysBetween = (a: Date, b: Date) => Math.max(0, (a.getTime() - b.getTime()) / 86_400_000);
const recencyWeight = (ageDays: number) => Math.exp(-ageDays / 90);

function weightedScore(events: LearningEvent[], mode: LearningMode, now: Date): number {
  const selected = events.filter((event) => event.mode === mode);
  if (selected.length === 0) return 0;
  let numerator = 0;
  let denominator = 0;
  for (const event of selected) {
    const weight = recencyWeight(daysBetween(now, new Date(event.timestamp)));
    numerator += clamp01(event.result) * assistanceFactor[event.assistance] * weight;
    denominator += weight;
  }
  return clamp01(denominator === 0 ? 0 : numerator / denominator);
}

export function deriveKnowledgeState(events: LearningEvent[], now: Date): KnowledgeState {
  const sorted = [...events].sort((a, b) => Date.parse(a.timestamp) - Date.parse(b.timestamp));
  const eventCount = sorted.length;
  const apply = weightedScore(sorted, 'apply', now);
  const discriminate = weightedScore(sorted, 'discriminate', now);
  const explicitRecall = sorted.some((event) => event.mode === 'recall');
  let recall = explicitRecall ? weightedScore(sorted, 'recall', now) : 0;

  if (!explicitRecall) {
    const latestUnaidedSuccess = [...sorted]
      .reverse()
      .find((event) => event.mode === 'apply' && event.assistance === 'none' && event.result > 0);
    if (latestUnaidedSuccess) {
      const ageDays = daysBetween(now, new Date(latestUnaidedSuccess.timestamp));
      recall = clamp01(apply * Math.exp(-ageDays / 45));
    }
  }

  return {
    encounter: clamp01(eventCount / 3),
    apply,
    discriminate,
    recall,
    helpDependence: eventCount === 0 ? 0 : sorted.filter((event) => event.assistance !== 'none').length / eventCount,
    eventCount,
    lastSeenAt: eventCount === 0 ? null : sorted[eventCount - 1].timestamp,
  };
}
