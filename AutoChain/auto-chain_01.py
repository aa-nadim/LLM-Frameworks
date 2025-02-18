from autochain.agent import Agent
from autochain.llm.providers.ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2:1b") 

agent = Agent(llm=llm)
response = agent.run("What is AutoChain?")
print(response)