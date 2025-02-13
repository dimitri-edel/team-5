import { test, expect } from '@playwright/test';

test('frontend can receive Hello World from API in development', async ({ page }) => {
  // Navigate to the frontend application
  await page.goto('http://localhost:5173');
  
  // Wait for the API response to be displayed
  // This assumes the response is rendered in an element with data-testid="hello-world"
  const helloWorldElement = await page.waitForSelector('[data-testid="hello-world"]');
  
  // Get the text content
  const text = await helloWorldElement.textContent();
  
  // Verify the content matches what we expect
  expect(text).toBe('Hello World');
}); 