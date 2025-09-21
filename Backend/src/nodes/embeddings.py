import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone.vectorstores import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone
pinecone = Pinecone(api_key=PINECONE_API_KEY)

index_name="knowledgeai-index"

spec=ServerlessSpec(
        cloud="aws", region="us-east-1"
)

if(index_name not in [i["name"] for i in pinecone.list_indexes()]):
    pinecone.create_index(name=index_name, dimension=768, metric="cosine", spec=spec)

index=pinecone.Index(index_name)

embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=API_KEY
)

def create_vector_space(docs):
    return PineconeVectorStore.from_documents(docs, embeddings_model, index_name=index_name)