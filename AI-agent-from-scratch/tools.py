from langchain_community.tools import Tool, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

# Tool built with duckduckgo-search, a replacement for the legacy duckduckgo-search package, which is no longer maintained and has compatibility issues with newer Python versions. The DuckDuckGoSearchRun tool uses the ddgs package to perform web searches and retrieve relevant information based on user queries.
search = DuckDuckGoSearchRun()
@tool
def search_tool(query: str) -> str: 
    """Search the web for information"""
    return search.run(query)

# Inbuilt wikipeadia tool from langchain, which uses the wikipedia-api package to fetch information from Wikipedia based on user queries. The WikipediaQueryRun tool is designed to retrieve concise summaries of Wikipedia articles, making it a valuable resource for obtaining quick and accurate information on a wide range of topics.
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
# @tool
# def wiki_tool(query: str) -> str:
#     """Search Wikipedia for information"""
#     return wiki_tool.run(query)

# Custom tool
def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

@tool
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """Saves structured research data to a text file."""
    return save_to_txt(data, filename)