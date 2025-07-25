from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from graphs.workflow import build_graph
from nodes.market_analyst import market_analyst_agent

app = FastAPI()

#schema for search query
class SearchQuery(BaseModel):
    query: Annotated[str, Field(description="The search query to be processed")]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the VettIQ API"}

@app.post("/research")
def search(request: SearchQuery):
    graph=build_graph()
    result=graph.invoke(request.query)
    return {"query": request.query, "result": result}