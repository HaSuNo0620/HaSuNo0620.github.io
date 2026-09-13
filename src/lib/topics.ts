const LOW_SIGNAL_TOPICS = new Set([
  'statistical mechanics',
  'correlation',
  'memory',
  'wave number',
  'linear response',
  'external field',
  'data analysis',
  'pricing',
  'reciprocal space',
  'long-range order',
  'spin chain',
  'bessel function',
  'compact field',
  'information thermodynamics',
  'inhomogeneous systems',
  'golden ratio',
  'stress tensor',
  'surface excess',
  'gauge redundancy',
  'capillarity',
  'fourier analysis',
  'dynamical systems',
  'jordan-wigner',
  'bethe ansatz',
  'logit model',
  'complex analysis',
  'mathematical physics',
]);

const MAX_TOPICS_PER_NOTE = 4;

export const curateTopics = (topics: string[]) => {
  const unique = [...new Set(topics.map((topic) => topic.trim()).filter(Boolean))];
  const curated = unique.filter((topic) => !LOW_SIGNAL_TOPICS.has(topic.toLowerCase()));

  // Keep the metadata usable even for an older note whose tags were all too broad.
  const source = curated.length > 0 ? curated : unique;
  return source.slice(0, MAX_TOPICS_PER_NOTE);
};

export const topicSlug = (topic: string) => topic
  .normalize('NFKC')
  .toLowerCase()
  .trim()
  .replace(/[^\p{L}\p{N}]+/gu, '-')
  .replace(/(^-|-$)/g, '');
