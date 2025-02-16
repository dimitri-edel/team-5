import axios from "axios";

if (process.env.NODE_ENV === 'production') {
    axios.defaults.baseURL = "https://team5-api-eu-5d24fa110c36.herokuapp.com/api";
} else {
    axios.defaults.baseURL = "http://localhost:8000";
}

// axios.defaults.baseURL = "https://team5-api-eu-5d24fa110c36.herokuapp.com/api";
// axios.defaults.baseURL = "http://localhost:8000";
axios.defaults.headers.post['Content-Type'] = "multipart/form-data";
axios.defaults.headers.get['Access-Control-Allow-Origin'] = "*";
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();
