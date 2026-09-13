import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { curateTopics } from './lib/topics';

const notes = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/data/notes' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    area: z.enum(['Physics', 'Mathematics', 'Computing', 'Economics', 'Culture & Media']),
    topics: z.array(z.string()).default([]).transform(curateTopics),
    status: z.enum(['seed', 'growing', 'evergreen']).default('growing'),
    draft: z.boolean().default(false),
  }),
});

export const collections = { notes };
