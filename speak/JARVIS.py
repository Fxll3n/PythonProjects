import speech_recognition as sr
import pyttsx3
import subprocess
import openai

# Initialize text-to-speech engine
engine = pyttsx3.init()

api_key = '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'

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_application(file_path):
    known_applications = {
        "discord": r"C:\Users\Alienware\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
        "notepad": r"C:\Windows\System32\notepad.exe",
        "opera": r"C:\Users\Alienware\AppData\Local\Programs\Opera GX\launcher.exe",
        # Add more applications as needed
    }

    try:
        if file_path in known_applications:
            subprocess.Popen([known_applications[file_path]], shell=True)
            speak(f"Opening {file_path}")
        else:
            speak(f"Sorry, I don't have information on how to open {file_path}.")
    except Exception as e:
        speak(f"Sorry, I couldn't open that application or file. {e}")

def make_gpt_request(api_key, prompt):
    # Set the API key
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Pretend to be JARVIS from Iron Man Movies but created by Angel. You "
                                              "have a 'Cousin' called HackBot, who is a discord bot also created by "
                                              "Angel for the John Hersey High School Hack Club Server."},
                {"role": "user", "content": prompt},
            ]
        )

        return response['choices'][0]['message']['content']

    except openai.error.OpenAIError as e:
        print(f"Error making GPT request: {e}")
        return "Sorry, I couldn't generate a response from GPT."

def listen_for_gpt_prompt():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for GPT prompt...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        gpt_prompt = recognizer.recognize_google(audio)
        print(f"GPT Prompt: {gpt_prompt}")
        return gpt_prompt

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the GPT prompt.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def listen_for_commands():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for the wake word 'Jarvis'...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command: {command}")

            if "jarvis" in command:
                speak("How may I assist you?")
                print("Listening for your command...")

                audio = recognizer.listen(source)
                user_command = recognizer.recognize_google(audio).lower()

                if "open" in user_command:
                    file_name = user_command.replace("open", "").strip()
                    open_application(file_name)

                else:
                    # For other commands, directly use GPT-3
                    gpt_response = make_gpt_request(api_key, user_command)
                    speak(gpt_response)

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:
        listen_for_commands()
