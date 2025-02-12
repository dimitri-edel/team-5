import { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = 'https://team5-api-eu-5d24fa110c36.herokuapp.com/';

interface ApiResponse {
  message: string;
}

export function HelloWorld() {
  const [message, setMessage] = useState<string>('');
  const [error, setError] = useState<string>('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMessage = async () => {
      try {
        const response = await axios.get<ApiResponse>(API_URL);
        setMessage(response.data.message);
        setError('');
      } catch (err) {
        setError('Failed to fetch message from API');
        setMessage('');
      } finally {
        setLoading(false);
      }
    };

    fetchMessage();
  }, []);

  if (loading) {
    return <div data-testid="loading">Loading...</div>;
  }

  if (error) {
    return <div data-testid="error" className="error">{error}</div>;
  }

  return <div data-testid="message">{message}</div>;
} 