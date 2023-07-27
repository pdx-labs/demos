import os
from pdx import Agent

# Instantiate the agent
agent_folder_path = os.path.dirname(__file__)
script_agent = Agent(agent_folder_path)
