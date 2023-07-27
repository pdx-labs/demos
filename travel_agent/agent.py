import os
from pdx import Agent

agent_folder_path = os.path.dirname(__file__)
chat_agent = Agent(agent_folder_path)

if __name__ == '__main__':
    # destination input must be in the same format as the .txt file
    destination = "paris_france"
    trip_duration = "4"
    file_name = f"{destination}.txt"

    content_file_path = os.path.join(agent_folder_path, file_name)
    with open(content_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    question = f"Create a {trip_duration}-day itinerary for my trip to {destination}."
    # question = f"Give me hotel recommendations for my vacation to {destination}. My budget is $350 per night."
    # question = "Find me a destination suitable for a family-friendly vacation that is under my budget of $10,000 for a trip duration of 5-days. I am traveling from Seattle, WA."
    _response = chat_agent.execute(
        {
            "0_system": {
                "destination": content
            },
            "2_user": {
                "question": question
            }
        })

print(f"User: {question}")
print(_response.data)
