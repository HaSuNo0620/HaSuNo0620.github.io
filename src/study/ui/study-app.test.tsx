import { fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { openDB } from 'idb';
import { describe, expect, it } from 'vitest';
import StudyApp from './StudyApp';

describe('StudyApp', () => {
  it('navigates from qualification selection into consequence-first case play and records handbook assistance', async () => {
    render(<StudyApp />);
    expect(await screen.findByRole('heading', { name: '危険物取扱者' })).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'ケースを見る' }));
    const caseHeading = await screen.findByText('ガソリン臭のする倉庫');
    const card = caseHeading.closest('article');
    expect(card).not.toBeNull();
    fireEvent.click(within(card!).getByRole('button', { name: 'このケースを始める' }));

    expect(await screen.findByText(/倉庫の扉を開けると強い石油系の臭気/)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: /照明スイッチには触れず/ }));
    expect(await screen.findByText(/着火源を増やさずに状況確認へ進める/)).toBeInTheDocument();
    expect(document.body.textContent).not.toMatch(/正解|不正解/);

    fireEvent.click(screen.getByRole('button', { name: '続ける' }));
    expect(await screen.findByText(/床付近で臭気が強く/)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: '危険物手帳' }));
    fireEvent.click(await screen.findByRole('button', { name: '着火源と蒸気' }));
    fireEvent.click(screen.getByRole('button', { name: /床面や低所へ蒸気/ }));

    await waitFor(async () => {
      const db = await openDB('qualification-study');
      const events = await db.getAll('learning-events');
      db.close();
      expect(events.some((event: { assistance?: string }) => event.assistance === 'handbook')).toBe(true);
    });
  });
});
