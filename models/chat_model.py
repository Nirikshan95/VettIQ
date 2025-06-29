from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import os
from dotenv import load_dotenv
from config import REPO_ID, TEMPERATURE, MAX_NEW_TOKENS
load_dotenv()

def load_chat_model() -> ChatHuggingFace:
    """
    Load a chat model from Hugging Face.

    Args:
        model_name (str): The name of the model to load.

    Returns:
        ChatHuggingFace: The loaded chat model.
    """
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not api_key:
        raise ValueError("HUGGINGFACEHUB_API_TOKEN environment variable is not set.")
    return ChatHuggingFace(
        llm=HuggingFaceEndpoint(
            repo_id=REPO_ID,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            huggingfacehub_api_key=api_key
        )
    )