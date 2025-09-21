import uvicorn
from fastapi import FastAPI
from api import router as api_router

def create_app()-> FastAPI:
    app = FastAPI(
        title="KnowledgeAI Backend",
        description="API for KnowledgeAI application",
        version="1.0.0"
    )
    app.include_router(api_router, prefix="/api")
    return app

def main():
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()    