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
    system: z.object({
      dimension: z.number().int().positive(),
      spatial: z.enum(['uniform', 'periodic', 'quasiperiodic', 'random']),
      range: z.union([
        z.enum(['R1', 'R2', 'Rn']),
        z.array(z.enum(['R1', 'R2', 'Rn'])).min(1),
      ]),
      interaction: z.string(),
      symmetry: z.array(z.string()).min(1),
      mechanics: z.enum(['classical', 'quantum']),
      role: z.enum(['model', 'comparison']).default('model'),
    }).optional(),
  }),
});

export const collections = { notes };
