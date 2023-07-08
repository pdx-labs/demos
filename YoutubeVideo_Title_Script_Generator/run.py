import os
from pdx import Agent
from pdx.settings import Keys
from title_agent import title_agent
from script_agent import script_agent

# Set up the api key using your own API key using the command "set API_KEY=your_api_key"
# for WINDOWS operating system in command prompt terminal and then retrieve key
openai_key = os.environ.get('OPENAI_KEY')
api_keys = Keys(openai_key=openai_key)

#User input: user can enter in any topic they want to generate a youtube title and script about that topic

# Processes user input and provides output
if __name__ == '__main__':
    _topic = 'Deep Learning'
    _title_response = title_agent.execute({
        "title_template": {
            "topic": _topic
        }
    })

    _script_response = script_agent.execute({
        "script_template": {
            "script": _title_response
        }
    })

# Print title and the script
print(f"Topic: {_topic}")
print(_script_response.completion)