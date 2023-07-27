import os
from pdx import Agent

# Instantiate the Agent object
agent_folder_path = os.path.dirname(__file__)
car_rec_agent = Agent(agent_folder_path)


if __name__ == '__main__':
    _question = 'I am a female driver ageo 20, budget is 50000 US dollar and looking for a sedan, it is better produced after 2020. I need to drive this car in snowy days.  I prefer Lexus, Mercedes benz.'

    _response = car_rec_agent.execute({
        '2_user': {'question': _question}
    })

    print(_response.data)