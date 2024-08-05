
import speech_recognition as sr
import pyttsx3
import os

def speak(text):
    """
    Convert text to speech.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """
    Listen for voice commands and return the recognized text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def open_application(app_name):
    """
    Open specified application based on the app name.
    """
    if app_name == "notepad":
        os.system("notepad")
    elif app_name == "calculator":
        os.system("calc")
    elif app_name == "chrome":
        os.system("start chrome")
    elif app_name == "word":
        os.system("start winword")
    elif app_name == "explorer":
        os.system("explorer")
    else:
        speak(f"Sorry, I cannot open {app_name}")

def process_command(command):
    """
    Process the voice command and execute the appropriate action.
    """
    if command:
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "what is your name" in command:
            speak("I am your voice assistant.")
        elif "how are you" in command:
            speak("I am fine, thank you. How can I help you?")
        elif "open" in command:
            app_name = command.replace("open ", "").strip()
            speak(f"Opening {app_name}")
            open_application(app_name)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            return False
        else:
            speak("I didn't catch that. Please try again.")
    return True

if __name__ == "__main__":
    speak("Initializing voice assistant. How can I help you today?")
    active = True
    while active:
        command = listen()
        active = process_command(command)
