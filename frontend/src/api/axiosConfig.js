import axios from "axios";

const baseURL = process.env.NODE_ENV === 'production'
  ? "https://team5-api-eu-5d24fa110c36.herokuapp.com/api"
  : "http://localhost:8000";

axios.defaults.baseURL = baseURL;
axios.defaults.headers.post['Content-Type'] = "multipart/form-data";
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();