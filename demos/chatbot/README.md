# Best Computer To Buy Based on Job Title

This demo uses the pdx library and OpenAI chat model to tell you what type of computer to buy,
details about the computer and the reviews corresponding why the given computer it best
based on the inputed job title.

## Installation
Before installing the pdx library, ensure that you are using the latest version of python (3.11.4).
> Python Upgrade/Installation

Check the python version using the following command:
```bash
python3 --version
```
The preferable version of python is:
``` Python 3.11.4
```
Install the latest version of python from the following link if you have not done so using the
following link: https://www.python.org/downloads/

> Install pdx library and dependencies

Clone the repository containing the pdx library from the following link: https://github.com/pdx-labs/pdx

Windows: Use the following commands to clone and install the pdx library and dependencies:
```bash
git clone https://github.com/pdx-labs/pdx.git
cd pdx
pip install pdx
pip install .
```
Once you have installed the library in your local environment, clone this forked repository to your
local environment. 

Windows: Use the following command to clone the repository:
```bash
git clone https://github.com/vxw8/Vivian_demos.git
```
After cloning the repository, add this folder "Vivian_demos" containing the demos to the pdx library folder

## Compilation
Open a new terminal and open the pdx library. Once you are in the library, go to the following folder
to run the demo:

```bash
cd Vivian_demos\demos\chatbot\tests
```
To check that the folder contains the script, you can run the following command
```bash
dir
```
The expected output should show that the script_2.py is in the folder

## Content Information
> config.yaml:
>> The configuration file contains information about the model to execute the prompts and the
>> templates used to create the output. For this specific demo, gpt-3.5-turbo will be used, which is an
>> OpenAI chat model. The templates stated in the configuration are product_prompt.jinja, which asks the question
>> about which computer is best suited for the job title input. Then, the second template product_info_prompt.jinja will
>> take in the response executed by the first prompt and provide information about the computer in JSON format.

> Templates
>> product_prompt.defaults.yaml:
This YAML file contains the default input software developer, but if you have a job title input, this can be disregarded because
of the chat model being used.

>> product_info_prompt.defaults.yaml:
>> This YAML file contains the default input none for the information because the information about the computer changes
>> based on the response from the first prompt.

>> product_prompt.jinja:
This jinja file contains the prompt template used to tell the model to choose a computer best suited for the specific job
>> title inputed in by the user.

>> product_info_prompt.jinja:
This jinja file takes in the information from the first prompt and outputs information about a specific computer that
>> is good for the specific job title as well as reviews for that specific computer.

> tests
>> script_2.py:
This is the script that will be run and where you can enter the job title in line 17 using the
following code:
```
job_title = "<ENTER_YOUR_JOB_TITLE>"
```

## Run Demo
Before running the demo, you need to open up a terminal and set your api key, where you plan to run your script.
Use the following command in your terminal with your own API key:
```
set API_KEY=<Enter your API Key without the triangular brackets>
```
Once you have selected your desired topic and set your API key, you can use the following command to run the script:

NOTE: Make sure that you are in the tests folder when running the command.
```
python script_2.py
```
Example Output:

Job Title: college student
{

    "answer": "The best computer for a college student is the MacBook Air because of its portability, long battery life, and compatibility with educational software.",
    
    "facts": [
    
        "The MacBook Air is lightweight and easy to carry around campus.",
        
        "It has a battery life of up to 12 hours, making it ideal for long study sessions.",
        
        "Many educational software programs are designed specifically for Mac OS, making the MacBook Air a compatible choice for college students."  
        
    ],
    
    "reviews": [

        "I love my MacBook Air for college! It's so easy to carry around and the battery lasts all day.",
        
        "I've had my MacBook Air for three years now and it's still going strong. It's perfect for taking notes in class and doing homework.",
        
        "The MacBook Air is a bit pricey, but it's worth it for the quality and reliability. I highly recommend it for college students."
    ]
    
}


## Contributions
Feel free to provide feedback or open an issue if there are any concerns/bugs with the code.






