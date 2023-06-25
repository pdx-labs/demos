# Youtube Video Title and Script Generator

This demo uses the pdx library to generate generate a youtube video title and script based on the topic you input.

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
cd Vivian_demos\demos\YoutubeVideo\tests
```
To check that the folder contains the script, you can run the following command
```bash
dir
```
The expected output should show that the script.py is in the folder

## Content Information
> config.yaml:
>> The configuration file contains information about the model to execute the prompts and the
>> templates used to create the output. For this specific demo, gpt-3.5-turbo will be used, which is an
>> OpenAI chat model. The template that will be used to format the title and script prompt will be title_template.jinja and script_template.jinja.

> Templates
>> title_template.defaults.yaml:
This YAML file contains the default inputs for the title prompt template. The topic input is set default to "Artificial Intelligence"

>> scipt_template.defaults.yaml:
>> This YAML file contains the default inputs for the script prompt template. The title input is set default to
>> "Understanding the Fundamentals of Artificial Intelligence".

>> title_template.jinja:
This jinja file contains the prompt template used to guide the model about creating a youtube video title based on the
>> topic chosen by the user.

>> script_template.jinja:
This jinja file takes in the title created by the model automatically and writes a youtube video script based on
>> the outputed title. Therefore, all the user needs to do is enter the main topic of the youtube video.

> tests
>> script.py:
This is the script that will be run and where you can enter your own topic of interest in line 14 using the
following code:
```
topic = "<ENTER_YOUR_DESIRED_TOPIC>"
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
python script.py
```
Example Output (User input: Neural Networks):

Topic: Neural Networks

Title: "Neural Networks: The Future of Artificial Intelligence"

Script:

Introduction:
Hello everyone, welcome back to our channel. Today, we're going to talk about one of the most exciting and promising fields of artificial intelligence - Neural Networks.

What are Neural Networks?
Neural Networks are a set of algorithms that are designed to recognize patterns and learn from data. They are modeled after the structure and function of the human brain, with interconnected nodes that process information and make decisions.

How do Neural Networks work?
Neural Networks work by processing large amounts of data through layers of interconnected nodes. Each node receives input from the previous layer and applies a mathematical function to it, before passing it on to the next layer. This process continues until the output layer produces a result.

Applications of Neural Networks:
Neural Networks have a wide range of applications, from image and speech recognition to natural language processing and predictive analytics. They are used in self-driving cars, virtual assistants, fraud detection systems, and many other areas.

Advantages of Neural Networks:
One of the biggest advantages of Neural Networks is their ability to learn and adapt to new data. They can improve their accuracy and performance over time, without the need for explicit programming. They are also highly parallelizable, which means they can process large amounts of data quickly and efficiently.

Challenges and Future of Neural Networks:
Despite their many advantages, Neural Networks still face some challenges, such as overfitting, bias, and interpretability. However, researchers are working on developing new techniques and algorithms to address these issues. The future of Neural Networks looks bright, with new applications and breakthroughs on the horizon.

Conclusion:
In conclusion, Neural Networks are a fascinating and powerful tool for artificial intelligence. They have the potential to revolutionize many industries and improve our lives in countless ways. We hope you enjoyed this video and learned something new. Don't forget to like and subscribe for more content 
like this. Thank you for watching!

## Contributions
Feel free to provide feedback or open an issue if there are any concerns/bugs with the code.






