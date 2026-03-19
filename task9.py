from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request models
class ChatRequest(BaseModel):
    message: str

class SummarizeRequest(BaseModel):
    text: str

# Home route (to check server)
@app.get("/")
def home():
    return {"message": "API is running successfully"}

# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": "You said: " + req.message}

# Summarize endpoint
@app.post("/summarize")
def summarize(req: SummarizeRequest):
    words = req.text.split()
    summary = " ".join(words[:10])   # simple summary
    return {"summary": summary}