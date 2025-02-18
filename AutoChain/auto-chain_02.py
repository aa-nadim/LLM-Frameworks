import google.generativeai as genai
from autochain.chain.chain import Chain
from autochain.memory.buffer_memory import BufferMemory
from autochain.tools.base import Tool
from autochain.agent.conversational_agent.conversational_agent import ConversationalAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Google Gemini API
genai.configure(api_key=api_key)

class GeminiLLM:
    """Custom wrapper for Google Gemini to work with AutoChain"""
    def __init__(self, model="gemini-pro", temperature=0):
        self.model = genai.GenerativeModel(model)
        self.temperature = temperature

    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return {"content": response.text}  # Ensure the response is in the expected format

# Initialize Gemini as the LLM
llm = GeminiLLM()

# Define tools
tools = [
    Tool(
        name="Get weather",
        func=lambda *args, **kwargs: "Today is a sunny day",  # Replace with a real API call
        description="This function returns the weather information.",
    ),
    Tool(
        name="Get time",
        func=lambda *args, **kwargs: "It's 12:00 PM right now.",  # Replace with a real time function
        description="This function returns the current time.",
    ),
]

# Initialize memory and agent
memory = BufferMemory()
agent = ConversationalAgent.from_llm_and_tools(llm=llm, tools=tools)

# Create the chain
chain = Chain(agent=agent, memory=memory)

# Run queries
user_query = "what is the weather today"
print(f">> User: {user_query}")
print(f">> Assistant: {chain.run(user_query)['content']}")

next_user_query = "What time is it?"
print(f">> User: {next_user_query}")
print(f">> Assistant: {chain.run(next_user_query)['content']}")