import os
from pdx import Agent
from pdx.settings import Keys

# Set up the api key using your own API key using the command "set API_KEY=your_api_key"
# for WINDOWS operating system in command prompt terminal and then retrieve key
api_key = os.environ.get('API_KEY')
api_keys = Keys(openai_key=api_key, anthropic_key=None, cohere_key=None)

# Instantiate the agent
my_agent = Agent(folder_path="YOUR_PATH\\demos\\YoutubeVideo", api_keys=api_keys)

#User input: user can enter in any topic they want to generate a youtube title and script about that topic
topic = "Neural Networks"

# Processes user input and provides output
if __name__ == '__main__':
    title_response = my_agent.execute({
        "title_template": {
            "topic": topic
        }
    })

    script_response = my_agent.execute({
        "script_template": {
            "script": title_response
        }
    })

# Print title and the script
print(f"Topic: {topic}")
print(script_response)