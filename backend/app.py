from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Ronex AI Backend Running"}

@app.post("/chat")
def chat(req: ChatRequest):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are Ronex AI, a powerful AI assistant."
            },
            {
                "role": "user",
                "content": req.message
            }
        ]
    )

    return {
        "response": response.choices[0].message.content
    }
