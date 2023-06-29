import os
from pdx import Agent

agent_path = os.path.dirname(__file__)
sentiment_classification_agent = Agent(agent_path)
