import speech_recognition as aa  
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()  # Ensure it speaks the latest text

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "zenith" in instruction:
                instruction = instruction.replace("zenith", "")
            print(instruction)
    except Exception as e:
        print(f"Error: {e}")  # Print exception for debugging
        instruction = ""
    return instruction
def play_zenith():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    
    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)

    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        talk("Today's date is " + date)

    elif "how are you" in instruction:
        talk("I am fine, how about you")

    elif "what is your name" in instruction:
        talk("I am Zenith, what can I do for you?")

    elif "what is" in instruction or "who is" in instruction:
        human = instruction.replace("what is", "").replace("who is", "").strip()
        try:
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I could not find any information.")
    else:
        talk("I didn't understand that.")

# Start the assistant
play_zenith()
