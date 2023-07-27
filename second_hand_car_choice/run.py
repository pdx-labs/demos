from insurance_agent import insurance_agent
from car_rec_agent import car_rec_agent


if __name__ == '__main__':
    _question = 'I am a female driver ageo 20, budget is 50000 US dollar and looking for a sedan, it is better produced after 2020. I need to drive this car in snowy days.  I prefer Lexus, Mercedes benz.'
    _response_rec = insurance_agent.execute({
        '1_prompt': {'question': _question}
    })
    print(_response_rec.data)

    _response_insurance = car_rec_agent.execute({
        '2_user': {'question': _response_rec.data}
    })
    print(_response_insurance.data)
