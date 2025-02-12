import { describe, it, expect, beforeAll, afterAll, afterEach } from 'vitest';
import { render, screen, waitForElementToBeRemoved } from '@testing-library/react';
import { setupServer } from 'msw/node';
import { rest } from 'msw';
import { HelloWorld } from '../HelloWorld';

const API_URL = '/api';

const server = setupServer(
  rest.get(API_URL, (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({ message: 'Hello, World!' })
    );
  })
);

// Start server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));

// Close server after all tests
afterAll(() => server.close());

// Reset handlers after each test
afterEach(() => server.resetHandlers());

describe('HelloWorld Component', () => {
  it('should display loading state initially', () => {
    render(<HelloWorld />);
    expect(screen.getByTestId('loading')).toBeInTheDocument();
  });

  it('should display the hello world message from API', async () => {
    render(<HelloWorld />);
    
    // Wait for loading to disappear
    await waitForElementToBeRemoved(() => screen.getByTestId('loading'));
    
    // Check if message is displayed
    const messageElement = screen.getByTestId('message');
    expect(messageElement).toBeInTheDocument();
    expect(messageElement.textContent).toBe('Hello, World!');
  });

  it('should display error message when API fails', async () => {
    // Override the default handler to return an error
    server.use(
      rest.get(API_URL, (req, res, ctx) => {
        return res(ctx.status(500));
      })
    );

    render(<HelloWorld />);
    
    // Wait for loading to disappear
    await waitForElementToBeRemoved(() => screen.getByTestId('loading'));
    
    // Check if error message is displayed
    const errorElement = screen.getByTestId('error');
    expect(errorElement).toBeInTheDocument();
    expect(errorElement.textContent).toBe('Failed to fetch message from API');
  });
}); 