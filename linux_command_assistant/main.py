import os
import json
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

CONFIG_FILE = Path.home() / ".local" / "share" / "linux_command_assistant" / "config.json"

def load_api_key():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f).get("api_key")
    return None

def get_command_for_question(question: str) -> str:
    llm = ChatOpenAI(temperature=0.0)
    prompt = PromptTemplate(
        input_variables=["question"],
        template="You are a Linux terminal expert. Given the question, output only the correct Linux command.\n\nQuestion: {question}\n\nCommand:"
    )
    chain = prompt | llm
    result = chain.invoke(input={"question": question})
    return result.content
