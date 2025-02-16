import axios from "axios";

axios.defaults.baseURL = "https://team5-api-eu-5d24fa110c36.herokuapp.com/api";
// axios.defaults.baseURL = "http://localhost:8000";
axios.defaults.headers.post['Content-Type'] = "multipart/form-data";
axios.defaults.withCredentials= true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();