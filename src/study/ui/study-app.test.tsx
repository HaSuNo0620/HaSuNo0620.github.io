import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import StudyApp from './StudyApp';

describe('StudyApp', () => {
  it('renders the study heading', () => {
    render(<StudyApp />);
    expect(screen.getByRole('heading', { name: '資格学習' })).toBeInTheDocument();
  });
});
