import { test, expect } from '@playwright/test';

test.describe('API Tests', () => {
  const API_URL = 'http://127.0.0.1:8000';
  const FRONTEND_URL = 'http://localhost:3000';

  test('should return correct message from direct API endpoint /test/', async ({ request }) => {
    const response = await request.get(`${API_URL}/test/`);
    expect(response.ok()).toBeTruthy();
    
    const data = await response.json();
    expect(data).toEqual({ message: 'API is working!' });
  });

  test('should return correct message from frontend proxy endpoint /api/test/', async ({ request }) => {
    const response = await request.get(`${FRONTEND_URL}/api/test/`);
    expect(response.ok()).toBeTruthy();
    
    const data = await response.json();
    expect(data).toEqual({ message: 'API is working!' });
  });
}); 