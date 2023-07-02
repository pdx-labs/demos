import os
from pdx import Agent
from pdx.settings import Keys

openai_key = os.environ.get("OPENAI_KEY")
api_keys = Keys(openai_key=openai_key)


# Instantiate the Agent object
agent_folder_path = os.path.dirname(__file__)
amazon_product_agent = Agent(path=agent_folder_path, api_keys=api_keys)


if __name__ == '__main__':
    question = "Can I use this in England?"
    _response = amazon_product_agent.execute({
        "air_fryer_prompt": {
            'question': question
        }
    })
    print(question)
    print(_response.completion)
