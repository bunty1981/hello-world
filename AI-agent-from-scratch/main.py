

from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent

#from langchain_core.tools import search_tool, wiki_tool, save_tool

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

# class for how we'd like the response from the LLM to be structured
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

system_prompt = """You are a research assistant that will help generate a research paper. 
    Answer the user query and use neccessary tools. 
    Ensure the output conforms to the provided schema."""

prompt = ChatPromptTemplate.from_messages([
        #system prompt telling the agent what its function is and how to response to a reqsearch query
        ("system", system_prompt),
        ("placeholder", "{chat_History}"), # If using memory
        ("human", "{query}"),
        ("placeholder", "{agent_Scratchpad}"), # REQUIRED
    ])


## USAGE using a chain with a sturctured output model to test the prompt and llm are working together as expected
# convert the llm output to be structured
structured_llm = llm.with_structured_output(ResearchResponse)
# create a simple chain to test the prompt and llm are working together as expected
chain = prompt | structured_llm
raw_response = chain.invoke({"query":"What is the capital of Zimbabwe"})
print("Response from Chain: ", raw_response)

##USAGE using an agent to test the prompt and llm are working together as expected, and to show how we can use the agent-executor under the hood without needing to set it up ourselves
# Creates a simple agent & set-up the agent-executor under the hood 
agent = create_agent(
    model = llm,
    system_prompt = system_prompt,
    response_format = ResearchResponse, #Uses LLM ProviderStartegy by default to convert the LLM output to be structured, but can also use a custom output parser if needed
    tools = []
)

#invoke the agent
query = "What is the capital of France?"
raw_response = agent.invoke(
    {"messages": [{"role": "user", "content": query}]}
)
print("Response from Agent: ", raw_response)

