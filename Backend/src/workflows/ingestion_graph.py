from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Optional, Any
from ..nodes.load_documents import load_documents_node
from ..nodes.chunk import chunk_node
from ..nodes.embedNode import embed_note
from ..nodes.summarize import summarize_node
from langchain_pinecone import PineconeVectorStore

class IngestionState(TypedDict, total=False):
    uploaded_file: Optional[Any]
    documents: Optional[Any]
    chunks: Optional[List[Any]]
    vectorstore: Optional[PineconeVectorStore]
    summary: Optional[str]
    query_results: Optional[List[Any]]
    answers: Optional[str]

def build_langgraph():
    # Create the graph
    graph = StateGraph(state_schema=IngestionState)

    # Add nodes
    graph.add_node("load_docs" ,load_documents_node)
    graph.add_node("chunk",chunk_node)
    graph.add_node("embed", embed_note)
    graph.add_node("summarize",summarize_node)

    # Define linear edges
    graph.add_edge("load_docs", "chunk")
    graph.add_edge("chunk", "embed")
    graph.add_edge("embed", "summarize")
    graph.add_edge("summarize", END)

    graph.set_entry_point("load_docs") 
    return graph.compile()

def run_ingestion_graph(initial_state: IngestionState):
    if initial_state is None:
        initial_state = {}

    print("Starting ingestion pipeline with LangGraph...")

    # Build the graph
    app = build_langgraph()

    # Execute the graph
    try:
        final_state = app.invoke(initial_state)
        print("✅ Ingestion finished successfully.")
    except Exception as e:
        print("⚠ Error during ingestion:", e)
        final_state = initial_state

    return final_state