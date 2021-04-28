import axios from "axios";
import { handleError } from "./error_handler/error_handler";

const url = "http://localhost:8000";
const baseUrl = url + "/api/";



const get = (url) => {
    return axios
        .get(baseUrl + url)
        .then((response) => {
            return response.data;
        })
        .catch((err) => {
            const message = handleError(err)
            throw new Error(message);
        });
}


const api = {
    get,
};

export default api;