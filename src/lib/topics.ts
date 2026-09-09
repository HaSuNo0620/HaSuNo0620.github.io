export const topicSlug = (topic: string) => topic
  .normalize('NFKC')
  .toLowerCase()
  .trim()
  .replace(/[^\p{L}\p{N}]+/gu, '-')
  .replace(/(^-|-$)/g, '');
