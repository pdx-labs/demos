import os
from pdx import Agent
from pdx.settings import Keys

openai_key = os.environ.get("OPENAI_KEY")
api_keys = Keys(openai_key=openai_key)


# Instantiate the Agent object
agent_folder_path = os.path.dirname(__file__)
insurance_agent = Agent(agent_folder_path, api_keys)


if __name__ == '__main__':
    _question = {
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
         

    _response = insurance_agent.execute({
        '2_user': {'question': _question}
    })

    print(_response.completion)