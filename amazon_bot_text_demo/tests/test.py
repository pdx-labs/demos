from pdx import Agent
import os
from pydantic import BaseSettings

# Set the environment variable for the OpenAI API key
os.environ['openai_key'] = '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'

# Retrieve the API key
API_KEY = os.environ.get('Openai_key')

# Instantiate the Agent object
my_agent = Agent(folder_path="/Users/heejin/Desktop/pdx/pdx/demos/amazon_bot_text_demo")

#Change the question you want to ask over here
question="Can i use this air fryer in England?"

if __name__ == '__main__':
    _response_1 = my_agent.execute({
        "air_fryer_prompt": {
            'question': question
        }
    })
    _response_2 = my_agent.execute({
        "air_fryer_prompt": {
            'content': _response_1
        }
    })

print(question)
print(_response_2)