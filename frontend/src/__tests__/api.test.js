import { describe, it, expect, vi } from 'vitest';
import { getHelloWorld } from '../services/api';

// Mock fetch globally
global.fetch = vi.fn();

describe('API Integration Tests', () => {
  beforeEach(() => {
    fetch.mockReset();
  });

  it('successfully fetches hello world message', async () => {
    // Mock the fetch response
    const mockResponse = { message: 'Hello, World!' };
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse,
    });

    const result = await getHelloWorld();
    
    // Verify the fetch was called with the correct URL
    expect(fetch).toHaveBeenCalledWith('http://127.0.0.1:8000/api/');
    
    // Verify we got the expected response
    expect(result).toEqual(mockResponse);
  });

  it('handles API errors appropriately', async () => {
    // Mock a failed response
    fetch.mockResolvedValueOnce({
      ok: false,
      status: 500
    });

    // Verify that the error is thrown
    await expect(getHelloWorld()).rejects.toThrow('HTTP error! status: 500');
  });
}); 