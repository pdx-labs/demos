# Practice Test Question Generator

This practice test question generator uses the pdx library to generate practice test questions based 
on the topic that you choose and the content that you provide the generator in a .txt file. The demo
also generates an answer to the question as well as reasons that support the answer.

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
Once you have installed the library in your local environment, clone this demos repository to your
local environment. 

Windows: Use the following command to clone the repository:
```bash
git clone https://github.com/pdx-labs/demos.git
```
After cloning the repository, add this folder "demos" containing the demos to the pdx library folder

## Compilation
Open a new terminal and open the pdx library. Once you are in the library, go to the following folder
to run the demo:

```bash
cd Test_Question_Generator
```
To check that the folder contains the agent.py file, you can run the following command
```bash
dir
```
The expected output should show that agent.py file is one of the existing files in the directory

You will also need to set the file path of the agent in the agent.py file. To do this,
open the agent.py file and edit the folder path in line 19 to be your path to the directory.
Code should look something like this:

```
my_agent = Agent(folder_path="C:\\Users\\User\\demos\\Test_Question_Generator"
                 , api_keys=api_keys)
```

## Content Information
> config.yaml:
>> The configuration file contains information about the model to execute the prompts and the
>> templates used to create the output. For this specific demo, text-davinci-003 will be used. The template
>> that will be used to format the prompt will be test_prompt.jinja

> agent.py:
>> This is agent that processes the user input (topic and content) and outputs the topic of interest and the questions, answers, and reasons generated based on the topic of interest and content provided by the user. This is the file where users will input their topic
of interest as well as the absolute file path for that topic to provide the model with information to generate the sample questions.
The user input will be done in lines 22 and 23 using the following code:
```
topic = 'YOUR_TOPIC'
file_path = 'YOUR_PATH\\example_content.txt'

> Templates
>> test_prompt.defaults.yaml:
This YAML file contains the default inputs for the template. The topic input is set default to Semiconductors
and the content section is information copied from a website about solar cells. The default also contains
a link to the website containing the information. This default section does not matter when you enter in your own
topic of interest and content to generate questions and answers.

>> test_prompt.jinja:
This jinja file contains the prompt template used to guide the model about the action and formating of the
output. In this case, the prompt tells the model to create 5 test questions with answers and reasoning based
on the topic and content that the user inputs.

> example_content.txt:
>>This .txt file contains an example of what the content you want to include can look like. The example
is about MOSFET devices. Note that this is just an example file that you can run if you don't have any
of your own content that you want to run. You can replace the content in this given file to provide your
own desired content. You can also select any txt file you want as long as you set the file_path in the agent.py
file to the absolute path of that file.

> tests
>> test_1.yaml:
This is a YAML test file that contains all of the tests for testing and debugging the prompt templates.

## Run Demo
Before running the demo, you need to open up a terminal and set your api key, where you plan to run your script.
Use the following command in your terminal with your own API key:
NOTE: This command is specific to Windwos. Use the command for your own operating system.
```
set OPENAI_KEY=<Enter your API Key without the triangular brackets>
```
Once you have selected your desired topic and set your API key, you can use the following command to run the script:

NOTE: Make sure that you are in the same directory as the agent.py file when running the command to run the script.
```
python agent.py
```
Example Output:

Topic: Mosfets

{

    "Question 1: What is a MOSFET?",
    
    "Answer 1": "A metal–oxide–semiconductor field-effect transistor (MOSFET, MOS-FET, or MOS FET) is a field-effect transistor (FET with an insulated gate) where the voltage determines the conductivity of the device.",
    
    "Reasons": [
        
        "It is used for amplifying or switching electronic signals.",
       
        "MOSFETs are now widely used in digital and analog circuits.",
       
        "It consists of three layers: a gate, dielectric, and substrate."
    
    ]

}

{
    
    "Question 2: What is the energy-band diagram of a MOS capacitor with a p-type substrate under a zero bias?",
    
    "Answer 2": "The energy bands in the semiconductor are flat indicating there is no net charges including interface exists in the semiconductor.",
    
    "Reasons": [
    
        "The ideal energy-band diagram of the MOS capacitor with a p-type substrate under a zero bias shows the energy bands in the semiconductor are flat.",
        
        "This indicates there is no net charges including interface exists in the semiconductor.",
        
        "The energy band is not bent upwards or downwards."
        
    ]
    
}


{

    "Question 3: What is the effect of a negative gate bias with respect to the semiconductor substrate?",
    
    "Answer 3": "The holes in the semiconductor will be attracted to the interface between semiconductor and oxide, forming an accumulative layer.",
    
    "Reasons": [
    
        "The bias bends the energy band upwards.",
        
        "This results in the valence-band edge being closer to Fermi level at the oxide-semiconductor interface than in the bulk material.",
        
        "This implies that there is an accumulation of holes."
        
    ]
    
}


{

    "Question 4: What is the effect of a positive gate bias with respect to the semiconductor substrate?",
    
    "Answer 4": "The holes in the semiconductor will be expelled away from the interface between semiconductor and oxide, forming a depletion layer.",
    
    "Reasons": [
    
        "The bias bends the energy band downwards.",
        
        "This results in the intrinsic Fermi level being closer to Fermi level at the oxide-semiconductor interface than in the bulk material.",
        
        "This implies that there is a space charge region formed."
    ]
}

{

    "Question 5: What are the four basic MOSFET device types?",
    
    "Answer 5": "Both the p-channel and the n-channel MOSFETs are available in two basic forms, the Enhancement mode and the Depletion mode.",
    
    "Reasons": [
    
        "The p-channel and the n-channel MOSFETs are both available in two basic forms.",
        
        "The Enhancement mode requires a Gate-Source voltage, (𝑉𝐺𝑆) greater than the threshold vo   ltage (𝑉𝑡ℎ) level to switch the device “ON”.",
        
        "The Depletion mode requires the Gate-Source voltage, (𝑉𝐺𝑆) to switch the device “OFF”."
        
    ]
    
}
## Contributions
Feel free to provide feedback or open an issue if there are any concerns/bugs with the code.






