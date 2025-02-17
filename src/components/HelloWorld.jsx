import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

const PROD_API_URL = 'https://team5-api-eu-5d24fa110c36.herokuapp.com/';
const DEV_API_URL = '/api';

export function HelloWorld() {
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMessage = async () => {
      try {
        // Use the development URL by default
        const apiUrl = process.env.NODE_ENV === 'production' ? PROD_API_URL : DEV_API_URL;
        const response = await axios.get(apiUrl);
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