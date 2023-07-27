import os
from pdx import Agent

# If not setting the key in the environment, you can set it here
# os.environ["OPENAI_KEY"] = "api-key-for-openai"

# Instantiate the Agent object
agent_folder_path = os.path.dirname(__file__)
amazon_product_agent = Agent(path=agent_folder_path)

if __name__ == '__main__':

    question = "Can I use this in England?"
    _response = amazon_product_agent.execute({
        "air_fryer_prompt": {
            'question': question
        }
    })
    print(question)
    print(_response.data)
