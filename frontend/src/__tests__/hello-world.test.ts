import { describe, it, expect, beforeAll, afterAll, afterEach } from 'vitest';
import { setupServer } from 'msw/node';
import { rest } from 'msw';
import axios from 'axios';

const API_URL = 'https://team5-api-eu-5d24fa110c36.herokuapp.com/';

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

//  Close server after all tests
afterAll(() => server.close());

// Reset handlers after each test
afterEach(() => server.resetHandlers());

describe('Hello World API', () => {
  it('should return hello world message', async () => {
    const response = await axios.get(API_URL);
    expect(response.status).toBe(200);
    expect(response.data).toEqual({ message: 'Hello, World!' });
  });

  it('should handle API errors', async () => {
    // Override the default handler for this test
    server.use(
      rest.get(API_URL, (req, res, ctx) => {
        return res(ctx.status(500));
      })
    );

    try {
      await axios.get(API_URL);
    } catch (error: any) {
      expect(error.response.status).toBe(500);
    }
  });
}); 