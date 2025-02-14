import { test, expect } from '@playwright/test';

test('API endpoint returns hello world message in development', async ({ request }) => {
  // Test the API directly
  const response = await request.get('http://127.0.0.1:8000/api/');
  expect(response.ok()).toBeTruthy();
  const data = await response.json();
  expect(data.message).toBe('Hello, World!');
});

test('Frontend displays hello world message from API in development', async ({ page }) => {
  // Test the frontend application
  await page.goto('http://localhost:5173/');
  
  // Wait for loading state to disappear and log the page content for debugging
  await page.waitForSelector('[data-testid="loading"]', { state: 'hidden' });
  console.log('Page content after loading:', await page.content());
  
  // Check for the message
  const messageElement = await page.getByTestId('hello-world');
  await expect(messageElement).toBeVisible();
  await expect(messageElement).toHaveText('Hello, World!');
});

test('Frontend handles API errors gracefully in development', async ({ page }) => {
  // Mock the API to return an error
  await page.route('http://127.0.0.1:8000/api/', route => route.abort());
  
  // Visit the frontend
  await page.goto('http://localhost:5173/');
  
  // Wait for loading state to disappear
  await page.waitForSelector('[data-testid="loading"]', { state: 'hidden' });
  
  // Check for error message with the actual text
  const errorElement = await page.getByTestId('error');
  await expect(errorElement).toBeVisible();
  await expect(errorElement).toHaveText('Failed to fetch message from API: Network Error');
}); 