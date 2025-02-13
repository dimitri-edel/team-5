const API_URL = 'http://127.0.0.1:8000';

export const getHelloWorld = async () => {
  try {
    const response = await fetch(`${API_URL}/api/`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching hello world:', error);
    throw error;
  }
}; 