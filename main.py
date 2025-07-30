from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated
from graphs.workflow import build_graph

app = FastAPI()
graph=build_graph()

# pydantic model for request body
class StartupIdea(BaseModel):
    startup_idea:Annotated[str,Field(...,description="Startup idea to validate")]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the VettiQ API"}

@app.post("/validate")
def research(idea:StartupIdea):
    try:
        result= graph.invoke({"startup_idea":idea.startup_idea})
        
        return JSONResponse(status_code=200, 
                            content={
                                "startup_idea": result.startup_idea,
                                "market_analysis":result.market_analysis,
                                "competition_analysis": result.competition_analysis,
                                "risk_assessment": result.risk_assessment,
                                "advisor_recommendations": result.advisor_recommendations,
                                "advice": result.advice}
                            )
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))