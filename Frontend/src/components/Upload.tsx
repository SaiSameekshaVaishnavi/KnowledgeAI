import React, { useState } from "react";
import { UploadFile } from "../api";

const Upload: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setStatus("");
    setLoading(true);

    try {
      const res = await UploadFile(file);
      setStatus(`Upload successful! ${res.chunks} chunks processed.`);
    } catch (err) {
      setStatus("Upload failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-lg mx-auto mt-10 p-6 bg-white shadow-xl rounded-2xl border border-gray-200">
      <h2 className="text-xl font-bold mb-4 text-gray-800">Upload Document</h2>
      <input
        type="file"
        accept=".pdf, .txt, .docx, .doc"
        onChange={(e) => setFile(e.target.files ? e.target.files[0] : null)}
        className="block w-full text-sm text-gray-600
        file:mr-4 file:py-2 file:px-4P
        file:rounded-lg file:border-0
        file:text-sm file:font-semibold
        file:bg-blue-50 file:text-blue-600
        hover:file:bg-blue-100
        mb-4
        "
      />
      <button
        onClick={handleUpload}
        disabled={!file || loading}
        className={
          "w-full flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-xl transition disabled:opacity-50 disabled:cursor-not-allowed"
        }
      >
        {loading && (
          <svg
            className="animate-spin h-5 w-5 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            ></circle>
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
            ></path>
          </svg>
        )}
        {loading ? "Uploading..." : "Upload"}
      </button>
      {status && (
        <p className="mt-4 text-center text-sm font-medium text-gray-700">
          {status}
        </p>
      )}
    </div>
  );
};
export default Upload;
