# Second_hand_car_choice_demo

This demo utilizes the pdx library to provide a recommendation system on second car choice, including the model, year, miles and possible insuracnce payment per year.



## Installation

### Install PDX

In your local Python environment, install `pdx`:

```bash
pip install pdx
```

More information about [PDX here](https://pdxlabs.io/docs/getting-started/introduction).

### Get the demo

Please feel free to clone this reposiroty of demos to your own local environment.

> Get your own OpenAI key

Click [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) to create your secret api key.

## Compilation

Make sure have all the code necessary for this demo (for instance by downloading it).

To double check the files:

```bash
cd second_hand_car_choice
ls
```

and the expected output contains

```python
car_rec_agent   insurance_agent run.py
```

Yayy, you are on the right spot!

## Car_rec_agent Content Explaination

Now, let us look through the files in this demo folder.

> 0_system.defaults.yaml

The contents over this default file is copied from a second_hand_car webpage regarding to Used 2019 Hyundai Sonata SE, so our AI model will output responses based on the default content. This file contains car model, price, mile, top features, and awards link.

> 0_system.jinja

This is a template file to provide template for the output. When we choose to input a question for the AI, this template will limit the output to one answer, a list of facts including price, production year, color, miles, other traits and driver's age. The prompt also contains chain of thought in the prompting as it consider the factors "step by step."

>1_user.jinja

It is the question file input to the model as I list my training question: "I am a female driver, budget is 20000 us dollar and looking for a small car, it is better produced after 2017. I only drive the car in california, not in snowy days. I prefer Audi, Hyundai. It must have no demage reported."

>1_assitant.jinja

It is the my desired answer for the question contained in 1_user.jinja with the template contained in 0_system.jinja

>2_user.defaults.yaml

It is the default question listed for the 2_user, the question user should input,in case user did not provide enough information.

>2_user.jinja

in the double bracket, the question will be replace by the question in init.py file. This is just a template for input

> config.yaml

This is the configuration file for us to choose the model for messages and the template for output. We choose to use gpt-3.5-turbo since we are using chat agent demo.
The prompt template is using system-user1-assitant1-user2 as the picture showing below. I feed the system using user_1 and the assitant's answer_1, looking for it can take two files into analysis.


<img width="367" alt="Screen Shot 2023-07-11 at 10 28 16 PM" src="https://github.com/AnnabelleMin/pdxdemos/assets/113308586/07e0e54f-f605-4710-aa21-235b183ba6b6">

> test_1.yaml

This is the test in the local to see if the agent is running as expected.

> __init__.py

This is a test file for us to input our question into thie file.

In line 15, there is a line:

```
question='I am a female driver ageo 20, budget is 50000 US dollar and looking for a sedan, it is better produced after 2020. I need to drive this car in snowy days.  I prefer Lexus, Mercedes benz.'
```

We can change this line to change the question and the program will provide us different outputs based on the input and implement in the applications.

## Insurance_agent Content Explaination

Now, let us look through the files in this demo folder.

> 0_system.defaults.yaml

The contents over this default file is copied from a second_hand_car webpage regarding to Used 2019 Hyundai Sonata SE, so our AI model will output responses based on the default content. This file contains car model, price, mile, top features, and awards link.

> 0_system.jinja

This is a template file to provide template for the output. When we choose to input a question for the AI, this template will limit the output to one answer, a list of facts including market price,production year, models, miles and drivers' age. The prompt also contains chain of thought in the prompting as it consider the factors "step by step."

>1_user.jinja

It is the question file input to the model as I list my training question,which is exactly the output for car_rec_agent.

>1_assitant.jinja

It is the my desired answer for the question contained in 1_user.jinja with the template contained in 0_system.jinja

>2_user.defaults.yaml

It is the default question listed for the 2_user, the question user should input,in case user did not provide enough information.

>2_user.jinja

in the double bracket, the question will be replace by the question in init.py file. This is just a template for input

> config.yaml

This is the configuration file for us to choose the model for messages and the template for output. We choose to use gpt-3.5-turbo since we are using chat agent demo.
The prompt template is using system-user1-assitant1-user2 as the picture showing below. I feed the system using user_1 and the assitant's answer_1, looking for it can take two files into analysis.


<img width="367" alt="Screen Shot 2023-07-11 at 10 28 16 PM" src="https://github.com/AnnabelleMin/pdxdemos/assets/113308586/07e0e54f-f605-4710-aa21-235b183ba6b6">

> test_1.yaml

This is the test in the local to see if the agent is running as expected.

> __init__.py

This is a test file for us to input our question into thie file.

In line 15, there starts a line for question under {}:

```
_question= {
    "answer": "2021 Lexus ES 350",
    "facts": [
        "price : $45,995",
        "production year : 2021",
        "color: silver",
        "miles: 10,000",
        "other traits: All-Wheel Drive, Heated Seats, Navigation System, Sunroof/Moonroof, Backup Camera, Bluetooth, Leather Seats, Alloy Wheels, Blind Spot Monitoring, Parking Sensors, Premium Package",
        "driver age: 20",
    ]
}
```
The question is closed by {} and the content in the question is exactly the output of car_rec_agent!
We can change this line to change the question and the program will provide us different outputs based on the input and implement in the applications.
## Testing

We use test_1.yaml file to run test in local environment to make sure it works in local environment.

First change your directory into each agent files.

If you are running Mac OS/ linux, type below in your terminal:

```
export OPENAI_KEY="your secret key"
```

Next,type below in the terminal:

```
pdx test <RELATIVE PATH TO YOUR AGENT> --verbose
```

Now you will see in your terminal,test_1 is running!

## Explaination on run.py

Here, we import the two agents created from their own files. The question in line 6 can be modified based on user's need.
Then, we first execute car_rec_agent and print their response. Next, we pass in the response and take it as a question to the insurance_agent, then print out the insurance_agent response.

## Coding Samples

How can we run the code?

First, make sure that you are in the test directory.

Second, type in your API key in terminal.

If you are running Mac OS/ linux, type below in your terminal:

```
export OPENAI_KEY="your secret key"
```

Third, type the following in your local terminal:

```
python run.py
```

If you are in Mac and the above code report error, please try

```
python3 run.py
```

And wait for 30 seconds, you should have your output in your terminal!

For example, if the question is still

The output I generated is

```
Based on the given information, the estimated insurance price range for a 2019 Hyundai Sonata SE with a market price of $15,495 and 80,390 miles is $839-1571 per year. The driver's age of 30 also contributes to a relatively lower insurance price.
{
    "answer": "2019 Hyundai Sonata SE",
    "facts": [
        "price : $15,495",
        "production year : 2019",
        "color: white",
        "miles: 80,390",
        "other traits: ABS brakes, Alloy wheels, Electronic Stability Control, Illuminated entry, Low tire pressure warning, Remote keyless entry, Traction control. ",
        "driver age: 30",
        "estimated insurance price range: $839-1571 per year"
    ]
}
```




## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
