import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export async function UploadFile (file: File){
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
}

export async function askQuestion (question: string){
  const response = await axios.post(`${API_BASE_URL}/ask`, { question}, {headers: {
    "Content-Type": "application/json",
  },});
  return response.data; 
}

