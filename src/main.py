#!/usr/bin/env python
import sys
from crew import WebscraperCrew
import agentstack
import agentops

from agentops.enums import EndState
from dotenv import load_dotenv
import os


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
agentops_api_key = os.getenv("AGENTOPS_API_KEY")
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

print("Environment variables loaded:", 
      "OPENAI_API_KEY" if openai_api_key else "❌",
      "AGENTOPS_API_KEY" if agentops_api_key else "❌",
      "FIRECRAWL_API_KEY" if firecrawl_api_key else "❌")


agentops.init(default_tags=agentstack.get_tags())

session = agentops.init(api_key=os.getenv('AGENTOPS_API_KEY'))

instance = WebscraperCrew().crew()

def run():
    """
    Run the crew.
    """
    instance.kickoff(inputs=agentstack.get_inputs())
    session.end_session(EndState.SUCCESS)


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        instance.train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=agentstack.get_inputs(), 
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        instance.replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    try:
        instance.test(
            n_iterations=int(sys.argv[1]), 
            openai_model_name=sys.argv[2], 
            inputs=agentstack.get_inputs(), 
        )
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


if __name__ == '__main__':
    run()