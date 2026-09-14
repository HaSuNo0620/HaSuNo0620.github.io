import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import StudyApp from './StudyApp';

describe('StudyApp', () => {
  it('renders qualification selection then all unordered cases', async () => {
    render(<StudyApp />);
    expect(screen.getByRole('heading', { name: '資格学習' })).toBeInTheDocument();
    const qualification = await screen.findByRole('heading', { name: '危険物取扱者' });
    expect(qualification).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'ケースを見る' }));
    expect(await screen.findByText('ガソリン臭のする倉庫')).toBeInTheDocument();
    expect(screen.getByText('溶剤を扱う作業場')).toBeInTheDocument();
    expect(screen.getByText('正体不明の液体')).toBeInTheDocument();
    expect(screen.getAllByRole('button', { name: 'このケースを始める' })).toHaveLength(3);
    expect(screen.getByText('今やるならこれ')).toBeInTheDocument();
  });
});
