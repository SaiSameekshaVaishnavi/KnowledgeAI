from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def split_documents(docs, chunk_size=3000, chunk_overlap=300):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

def enhance_query(query: str) -> str:
    """
    Uses Gemini to rephrase/expand the user query
    into a more detailed and retrieval-friendly version.
    """

    if not API_KEY:
        raise ValueError("❌ GEMINI_API_KEY not found in environment")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=API_KEY
    )

    prompt = f"""
    You are a query enhancer for a knowledge base system.
    Given a user query, rewrite it to be more detailed,
    include synonyms and related terminology, but DO NOT
    change its original meaning.

    User query: "{query}"
    """

    try:
        resp = llm.invoke(prompt)
        enhanced = resp.content.strip()
        return enhanced
    except Exception as e:
        print(f"⚠ Query enhancement failed: {e}")
        return query 