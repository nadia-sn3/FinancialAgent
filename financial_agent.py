from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv() # Loads environment variables from .env file

# Create the agent
finance_agent = Agent(
    name = "Finance Agent",
    description = "Your task is to find the financial information.",
    model = Groq(id="llama-3.3-70b-versatile"), # Using Groq's Llama 3 70B model
    tools = [YFinanceTools(
        stock_price=True, # Enable stock price lookups
        analyst_recommendations=True, # Enable analyst data
        company_info=True, # Enable company information
        company_news=True)], # Enable company news
    instructions = ["Use tables to display the data."],
    show_tool_calls = True,  # Makes the agent transparent about its process
    markdown = True, # Enables rich formatting in responses
    debug_mode = True # Helps with troubleshooting
)