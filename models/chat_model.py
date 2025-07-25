from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from tools.web_search_tool import web_search
import os
from dotenv import load_dotenv
from config import REPO_ID, TEMPERATURE, MAX_NEW_TOKENS
load_dotenv()

tools_list=[web_search]
api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not api_key:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN environment variable is not set.")
chat_model=ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id=REPO_ID,
        max_new_tokens=MAX_NEW_TOKENS,
        temperature=TEMPERATURE,
        huggingfacehub_api_token=api_key
        )
    )
llm_with_tools=chat_model.bind_tools(tools_list)  # No tools are bound in this case