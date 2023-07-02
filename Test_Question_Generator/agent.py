import os
from pdx import Agent
from pdx.settings import Keys

# Set up the api key using your own API key using the command based on your device
# for WINDOWS operating system in command prompt terminal and then retrieve key
api_key = os.environ.get('OPENAI_KEY')
api_keys = Keys(openai_key=api_key, anthropic_key=None, cohere_key=None)

# Instantiate the new Agent function in the same folder as the config.yaml file
my_agent = Agent(folder_path='YOUR_PATH_TO_DIRECTORY\\Test_Question_Generator'
                 , api_keys=api_keys)

# Main function that processes user request
# User input: Select topic of interest
# This topic variable can be changed to any topic you desire as long as the content
# you enter matches the topic.
# Upload .txt file containing the topic information you want to create questions from
# file path: the absolute file path of the txt file containing information that is being read
if __name__ == '__main__':
    topic = 'Mosfets'
    file_path = 'C:\\Users\\User\\Vivian_demos\\Test_Question_Generator\\example_content.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    response = my_agent.execute({
        "test_prompt": {
           "topic" : topic,
           "content": content
        }
    })

# Prints the topic and the sample test questions generated
print(f"Topic: {topic}")
print(response)