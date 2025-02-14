import React from 'react';
import { describe, it, expect, beforeAll, afterAll, afterEach, beforeEach, vi } from 'vitest';
import { render, screen, waitForElementToBeRemoved } from '@testing-library/react';
import { setupServer } from 'msw/node';
import { http, HttpResponse } from 'msw';
import { HelloWorld } from '../HelloWorld';

const PROD_API_URL = 'https://team5-api-eu-5d24fa110c36.herokuapp.com/api/';
const DEV_API_URL = 'http://127.0.0.1:8000/api/';

const server = setupServer();

// Start server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: 'warn' }));

// Close server after all tests
afterAll(() => server.close());

// Reset handlers after each test
afterEach(() => {
  server.resetHandlers();
  vi.unstubAllEnvs();
});

describe('HelloWorld Component in Development', () => {
  beforeEach(() => {
    vi.stubEnv('NODE_ENV', 'development');
    server.use(
      http.get(DEV_API_URL, () => {
        return HttpResponse.json({ message: 'Hello, World!' });
      })
    );
  });

  it('should display loading state initially', () => {
    render(<HelloWorld />);
    expect(screen.getByTestId('loading')).toBeInTheDocument();
  });

  it('should display the hello world message from API', async () => {
    render(<HelloWorld />);
    await waitForElementToBeRemoved(() => screen.getByTestId('loading'));
    const messageElement = screen.getByTestId('hello-world');
    expect(messageElement).toBeInTheDocument();
    expect(messageElement.textContent).toBe('Hello, World!');
  });

  it('should display error message when API fails', async () => {
    server.use(
      http.get(DEV_API_URL, () => {
        return new HttpResponse(null, { status: 500 });
      })
    );
    render(<HelloWorld />);
    await waitForElementToBeRemoved(() => screen.getByTestId('loading'));
    expect(screen.getByTestId('error')).toBeInTheDocument();
  });
});

describe('HelloWorld Component in Production', () => {
  beforeEach(() => {
    vi.stubEnv('NODE_ENV', 'production');
    server.use(
      http.get(PROD_API_URL, () => {
        return HttpResponse.json({ message: 'Hello, World!' });
      })
    );
  });

  it('should display the hello world message from production API', async () => {
    render(<HelloWorld />);
    await waitForElementToBeRemoved(() => screen.getByTestId('loading'));
    const messageElement = screen.getByTestId('hello-world');
    expect(messageElement).toBeInTheDocument();
    expect(messageElement.textContent).toBe('Hello, World!');
  });

  it('should display error message when production API fails', async () => {
    server.use(
      http.get(PROD_API_URL, () => {
        return new HttpResponse(null, { status: 500 });
      })
    );
    render(<HelloWorld />);
    await waitForElementToBeRemoved(() => screen.getByTestId('loading'));
    expect(screen.getByTestId('error')).toBeInTheDocument();
  });
}); 