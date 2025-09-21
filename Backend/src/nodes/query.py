import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def query_node(state: dict, query_text: str, top_k: int = 4) -> dict:
    vectordb = state.get("vectorstore", None)

    if vectordb is None:
        print("⚠ No vectorstore found in state")
        state["query_results"] = []
        return state

    try:
        docs = vectordb.similarity_search(query_text, k=top_k)
    except Exception:
        try:
            retriever = vectordb.as_retriever(search_kwargs={"k": top_k})
            docs = retriever.invoke(query_text)
        except Exception as e:
            print(f"Error during similarity search: {e}")
            docs = []

    state["query_results"] = docs
    print(f"Retrieved {len(docs)} documents for the query.")
    return state