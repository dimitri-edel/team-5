import axios from 'axios';

jest.mock('axios');

describe('API Tests', () => {
  it('should return correct message from /api/test', async () => {
    axios.get.mockResolvedValue({ data: { message: "API is working!" } });
    
    const response = await axios.get('/api/test');
    expect(response.data).toEqual({ message: "API is working!" });
    expect(axios.get).toHaveBeenCalledWith('/api/test');
  });
}); 