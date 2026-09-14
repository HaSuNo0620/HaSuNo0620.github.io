import { fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { openDB } from 'idb';
import { describe, expect, it } from 'vitest';
import { loadContentPacks } from '../content/load-content';
import { startStorySession, choose } from '../domain/story-engine';
import Debrief from './Debrief';
import StudyApp from './StudyApp';

describe('StudyApp', () => {
  it('navigates into consequence-first play and records handbook assistance', async () => {
    render(<StudyApp />);
    expect(await screen.findByRole('heading', { name: '危険物取扱者' })).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'ケースを見る' }));
    const caseHeading = await screen.findByText('ガソリン臭のする倉庫');
    const card = caseHeading.closest('article'); expect(card).not.toBeNull();
    fireEvent.click(within(card!).getByRole('button', { name: 'このケースを始める' }));
    expect(await screen.findByText(/倉庫の扉を開けると強い石油系の臭気/)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: /照明スイッチには触れず/ }));
    expect(await screen.findByText(/着火源を増やさずに状況確認へ進める/)).toBeInTheDocument();
    expect(document.body.textContent).not.toMatch(/正解|不正解/);
    fireEvent.click(screen.getByRole('button', { name: '続ける' }));
    fireEvent.click(screen.getByRole('button', { name: '危険物手帳' }));
    fireEvent.click(await screen.findByRole('button', { name: '着火源と蒸気' }));
    await waitFor(() => expect(screen.getByRole('button', { name: /床面や低所へ蒸気/ })).not.toBeDisabled());
    fireEvent.click(screen.getByRole('button', { name: /床面や低所へ蒸気/ }));
    await waitFor(async () => {
      const db = await openDB('qualification-study'); const stored = await db.getAll('learning-events'); db.close();
      expect(stored.some((event: { assistance?: string }) => event.assistance === 'handbook')).toBe(true);
    });
  });

  it('renders debrief sections and related knowledge', () => {
    const pack = loadContentPacks().find((item) => item.manifest.id === 'hazardous-materials')!;
    const story = pack.stories.find((item) => item.id === 'warehouse')!;
    let session = startStorySession(story, 'gasoline-leak', new Date('2026-09-14T00:00:00Z'));
    session = choose(story, session, 'avoid-switch', new Date('2026-09-14T00:01:00Z')).session;
    render(<Debrief pack={pack} story={story} session={{ ...session, endingId: 'controlled' }} onDone={() => undefined} />);
    expect(screen.getByRole('heading', { name: 'あなたの判断' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: '起きたこと' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: '関係する知識' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: '試験ではどう問われるか' })).toBeInTheDocument();
    expect(screen.getByText('漏洩時は着火源を増やさない')).toBeInTheDocument();
  });
});
