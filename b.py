import speech_recognition as sr
import wit
import pyttsx3
import pyjokes
ttx = "hello oompa loompa"
# Initialize the Wit client with your access token
wit_client = wit.Wit('WUG6YPRUU43NJ47HI2GK3TOXTPZYLRHN')
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def handle_message(message):
    # Send the message to Wit.ai for processing
    resp = wit_client.message(message)
    
    # Extract the intent and entities from the response
    intent = resp['intents'][0]['name'] if 'intents' in resp else None
    entities = resp['entities']
    
    # Based on the intent, generate a response
    if intent == 'abilities':
        return "I'm sorry, I cannot perform that function."
    elif intent == 'hello_hi':
        return "Hello, how can I help you?"
    elif intent == 'angry':
        return "It's okay. How can I help you calm down?"
    elif intent == 'greet':
        return "I feel great today, how are you feeling?"
    elif intent == 'happy':
        return "That's wonderful!"
    elif intent == "insult":
        return "I apologize if I've done anything wrong."
    elif intent == "name":
        return "currently, my name is 'faster'"
    elif intent == "sad":
        return "oh, how can i make you feel good?"
    elif intent == "thanks":
        return "Glad I could help"
    elif intent == "joke":
        joke = pyjokes.get_joke(category='all')
        return joke
    else:
        return "I'm sorry, I didn't understand that."
   

# Function to detect the wake word
def detect_wake_word(recognizer, audio):
    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        if "faster" in text.lower():
            return True
    except sr.UnknownValueError:
        # Google Web Speech API could not understand the audio
        pass
    except sr.RequestError as e:
        # The API was unreachable or unresponsive
        print(f"Could not request results from Google Web Speech API; {e}")
    return False

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Main loop to continuously listen for the wake word and respond
while True:
    with sr.Microphone() as source:
        print("Waiting for wake word...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

        # Check if the wake word is detected
        if detect_wake_word(recognizer, audio):
            print("Wake word detected. How can I assist you?")
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source)

            try:
                # Recognize speech using Google Web Speech API
                text = recognizer.recognize_google(audio_data)
                print("You said:", text)
                
                # Pass the recognized speech to Wit.ai for natural language understanding
                response = handle_message(text)
                print("Bot:", response)
                
                # Speak the response
                engine.say(response)
                engine.runAndWait()
                
            except sr.UnknownValueError:
                # API was unable to understand the audio
                print("Google Web Speech API could not understand the audio, please try again.")
            except sr.RequestError as e:
                # The API was unreachable or unresponsive
                print(f"Could not request results from Google Web Speech API; {e}")
