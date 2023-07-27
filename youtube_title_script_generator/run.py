from title_agent import title_agent
from script_agent import script_agent


# User input: user can enter in any topic they want to generate a youtube title and script about that topic

# Processes user input and provides output
if __name__ == '__main__':
    _topic = 'Deep Learning'
    _title_response = title_agent.execute({
        "title_template": {
            "topic": _topic
        }
    })

    _script_response = script_agent.execute({
        "script_template": {
            "title": _title_response.data
        }
    })

    # Print title and the script
    print(f"Topic: {_topic}")
    print(_script_response.data)
