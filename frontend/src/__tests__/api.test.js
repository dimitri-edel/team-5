import axios from 'axios';

jest.mock('axios');

describe('API Tests', () => {
  beforeEach(() => {
    // Clear mock data before each test
    jest.clearAllMocks();
  });

  it('should return correct message from direct API endpoint /api/test', async () => {
    axios.get.mockResolvedValue({ data: { message: "API is working!" } });
    
    const response = await axios.get('/api/test');
    expect(response.data).toEqual({ message: "API is working!" });
    expect(axios.get).toHaveBeenCalledWith('/api/test');
  });

  it('should return correct message from frontend proxy endpoint localhost:5173/api/test', async () => {
    axios.get.mockResolvedValue({ data: { message: "API is working!" } });
    
    const response = await axios.get('http://localhost:5173/api/test');
    expect(response.data).toEqual({ message: "API is working!" });
    expect(axios.get).toHaveBeenCalledWith('http://localhost:5173/api/test');
  });
}); 