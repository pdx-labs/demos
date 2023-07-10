# Travel Agent Bot

This travel agent bot uses the pdx library to help create an itinerary for your desired vacation. You can also customize your question based on your own needs so that the travel agent can assist you with your needs such as asking for a list of best vacations in your travel destination or hotel recommendations. The travel agent can also assist you in making recommendations about a vacation destination using your
own preferences.

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
dir
```

The expected output should show that agent.py file is one of the existing files in the directory.

## Content Information

### `config.yaml`

The configuration file contains information about the model to execute the prompts and the templates used to create the output. For this specific demo, gpt-3.5-turbo will be used. The template that will be used to format the prompt will be prompt.jinja

### `agent.py`

This is an agent that processes the user input (destination and trip duration) and outputs an itineray in a specific format (1_assistant format for that specific destination). This is the file where users can either create a travel itinerary for their desired destination or ask any travel-related questions regarding attractions, hotels or transportation. Currently, the question is formated so that you can only ask the travel bot to create a travel itinerary by only having to input your destination (needs to match the file name of the .txt file) and your trip duration. However, you can also ask any other travel-related question by uncommenting line 22 and commenting out line 21. 

To create a travel itinerary, the user input will be done in lines 13 and 14 using the following code:

```
destination = "paris_france"
trip_duration = "4"
```
To ask travel-related question, change the code in lines 21 and 22 as well as include your destination in line 13 using the following code:
```
destination = "hawaii"
# question = f"Create a {trip_duration}-day itinerary for my trip to {destination}."
question = f"Give me hotel recommendations for my vacation to {destination}. My budget is $350 per night."
```
NOTE: Above is a sample question about hotel recommendations from a certain destination including a budget for hotel per night.

To ask for destination recommendation based on your own vacation preferences, change the code in lines 21 - 23 using the following code:
```
# question = f"Create a {trip_duration}-day itinerary for my trip to {destination}."
# question = f"Give me hotel recommendations for my vacation to {destination}. My budget is $350 per night."
question = "Find me a destination suitable for a family-friendly vacation that is under my budget of $10,000 for a trip duration of 5-days. I am traveling from Seattle, WA."
```
### Templates

`**0_system.defaults.yaml**`

This YAML file contains the default inputs for the template. The destination input is an introduction to the travel agent. This default section does not matter when you enter your travel destination. If you do not include a destination, the default value will
tell the system to act as a travel agent to help with any travel-related questions.

`**0_system.jinja**`
This jinja file contains the prompt template used to guide the model about the action and formating of the
output. In this case, the prompt tells the model to assist the user in creating an itinerary for their specified travel destination or any other travel-related question based on their destination or destination recommendation based on vacation needs.

`**1_user.jinja**`
This jinja file contains a prompt template that shows an example of what type of question a user could ask the travel agent bot. In this case, the example is of a user asking to create a 3-day travel itinerary to Santorini, Greece. This is to help the model understand what type of question the user may ask.

`**1_assistant.jinja**`
This jinja file contains the prompt template that shows an example of what the travel agent's response may be when the user asks about creating a 3-day travel itinerary to Santorini, Greece. This helps improve the accuracy and gives consistent formatting for outputs made from the model for this specific type of question.

`**2_user.defaults.yaml.**`
This YAML file contains the default inputs for the user prompt template. This question input is a question about creating a travel itinerary for a trip to Paris, France. This default input does not matter if the user enters a question to ask the travel agent bot. However, if you do not include a question input, this default input will provide the agent with a question to produce an output.

`**2_user.jinja**`
This jinja file contains the prompt template used to guide the model about the user input. The user input is a travel-related question that the user will input in the python script file. 

`**destination.txt**`
Each of the .txt files that are named a following destination contain information regarding each destination. These files contains information from online that is inputed into the model to create an itinerary for a specific destination more accurately. If you want, you can also create additional .txt files for countries not listed as long as you name the .txt file in the format as the examples. The information within these .txt files are lists of attractions, hotels, and modes of transportation for that specific location. You can use any of the three existing files or create your own when running the agent.

### tests

`**test_1.yaml**`

This is a YAML test file that contains all of the tests for testing and debugging the prompt templates.

## Run Demo

Before running the demo, you need to open up a terminal and set your api key, where you plan to run your script.

Use the following command in your terminal with your own API key:

NOTE: This command is specific to Windows. Use the command for your own operating system.

```
set OPENAI_KEY=<Enter your API Key without the triangular brackets>
```

Once you have selected your desired topic and set your API key, you can use the following command to run the script:

NOTE: Make sure that you are in the same directory as the agent.py file when running the command to run the script.

```
python agent.py
```
Example Output:
```
User: Create a 4-day itinerary for my trip to paris_france.
Travel Agent Response:

