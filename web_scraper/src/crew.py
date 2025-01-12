from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools

@CrewBase
class WebscraperCrew():
    """web_scraper crew"""

    # Agent definitions
    @agent
    def alex(self) -> Agent:
        return Agent(
            config=self.agents_config['alex'],
            tools=[tools.file_read_tool, tools.web_scrape, tools.web_crawl, tools.
    retrieve_web_crawl],  # Pass in what tools this agent should have
            verbose=True,
            
        )

    @agent
    def web_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['web_scraper'],
            tools=[tools.web_scrape, tools.web_crawl, tools.retrieve_web_crawl], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            tools=[tools.web_scrape, tools.web_crawl, tools.retrieve_web_crawl], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
        )

    # Task definitions
    @task
    def hello_world(self) -> Task:
        return Task(
            config=self.tasks_config['hello_world'],
        )

    @task
    def web_scraper_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_scraper_task'],
        )

    @task
    def summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizer_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
        )