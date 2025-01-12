# ai
```bash

python3 -m venv .venv
source .venv/Scripts/activate

source .venv/bin/activate


pip install -r requirements.txt


pip install agentstack

agentstack init web_scraper

cd web_scraper

agentstack generate agent web_scraper

agentstack generate task web_scraper_task


agentstack generate agent summarizer

agentstack generate task summarizer_task


agentstack tools add firecrawl

agentstack run




```