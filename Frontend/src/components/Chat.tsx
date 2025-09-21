import React, { useState } from "react";
import { askQuestion } from "../api";

const Chat: React.FC = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    try {
      const res = await askQuestion(question);

      const text = res.answer || "No answer found.";
      let i = 0;
      const interval = setInterval(() => {
        setAnswer((prev) => prev + text.charAt(i));
        i++;
        if (i >= text.length) {
          clearInterval(interval);
          setLoading(false);
        }
      }, 20);
    } catch (err) {
      setAnswer(
        "Failed to get answer. Please try again."
      );
      setLoading(false);
    }
  };

  return (
    <div className="max-w-lg mx-auto mt-10 p-6 bg-white shadow-xl rounded-2xl border border-gray-200">
      <h2 className="text-xl font-bold mb-4 text-gray-800">
        Chat with Document
      </h2>
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a question..."
          className="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm"
        />

        <button
          onClick={handleAsk}
          disabled={!question.trim()}
          className={`py-2 px-4 rounded-lg font-medium transition ${
            question.trim()
              ? "bg-green-600 text-white hover:bg-green-700"
              : "bg-gray-300 text-gray-500 cursor-not-allowed"
          }`}
        >
          {loading ? "..." : "Ask"}
        </button>
      </div>

      {loading && (
        <div className="flex items-center space-x-2 text-gray-500">
          <div className="w-4 h-4 border-2 border-gray-400 border-t-transparent rounded-full animate-spin"></div>
          <span>Thinking...</span>
        </div>
      )}

      {answer && !loading && (
        <div className="p-3 bg-gray-100 rounded-lg text-sm text-gray-800 whitespace-pre-line">
          <strong>Answer:</strong> {answer}
        </div>
      )}
    </div>
  );
};

export default Chat;
