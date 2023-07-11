import os
from pdx import Agent
from pdx.settings import Keys
from job_description_generator import job_description_agent
from computer_specifications_generator import computer_specifications_agent

# Set up the api key using your own API key using the command "set OPENAI_KEY=your_api_key"
openai_key = os.environ.get('OPENAI_KEY')
api_keys = Keys(openai_key=openai_key)

# Main function that processes input and outputs the responses from the templates
if __name__ == '__main__':
    job = 'Big Data Developer'
    _job_info = job_description_agent.execute({
        "job_description": {
           "job": job
        }
    })

    _computer_info = computer_specifications_agent.execute({
        "product_info": {
            "information": _job_info
        }
    })

# Prints out the job title and response
print(f"Job Title: {job}")
print(_computer_info.completion)
print("Warning:")
print("Do not solely base your purchase on the response from this demo since it is just a generalized response from an AI model.")
print("Make sure to do your own research about the computer suggested in the response before purchasing.")
print("Additionally, if there are specific requirements you need in your computer, please do your own research as well to determine the best computer suited for your needs.")