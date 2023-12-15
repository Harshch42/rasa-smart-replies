import json
import random
import asyncio
from rasa.core.agent import Agent

# Load the trained Rasa model
agent = Agent.load("models/20231212-211551-beveled-gauge.tar.gz")

# Load the responses from the JSON file
with open("suggestions.json", "r") as f:
    responses = json.load(f)
    

async def get_suggestions(message):
    
    result = await agent.parse_message(message_data=message)

    # Get the intent from the result
    intent = result["intent"]["name"]

    # Get the responses for the intent
    intent_responses = responses.get(intent, {})

    # Randomly select responses from each category
    suggestions = [random.choice(intent_responses[key]) for key in intent_responses]

    return suggestions
    

message = "Hello sir!"
suggestions = asyncio.run(get_suggestions(message))
print(suggestions)


