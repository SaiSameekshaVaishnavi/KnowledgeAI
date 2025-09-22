# 📘 KnowledgeAI – Document Q&A System

**Knowledge AI** is an end-to-end **Retrieval-Augmented Generation (RAG)** system that allows users to *upload documents from the Frontend* and then *query them through natural language*. Powered by **LangChain, LangGraph, Gemini, Pinecone**

---
## ✨ Features

- 💡 **Document Upload**:
Upload files (.pdf, .txt, etc.) directly from the frontend.


- ⚙ **Automatic Chunking**:
Splits large documents into manageable chunks for efficient retrieval.


- 📁 **Smart Embeddings**:
Uses Google Generative AI Embeddings (Gemini) to represent document content.


- 🧾 **Semantic Search**:
Stores embeddings in Pinecone for fast and relevant similarity search.


- 🔊 **Question Answering**:
Ask questions about uploaded documents and get precise, context-aware answers.


- **Frontend**  
    - ⚛ React  
    - 🟦 TypeScript  
    - 🎨 TailwindCSS  

- **Backend**  
    - 🚀 FastAPI  
    - 🔗 LangChain  
    - 🧩 LangGraph  
    - 📦 Pinecone  
    - 🤖 Gemini LLM  
   
---

## 🧠 Tech Stack
| Layer | Tools |
|-------|-------|
| LLM | Gemini, LangChain, LangGraph |
| Frontend | React, Typescript, HTML5/CSS3, TailwindCSS |
| Backend | Python, FastAPI, Uvicorn|
| Vector Database | Pinecone |
| Workflow Graph | LangGraph |

---

## 🗂 Project Structure
 ```
 KnowledgeAI/
│
├── Backend/
│ ├── src/
│ │ ├── api.py # FastAPI routes for /upload and /ask
│ │ ├── nodes/ # Node functions: load_documents, chunking, embeddings, query, answer
│ │ ├── workflows/ # LangGraph ingestion graph
│ │ ├── utils.py # Helpers: split documents, enhance query
│ │ └── embeddings.py # Vector store creation with Pinecone
│ ├── .env # API keys for Gemini & Pinecone
│ └── requirements.txt # Python dependencies
│
├── Frontend/
│ ├── src/
│ │ ├── api.ts # Axios API calls
│ │ ├── components/
│ │ │ ├── Upload.tsx # File upload component
│ │ │ └── Chat.tsx # Chat interface component
│ │ ├── App.tsx # Main app entry
│ │ └── index.tsx # React root file
│ ├── package.json # Node dependencies
│ └── tailwind.config.js # TailwindCSS configuration
│
├── README.md
 ```


---

## 🚀 Getting Started

## Clone the repo
```
git clone https://github.com/yourusername/your-project-name
cd KNOWLEDGEAI
```
 ## To set up Backend
 1. Navigate to Backend Folder
    ```
    cd Backend
    ```

 2. Activate Virtual Environment or create if needed
    ```
    python -m venv .venv
    .venv\Scripts\activate   # Windows
    source .venv/bin/activate   # Mac/Linux
    ```
  
  3. Install Dependencies
     ```
     pip install -r requiremnts.txt
     ```
  
  4. Add .env file
     ```
      GEMINI_API_KEY=your_api_key
      PINECONE_API_KEY=your_api_key
     ```
  
  5. Run the Fast API Server
     ```
     uvicorn src.api:app --reload
     ```


 ## To set up Frontend
 1. Navigate to Frontend Folder
    ```
    cd Frontend
    ```

 2. Install Dependencies
     ```
     npm install
     ```
  
  3.  Run the DEV Server
      ``` 
       npm dev run
      ```    

---
## 🗣 How It Works

### 🖥 Frontend  
- Users can **upload documents** (`.pdf`, `.txt`) via a simple UI.  
- After processing, users can **ask natural language questions** about the uploaded document.  
- The UI communicates with the backend using **Axios API calls**.  

### ⚡ Backend  

**File Upload API (`/upload`)**  
- Accepts the file from the frontend.  
- Reads the contents and **splits them into smaller chunks** for better retrieval.  
- Generates **vector embeddings** using **Google Generative AI embeddings (Gemini)**.  
- Stores embeddings in **Pinecone** for semantic search.  

**Query API (`/ask`)**  
- Enhances the user query with **Gemini LLM** for better retrieval quality.  
- Searches **Pinecone** for the most relevant chunks.  
- Uses the **LLM** to generate a final, context-aware answer.  

### 🔗 Workflow (Ingestion Pipeline with LangGraph)  
1. Upload File → Load Documents
2. Chunk Documents → Create Embeddings  
3. Store in Pinecone → Summarize

🧪 **Example Prompts**
- “I have uploaded a PDF about life, explain about life”
- “Explain about necessities for a happy life”


---  

### 👨‍💻 Author: Sameeksha Vaishnavi
📄 MIT License – Feel free to use, modify and distribute!
