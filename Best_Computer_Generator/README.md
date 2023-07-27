# Best Computer To Buy Based on Job Title

This demo uses the pdx library and OpenAI chat model to give a computer recommendation that is best suited for your job, the computer specifications that make it best for the specific job input, and the reviews about the given computer.

## Installation

### Install PDX

In your local Python environment, install `pdx`:

```bash
pip install pdx
```

More information about [PDX here](https://pdxlabs.io/docs/getting-started/introduction).

### Get the demo

Please feel free to clone this repository of demos to your own local environment.

> Get your own OpenAI key

Click [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) to create your secret api key.

## Compilation

Make sure have all the code necessary for this demo (for instance by downloading it).

To double check the files:

```bash
dir
```

The expected output should show that the agent.py file as one of the existing files

## Content Information
### `agent.py`

This is the python script file that processes the user input (job) and outputs the best computer for the specific job title that
the user inputs with the reasons and reviews about why it is the best computer. You can type your user input following this code
in line 13, where you can enter your job title:

```
job = "YOUR_JOB"
```

### job_description_generator Folder

`**config.yaml**`
This configuration file contains information about the agent used to generate a job description and what computer specifications are necessary for a specific job. This file contains the name of the agent, the agent description, the LLM model used by the agent (gpt-3.5-turbo), and the prompt templates used by the agent (job_description.jinja).

`**__init__.py**`
This python file creates the agent used to generate a job description and specific computer needs in this job. This agent is called in the agent.py file when using this product in real-life scenarios.

### computer_specifications_generator Folder

`**config.yaml**`
This configuration file contains information about the agent used to generate a computer recommendation best suited for a specific job, the computer specifications, and reviews about the product. This file contains the name of the agent, the agent description, the LLM model used by the agent (gpt-3.5-turbo), and the prompt templates used by the agent (product_info.jinja).

`**__init__.py**`
This python file creates the computer_specifications_agent, which is formally called from the agent.py file when using this product in real-life scenarios.

### Templates

`**job_description.defaults.yaml**`
This YAML file contains the default input teacher, but if you have a job title input, this can be disregarded as
the agent file will give priority to the input made in the file.

`**job_description.jinja**`
This jinja file contains the prompt template used to guide the model to generate a job description and specify the computer needs required for a specific job input made by the user.

`**product_info.defaults.yaml**`
This YAML file contains the default job and information inputs. The default job is a teacher and the default information is regarding the computer requirements for a teacher. These default values can be disregarded as long as the user inputs a job title in the agent.py file

`**product_info.jinja**`
This jinja file guides the model about the actions taken and formatting to generate an output. This file takes in the information previously generated from the first agent (job description/computer needs) and writes an output in the JSON format about a computer recommendation, the specifications of the computer, and the reviews of the computer as a product.

## Testing

`**test_1.yaml**`
This is a YAML test file contains user inputs used for testing and debugging the prompt templates.

## Run Demo
Before running the demo, you need to open up a terminal and set your api key, where you plan to run your script.

Use the following command in your terminal with your own API key:

NOTE: The following command is for Windows operatig system. Use specific command to set the API key based on your computer's oeprating system.
```
set OPENAI_KEY=<Enter your API Key without the triangular brackets>
```
Once you have all the correct user inputs and set your API key, you can use the following command to run the script:

NOTE: Make sure that you are in the same directory as the agent.py file when running the command.
```
python agent.py
```
Example Output:

Job Title: Graphic Designer
{
    "Computer Recommendation": "Apple MacBook Pro",
    "Computer Specifications": [
        "High-performance computer with a fast processor",
        "Ample RAM (8GB or more)",
        "Dedicated graphics card",
        "Compatible with macOS",
        "Access to Adobe Creative Cloud software",
        "Color-calibrated monitor with accurate color representation",
        "Drawing tablet for digital illustrations",
        "Sufficient storage space with SSD and external hard drives or cloud storage",
        "Reliable and fast internet connection"
    ],
    "reviews": [
        "Review 1: The MacBook Pro is a powerful machine that can handle large files and complex software. The fast processor and ample RAM ensure smooth performance.",
        "Review 2: The color accuracy of the MacBook Pro's display is excellent, making it ideal for graphic designers who need to ensure their designs appear as intended.",
        "Review 3: The MacBook Pro's compatibility with macOS and Adobe Creative Cloud software makes it a popular choice among graphic designers.",
        "Review 4: The MacBook Pro's SSD provides fast storage access, while the option to expand storage with external hard drives or cloud storage ensures sufficient space for large 
files.",
        "Review 5: The MacBook Pro's reliable and fast internet connection allows graphic designers to easily collaborate with clients or team members and download/upload large files."    ]
}
Warning:
Do not solely base your purchase on the response from this demo since it is just a generalized response from an AI model.
Make sure to do your own research about the computer suggested in the response before purchasing.
Additionally, if there are specific requirements you need in your computer, please do your own research as well to determine the best computer suited for your needs.

## Contributions
Feel free to provide feedback or open an issue if there are any concerns/bugs with the code.