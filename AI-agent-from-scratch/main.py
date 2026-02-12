

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

# # parser to parse response object
# parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Prompt template - creates a chat prompt template from a variety of message formats
# prompt = ChatPromptTemplate.from_messages(
#     [
#         #system prompt telling the agent what its function is and how to response to a reqsearch query
#         (
#             "system",
#             #""" --> Allow text to span multiple lines
#             """ 
#             You are a research assistant that will help generate a research paper.
#             Answer the user query and use neccessary tools. 
#             Wrap the output in this format and provide no other text\n{my_format_instructions}
#             """,
#         ),

#         # the next three fields will be populated automatically when the agent runs
#         # ("placeholder", "{chat_hisytory}"), # will be populated automatically when the agent runs
#         # ("human", "{query}"), # will be populated automatically when the agent runs
#         # ("placeholder", "{agent_Scratchpad}"), # will be populated automatically when the agent runs
#     ]
# ).partial(my_format_instructions=parser.get_format_instructions)

system_prompt = "You are a research assistant that will help generate a research paper. Answer the user query and use neccessary tools. Ensure the output conforms to the provided schema."

prompt = ChatPromptTemplate.from_messages([
        #system prompt telling the agent what its function is and how to response to a reqsearch query
        ("system", system_prompt),
        ("human", "{query}")
    ])




# convert teh llm output to be structured
llm = llm.with_structured_output(ResearchResponse)
chain = prompt | llm

raw_response = chain.invoke({"query":"What is the capital of Zimbabwe"})
print(raw_response)

## *** --> need to work on how to create_agent with system_prompt and tools, and how to invoke the agent with a query.***
# # Creates a simple agent & set-up the agent-executor under the hood 
# agent = create_agent(
#     model = llm,
#     system_prompt = prompt,
#     tools = []
# )


# #invoke the agent
# raw_response = agent.invoke({"query":"What is the capital of Zimbabwe"})

#response = llm.invoke("What is the capital of France?")
#print(response)