import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

const PROD_API_URL = 'https://team5-api-eu-5d24fa110c36.herokuapp.com/api/';
const DEV_API_URL = 'http://127.0.0.1:8000/api/';

export function HelloWorld() {
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMessage = async () => {
      try {
        const apiUrl = process.env.NODE_ENV === 'production' ? PROD_API_URL : DEV_API_URL;
        console.log('Current environment:', process.env.NODE_ENV);
        console.log('Using API URL:', apiUrl);
        const response = await axios.get(apiUrl);
        console.log('API Response:', response.data);
        setMessage(response.data.message);
        setError('');
      } catch (err) {
        console.error('API Error Details:', {
          message: err.message,
          response: err.response?.data,
          status: err.response?.status,
          headers: err.response?.headers
        });
        setError(`Failed to fetch message from API: ${err.message}`);
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

  return <div data-testid="hello-world">{message}</div>;
} 