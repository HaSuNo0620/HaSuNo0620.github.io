import { fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { openDB } from 'idb';
import { describe, expect, it } from 'vitest';
import { loadContentPacks } from '../content/load-content';
import { startStorySession, choose } from '../domain/story-engine';
import Debrief from './Debrief';
import StudyApp from './StudyApp';

describe('StudyApp', () => {
  it('completes the full study flow including assistance, resume, debrief, history, and detailed mastery', async () => {
    const firstMount = render(<StudyApp />);
    expect(await screen.findByRole('heading', { name: '危険物取扱者' })).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'ケースを見る' }));
    const caseHeading = await screen.findByText('ガソリン臭のする倉庫');
    let card = caseHeading.closest('article'); expect(card).not.toBeNull();
    expect(within(card!).getByText('今やるならこれ')).toBeInTheDocument();
    fireEvent.click(within(card!).getByRole('button', { name: 'このケースを始める' }));

    fireEvent.click(await screen.findByRole('button', { name: /照明スイッチには触れず/ }));
    expect(await screen.findByText(/着火源を増やさずに状況確認へ進める/)).toBeInTheDocument();
    expect(document.body.textContent).not.toMatch(/正解|不正解/);
    fireEvent.click(screen.getByRole('button', { name: '続ける' }));

    fireEvent.click(screen.getByRole('button', { name: '危険物手帳' }));
    fireEvent.click(await screen.findByRole('button', { name: '着火源と蒸気' }));
    await waitFor(() => expect(screen.getByRole('button', { name: /床面や低所へ蒸気/ })).not.toBeDisabled());
    fireEvent.click(screen.getByRole('button', { name: /床面や低所へ蒸気/ }));
    expect(await screen.findByText(/空気より重い蒸気が低所へ広がる危険/)).toBeInTheDocument();

    firstMount.unmount();
    render(<StudyApp />);
    expect(await screen.findByRole('heading', { name: '危険物取扱者' })).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'ケースを見る' }));
    card = (await screen.findByText('ガソリン臭のする倉庫')).closest('article'); expect(card).not.toBeNull();
    fireEvent.click(within(card!).getByRole('button', { name: '続きから' }));
    expect(await screen.findByText(/空気より重い蒸気が低所へ広がる危険/)).toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: '続ける' }));
    fireEvent.click(await screen.findByRole('button', { name: '第一石油類として扱う' }));
    expect(await screen.findByText(/ガソリンを第一石油類として整理できた/)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: '続ける' }));
    fireEvent.click(await screen.findByRole('button', { name: /漏洩拡大を抑える対応/ }));
    expect(await screen.findByText(/非水溶性で水より軽いガソリン/)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: '続ける' }));
    fireEvent.click(await screen.findByRole('button', { name: /適応する消火方法/ }));

    expect(await screen.findByText(/事故拡大を抑えた/)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'ケースを振り返る' }));
    expect(await screen.findByRole('heading', { name: 'あなたの判断' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: '起きたこと' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: '関係する知識' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: '試験ではどう問われるか' })).toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: 'ケース一覧へ戻る' }));
    card = (await screen.findByText('ガソリン臭のする倉庫')).closest('article'); expect(card).not.toBeNull();
    expect(within(card!).getByText('1回完了')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: '理解の状態' }));
    fireEvent.click(await screen.findByRole('button', { name: '詳細を見る' }));
    expect(screen.getByRole('columnheader', { name: '適用' })).toBeInTheDocument();
    expect(screen.getByLabelText('漏洩時は着火源を増やさない apply')).toBeInTheDocument();

    const db = await openDB('qualification-study');
    const stored = await db.getAll('learning-events'); db.close();
    expect(stored.some((event: { assistance?: string }) => event.assistance === 'handbook')).toBe(true);
  });

  it('renders debrief sections and related knowledge in isolation', () => {
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
