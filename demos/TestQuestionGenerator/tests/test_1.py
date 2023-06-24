import os
from pdx import Agent
from pdx.settings import Keys

# Set up the api key using your own API key using the command "set API_KEY=your_api_key"
# for WINDOWS operating system in command prompt terminal and then retrieve key
api_key = os.environ.get('API_KEY')
api_keys = Keys(openai_key=api_key, anthropic_key=None, cohere_key=None)

# User input: Select topic of interest
# This topic variable can be changed to any topic you desire as long as the content
# you enter matches the topic
topic = "Solar Cells"

# Upload .txt file containing the topic information you want to create questions from
# file path: the absolute file path of the txt file containing information that is being read
file_path = 'YOUR_PATH\\pdx\\demos\\TestQuestionGenerator\\example_content.txt'
file = open(file_path, 'r', encoding='utf-8')
content = file.read()

# Instantiate the new Agent function in the same folder as the config.yaml file
my_agent = Agent(folder_path='YOUR_PATH\\pdx\\demos\\TestQuestionGenerator'
                 , api_keys=api_keys)

# Main function that processes user request
if __name__ == '__main__':
    response_1 = my_agent.execute({
        "test_prompt": {
           "topic" : topic
        }
    })

    sample_questions = my_agent.execute({
        "test_prompt": {
            "content": content
        }
    })

# Prints the topic and the sample test questions generated
print(f"Topic: {topic}")
print(sample_questions)