import os
from pdx import Agent

# If not setting the key in the environment, you can set it here
# os.environ["OPENAI_KEY"] = "api-key-for-openai"

agent_path = os.path.dirname(__file__)
sentiment_classification_agent = Agent(agent_path)

if __name__ == '__main__':

    sentence = "This is a good movie."
    _response = sentiment_classification_agent.execute({
        "1_prompt": {
            'sentence': sentence
        }
    })
    print(sentence)
    print(_response.data)
