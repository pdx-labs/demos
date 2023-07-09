import os
from pdx import Agent
from pdx.settings import Keys

# Set up the api key using your own API key using the command "set API_KEY=your_api_key"
# for WINDOWS operating system in command prompt terminal and then retrieve key
openai_key = os.environ.get('OPENAI_KEY')
api_keys = Keys(openai_key=openai_key)

# Instantiate the agent
agent_folder_path = os.path.dirname(__file__)
script_agent = Agent(agent_folder_path, api_keys=api_keys)
