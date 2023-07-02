import os
from pdx import Agent
from pdx.settings import Keys

# Set up the api key using your own API key using the command "set API_KEY=your_api_key"
# for WINDOWS operating system in command prompt terminal and then retrieve key
api_key = os.environ.get('OPENAI_KEY')
api_keys = Keys(openai_key=api_key, anthropic_key=None, cohere_key=None)

# Instantiate the new Agent function
# The folder path should correspond to the directory containing the config.yaml file
my_agent = Agent(folder_path="YOUR_PATH_TO_DIRECTORY\\demos\\Best_Computer_Generator"
                 , api_keys=api_keys)

# User input: The user can enter in a job title, so the agent will output the
# type of computer best suited for the job and give me link or website to buy from.
job = 'Big Data Developer'

# Main function that processes input and outputs the responses from the templates
if __name__ == '__main__':
    response_1 = my_agent.execute({
        "product_prompt": {
           "job_title" : job
        }
    })

    product_response = my_agent.execute({
        "product_info_prompt": {
            "information": response_1
        }
    })

# Prints out the job title and response
print(f"Job Title: {job}")
print(product_response)
print("Warning:")
print("Do not solely base your purchase on the response from this demo since it is just a generalized response from an AI model.")
print("Make sure to do your own research about the computer suggested in the response before purchasing.")
print("Additionally, if there are specific requirements you need in your computer, please do your own research as well to determine the best computer suited for your needs.")