

from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

#from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

#from langchain.agents import create_agent
#from langchain.agents import AgentExecutorA

#from tools import search_tool, wiki_tool, save_tool

# Running on github / codespaces
import os;
openai_api_key = os.environ.get("OPENAI_API_KEY") # Assumes OPENAI_API_KEY setup in github secrets
anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY") # Assumes OPENAI_API_KEY setup in github secrets

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=openai_api_key) 
#llm_claude = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0, api_key=anthropic_api_key)

# # Running on local machines
# from dotenv import load_dotenv # Load in environment variable, including secrete keys for .env
# # *** If using this method ensure .env is listed in .gitignore do it STAYS local

# llm = ChatOpenAI(model="gpt-4", temperature=0, api_key="OPENAI_API_KEY") 
# llm_claude = ChatAnthropic(model="claude-2", temperature=0, api_key="ANTHROPIC_API_KEY")




response = llm.invoke("What is the capital of France?")
print(response)