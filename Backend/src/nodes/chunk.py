from ..utils import split_documents

def chunk_node(state):
    print("Current State in chunks", state)
    docs=state.get("documents", [])
    if not docs:
        print("No documents found to chunk!")
        return state
    
    chunks=split_documents(docs, chunk_size=1000, chunk_overlap=200)
    state["chunks"]=chunks
    print(f"Created {len(chunks)} chunks")
    
    return state