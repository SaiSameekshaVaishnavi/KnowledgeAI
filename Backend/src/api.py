from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .workflows.ingestion_graph import run_ingestion_graph
from .nodes.query import query_node
from .nodes.answer import answer_node
from .utils import enhance_query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ptrcmpvl-5173.inc1.devtunnels.ms/", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile=File(...)):
    contents=await file.read()

    initial_state = {
        "uploaded_file": {
            "filename": file.filename,
            "content": contents
        }
    }
    print(f"Received file: {file.filename}, size: {len(contents)} bytes")
    final_state = run_ingestion_graph(initial_state)
    print("Final State after ingestion:", final_state)
    
    return {"status": "File processed successfully", "chunks": len(final_state.get("chunks", []))}


@app.post("/ask")
async def ask_question(question: str, state:dict):
    if not state or "vectorstore" not in state:
        return {"error": "No data ingested. Please upload a file first."}

    enhanced_query =enhance_query(question)
    state["query_text"] = enhanced_query

    state = query_node(state, enhanced_query)
    state = answer_node(state, question)

    answers = state.get("answers", [])
    if not answers:
        return {"error": "No answers found."}

    return {"answers": answers}