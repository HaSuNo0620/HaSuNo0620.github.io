import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const notes = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/data/notes' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    area: z.enum(['Physics', 'Mathematics', 'Computing', 'Culture & Media']),
    topics: z.array(z.string()).default([]),
    status: z.enum(['seed', 'growing', 'evergreen']).default('growing'),
    draft: z.boolean().default(false),
  }),
});

export const collections = { notes };
