import os
from pdx import Agent
from pdx.settings import Keys

API_key=os.environ.get("OPENAI_KEY")
api_keys=Keys(openai_key=API_key, anthropic_key=None, cohere_key=None)


# Instantiate the Agent object
my_agent = Agent(folder_path="/CHANGE THIS TO YOUR PATH/amazon_bot_text_demo",api_keys=api_keys)


if __name__ == '__main__':
    question="Can I use this in England?"
    _response_1 = my_agent.execute({
        "air_fryer_prompt": {
            'question': question
        }
    })
    print(_response_1)

print(question)

