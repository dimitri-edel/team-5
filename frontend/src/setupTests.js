import '@testing-library/jest-dom';
import axios from 'axios';
import { TextEncoder, TextDecoder } from 'util';

global.TextEncoder = TextEncoder;
global.TextDecoder = TextDecoder;

// Configure axios for tests
axios.defaults.baseURL = 'http://localhost:8000'; 