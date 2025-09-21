from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import AIMessage, HumanMessage

import os
from dotenv import load_dotenv
load_dotenv()

def summarize_node(state):
    docs=state.get("documents", [])
    if not docs:
        print("No documents to summarize!")
        return state
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

    summaries=[]
    for doc in docs:
        prompt=ChatPromptTemplate.from_messages([
            ("system", "You are helpful assistant that summarizes document concisely."),
            ("human", "{text}")
        ])
        input_text=doc.page_content
        message=prompt.format_prompt(text=input_text).to_messages()
        summary=llm.invoke(message).content
        doc.metadata["summary"]=summary
        summaries.append(doc)

    state["documents"]=summaries
    print("Summarization completed for all documents")
    return state    