Day 1: Exploring the City
Morning:
- Arrive at Paris and transfer to your hotel.
- Start your day with a visit to the iconic Eiffel Tower. Take in the panoramic views of the city from the top.

Afternoon:
- Visit the Musée d'Orsay, home to an impressive collection of French art including works by Monet and Van Gogh.
- Take a leisurely stroll along the Seine River and enjoy the beautiful architecture of the city.

Evening:
- Explore the charming neighborhood of Montmartre. Visit the Sacré-Cœur Basilica and enjoy the lively atmosphere of the area.
- Have dinner at a traditional French restaurant in Montmartre, such as Le Relais de la Butte or La Bonne Franquette.

Hotel for Day 1: Choose a hotel in the city center, such as Hotel de Crillon or Hotel Bourg Tibourg.

Day 2: Historical Landmarks
Morning:
- Visit the Louvre Museum, home to the famous Mona Lisa and other masterpieces. Spend the morning exploring the vast collection.

Afternoon:
- Explore the Notre-Dame Cathedral and take a guided tour to learn about its history and architecture.
- Visit the Sainte-Chapelle, known for its stunning stained glass windows.

Evening:
- Take a leisurely walk along the Champs-Élysées and enjoy the luxury shops and cafes.
- Have dinner at a restaurant on the Champs-Élysées, such as L'Avenue or Le Fouquet's.

Hotel for Day 2: Choose a hotel near the Louvre or Champs-Élysées, such as Hotel La Comtesse Tour Eiffel or Kimpton St Honore Paris.

Day 3: Palace and Gardens
Morning:
- Take a day trip to the Palace of Versailles. Explore the opulent palace and its beautiful gardens.
- Visit the Hall of Mirrors and learn about the history of the French monarchy.

Afternoon:
- Return to Paris and visit the Palais Garnier, the famous opera house. Take a guided tour to admire its grand architecture.

Evening:
- Enjoy a dinner cruise along the Seine River. Admire the illuminated landmarks of Paris while enjoying a delicious meal.

Hotel for Day 3: Choose a hotel near the Palace of Versailles or the Palais Garnier, such as Hotel de Neuville - Arc de Triomphe.

Day 4: Cultural Experiences
Morning:
- Visit the charming neighborhood of Le Marais. Explore the narrow streets, visit art galleries, and browse through boutique shops.

Afternoon:
- Take a boat tour along the Canal Saint-Martin. Enjoy the scenic views and pass through charming locks and bridges.

Evening:
- Visit the Latin Quarter and enjoy the vibrant atmosphere. Explore the historic streets and dine at a traditional French bistro.

Hotel for Day 4: Choose a hotel in Le Marais or the Latin Quarter, such as Hotel du Haut Marais or Hotel des Grandes Ecoles.

Transportation: The best way to get around Paris is by using the Paris metro and RER train system. Purchase a single or multi-day pass to easily access different 
attractions and neighborhoods. Buses are also a convenient option for getting around the city. Taxis and car services like Uber are available for more flexibility and convenience.

Note: This itinerary is just a suggestion, and you can customize it based on your preferences and the activities you're interested in. Make sure to check the operating hours and availability of attractions and restaurants before your trip. Enjoy your time in Paris!

```

## Contributions

Feel free to provide feedback or open an issue if there are any concerns/bugs with the code.