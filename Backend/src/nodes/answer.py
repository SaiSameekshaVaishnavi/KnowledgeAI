import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path=Path('../../.env'))
API_KEY = os.getenv("GEMINI_API_KEY")

def answer_node(state: dict, query_text: str) -> dict:
    docs = state.get("query_results", [])
    if not docs:
        print("No chunks found for answering!")
        return state

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY not found in environment")

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=API_KEY)

    # Build a compact context by concatenating top doc texts (limit length if needed)
    context_pieces = []
    for d in docs:
        # LangChain Document object often has .page_content
        content = getattr(d, "page_content", None) or (d if isinstance(d, str) else "")
        context_pieces.append(content)

    # Join and truncate if very long (avoid sending too much)
    context = "\n\n".join(context_pieces)
    if len(context) > 12000:
        context = context[:12000]  # simple truncation; tune as needed

    prompt = f"""You are an assistant that answers the question using ONLY the context below.
If the answer is not in the context, reply: "I don't know."

Context:
{context}

Question: {query_text}
"""

    resp = llm.invoke(prompt)
    resp_text=getattr(resp, "content", None) or getattr(resp, "text", None)
    state["answers"] = [resp_text]
    print("Generated answer using Gemini.")
    return state