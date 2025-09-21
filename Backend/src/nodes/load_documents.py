from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from typing import Dict, Any
from io import BytesIO


def load_documents_node(state: Dict[str, Any]) -> Dict[str, Any]:
    print("Current State in Load Documents", state)
    uploaded_file = state.get("uploaded_file", None)
    if uploaded_file is None:
        print("No uploaded file found in state")
        state["documents"] = []
        return state
    
    file_bytes = uploaded_file.get("content", None)
    filename = uploaded_file.get("filename", "unknown")
    
    ext=filename.split(".")[-1].lower()

    if ext==".pdf":
     loader=PyPDFLoader(BytesIO(file_bytes))
     docs=loader.load()
    elif ext==".txt":
        loader=TextLoader(BytesIO(file_bytes))
        docs=loader.load()
    else:
        text=file_bytes.decode("utf-8", errors="ignore")
        docs=[Document(page_content=text, metadata={"source": filename})]   
    
    state["documents"]=docs
    print(f"Loaded {len(docs)} documents from {filename}")
    
    return state
