from langchain_community.llms import Ollama
from browser_use import Agent
import asyncio

# Initialize Ollama with the llama3.2:1b model
llm = Ollama(model="llama3.2:1b")

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
