from .embeddings import embeddings_model, index_name, PineconeVectorStore

def embed_note(state: dict) -> dict:
    print("Current State in Embeddings", state)
    documents = state.get("chunks", None)
    if documents is None:
        print("⚠ No chunks found in state")
        state["vectorstore"] = None
        return state

    try:
        vectordb = PineconeVectorStore.from_documents(documents, embeddings_model, index_name=index_name)
        state["vectorstore"] = vectordb
        print(f"Created vector store with {len(documents)} documents.")
    except Exception as e:
        print(f"Error creating vector store: {e}")
        state["vectorstore"] = None
    
    return state