import axios from "axios";

axios.defaults.baseURL = "https://team5-api-eu-5d24fa110c36.herokuapp.com/";
axios.defaults.headers.post['Content-Type'] = 'multipart/form-data';
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();