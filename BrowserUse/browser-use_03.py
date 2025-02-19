import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv

load_dotenv()
# llm = ChatOpenAI(model="gpt-4o")
api_key = os.getenv("GEMINI_API_KEY")
# Initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp", api_key=SecretStr(os.getenv("GEMINI_API_KEY"))
)
async def main():
    sensitive_data = {
        "xyz_name": "your@gmail.com",
        "xyz_password": "your_password",
    }
agent = Agent(
        task="""your prompt""",
        llm=llm,
        sensitive_data=sensitive_data,
    )

result = await agent.run()
print(result)
asyncio.run(main())
