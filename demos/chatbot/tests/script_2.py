import os
from pdx import Agent
from pdx.settings import Keys

# Set up the api key using your own API key using the command "set API_KEY=your_api_key"
# for WINDOWS operating system in command prompt terminal and then retrieve key
api_key = os.environ.get('API_KEY')
api_keys = Keys(openai_key=api_key, anthropic_key=None, cohere_key=None)

# Instantiate the new Agent function
# The folder path should correspond to the directory containing the config.yaml file
my_agent = Agent(folder_path="YOUR_PATH\\pdx\\demos\\chatbot"
                 , api_keys=api_keys)

# User input: User can enter in a job title, so the agent will output the
# type of computer best suited for the job and give me link or website to buy from.
job_title = "Data Engineer"

# Main function that processes input and outputs the responses from the templates
if __name__ == '__main__':
    response_1 = my_agent.execute({
        "product_prompt": {
           "job_title" : job_title
        }
    })

    product_response = my_agent.execute({
        "product_info_prompt": {
            "information": response_1
        }
    })

# Prints out the job title and response
print(f"Job Title: {job_title}")
print(product_response)