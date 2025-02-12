import { useState, useEffect } from 'react';
import axios from 'axios';

// Use the proxied URL in development
const API_URL = '/api';

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
        console.error('API Error:', err);
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