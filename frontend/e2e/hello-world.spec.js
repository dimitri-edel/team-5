import { test, expect } from '@playwright/test';

test('API endpoint returns hello world message', async ({ request }) => {
  // Test the API directly
  const response = await request.get('https://team5-api-eu-5d24fa110c36.herokuapp.com/');
  expect(response.ok()).toBeTruthy();
  const data = await response.json();
  expect(data.message).toBe('Hello, World!');
});

test('Frontend displays hello world message from API', async ({ page }) => {
  // Test the frontend application
  await page.goto('https://team5-frontend-eu-f40f1bfc04e7.herokuapp.com/');
  
  // Wait for loading state to disappear
  await page.waitForSelector('[data-testid="loading"]', { state: 'hidden' });
  
  // Check for the message
  const messageElement = await page.getByTestId('message');
  await expect(messageElement).toBeVisible();
  await expect(messageElement).toHaveText('Hello, World!');
});

test('Frontend handles API errors gracefully', async ({ page }) => {
  // Mock the API to return an error
  await page.route('**/api', route => route.abort());
  
  // Visit the frontend
  await page.goto('https://team5-frontend-eu-f40f1bfc04e7.herokuapp.com/');
  
  // Wait for loading state to disappear
  await page.waitForSelector('[data-testid="loading"]', { state: 'hidden' });
  
  // Check for error message
  const errorElement = await page.getByTestId('error');
  await expect(errorElement).toBeVisible();
  await expect(errorElement).toHaveText('Failed to fetch message from API');
}); 