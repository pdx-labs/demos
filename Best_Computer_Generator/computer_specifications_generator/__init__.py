import os
from pdx import Agent 
from pdx.settings import Keys

openai_key = os.environ.get('OPENAI_KEY')
api_keys = Keys(openai_key=openai_key)

agent_folder_path = os.path.dirname(__file__)
computer_specifications_agent = Agent(agent_folder_path, api_keys=api_keys)