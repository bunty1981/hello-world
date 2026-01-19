from dotenv import load_dotenv # Load in environment variable, including secerte keys
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
#from langchain_anthropic import ChatAnthropic. -- blocked by firewall
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

#from langchain.agents import create_agent
#from langchain.agents import AgentExecutorA

#from tools import search_tool, wiki_tool, save_tool

load_dotenv()

#import httpx
#httpx_client = httpx.Client(verify=False)  # Disable SSL verification
#llm = ChatOpenAI(http_client= httpx_client, model="gpt-4o-mini", temperature=0, api_key="OPENAI_API_KEY") 

llm = ChatOpenAI(model="gpt-4", temperature=0, api_key="OPENAI_API_KEY") # Currently blocked by firewall 
#llm2 = ChatAnthropic(model="claude-2", temperature=0, api_key="ANTHROPIC_API_KEY") # Currently blocked by firewall

response = llm.invoke("What is the capital of France?")
print(response)