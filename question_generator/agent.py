import os
from pdx import Agent

# Set up the api key using your own API key using the command based on your device
# for WINDOWS operating system in command prompt terminal
# If not setting the key in the environment, you can set it here
# os.environ["OPENAI_KEY"] = "api-key-for-openai"

# Instantiate the new Agent function in the same folder as the config.yaml file
# This code snippet finds the directory name of this file.
agent_folder_path = os.path.dirname(__file__)
my_agent = Agent(agent_folder_path)

if __name__ == '__main__':
    # Main function that processes user request
    # User input: Select topic of interest
    # This topic variable can be changed to any topic you desire as long as the content
    # you enter matches the topic.
    # Upload .txt file containing the topic information you want to create questions from
    # file path: the absolute file path of the txt file containing information that is being read
    topic = 'Mosfets'
    content_file_path = os.path.join(agent_folder_path, 'topic_content.txt')
    with open(content_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    response = my_agent.execute({
        "prompt": {
            "topic": topic,
            "content": content
        }
    })

    # Prints the topic and the sample test questions generated
    print(f"Topic: {topic}")
    print(response.data)
