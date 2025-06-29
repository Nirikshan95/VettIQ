from langchain_community.tools import DuckDuckGoSearchRun

def web_search(query: str) -> str:
    """
    Perform a web search using DuckDuckGo and return the results.
    
    Args:
        query (str): The search query.
        
    Returns:
        str: The search results.
    """
    search_tool = DuckDuckGoSearchRun()
    result = search_tool.run(query)
    return result