from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

#schema for search query
class SearchQuery(BaseModel):
    query: Annotated[str, Field(description="The search query to be processed")]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the VettIQ API"}

@app.post("/search")
def search(query: SearchQuery):
    return {"query": query.query, "message": "This is a placeholder for the search functionality."}