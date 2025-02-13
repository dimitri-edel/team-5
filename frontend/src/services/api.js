const PROD_API_URL = 'https://team5-api-eu-5d24fa110c36.herokuapp.com/api';
const DEV_API_URL = 'http://127.0.0.1:8000/api';

const API_URL = process.env.NODE_ENV === 'production' ? PROD_API_URL : DEV_API_URL;

export const getHelloWorld = async () => {
  try {
    console.log('Fetching from API URL:', API_URL);
    const response = await fetch(`${API_URL}/`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log('API Response:', data);
    return data;
  } catch (error) {
    console.error('Error fetching hello world:', error);
    throw error;
  }
}; 