import wit

# Initialize the Wit client with your access token
client = wit.Wit('WUG6YPRUU43NJ47HI2GK3TOXTPZYLRHN')

# Define a function to handle messages
def handle_message(message):
    # Send the message to Wit.ai for processing
    resp = client.message(message)
    
    # Extract the intent and entities from the response
    intent = resp['intents'][0]['name'] if 'intents' in resp else None
    entities = resp['entities']
    
    # Based on the intent, generate a response
    if intent == 'abilities':
        return "im useless"
    elif intent == 'hello_hi':
        return "hello, how can i help you?"
    elif intent == 'angry':
        return "oh, its okay how can i help you calm down?"
    elif intent == 'greet':
        return "oh, i feel great today, how are you feeling today?"
    elif intent == 'happy':
        return "oh great!"
    elif intent == "insult":
        return "im sorry what did i do wrong?"
    
    else:
        return "I'm sorry, I didn't understand that."

# Main loop to continuously get user input and respond
while True:
    user_input = input("You: ")
    response = handle_message(user_input)
    print("Bot:", response)
