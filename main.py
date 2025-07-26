from fastapi import FastAPI
from pydantic import BaseModel, Field
from graphs.workflow import build_graph

app = FastAPI()
graph=build_graph()

# pydantic model for request body
class StartupIdea(BaseModel):
    startup_idea:str= Field(...,description="Startup idea to validate")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the VettiQ API"}

@app.post("/validate")
def research(idea:StartupIdea):
    
    result= graph.invoke({"startup_idea":idea.startup_idea})
    
    return {"result": result}