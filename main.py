import webbrowser
import pyttsx3
import speech_recognition as sr


# Initialize the speech recognition engine and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    # Convert text to speech.
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    # Process the user's voice command and perform appropriate actions.
    command = command.lower()
    actions = {
        "open google": "https://google.com",
        "open facebook": "https://facebook.com",
        "open youtube": "https://youtube.com",
        "open linkedin": "https://linkedin.com",
        "open instagram": "https://instagram.com",
        "open twitter": "https://x.com",
    }

    # Handle predefined commands
    for key, url in actions.items():
        if key in command:
            speak(f"Opening {key.split(' ')[1]}...")
            webbrowser.open(url)
            return

    # Handle dynamic commands like playing music
    if "play song" in command:
        song_name = command.replace("play song", "").strip()
        play_song(song_name)
    else:
        speak("Sorry, I couldn't understand that command.")

def play_song(song_name):
    # Play a song from a simulated music library.
    music_library = {
        "let me": "https://youtu.be/J-dv_DcDD_A?si=WY1GFlAoelplGZ7T",
        "time": "https://youtu.be/tt2k8PGm-TI?si=Ebtzz_D67NFER0B4",
        "alienated": "https://youtu.be/2ntdRjSdzZ4?si=gqB7H-OB9JD3COzj",
        "girlfriend": "https://youtu.be/3AtDnEC4zak?si=FlT0L9JFwUVWRAPh",
        "attention" : "https://www.youtube.com/watch?v=nfs8NYg7yQM",
    }

    try:
        song_url = music_library[song_name.lower()]
        speak(f"Playing {song_name}...")
        webbrowser.open(song_url)
    except KeyError:
        speak(f"Sorry, I couldn't find the song {song_name}.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        speak("An error occurred while trying to play the song.")

def main():
    # Main function to initialize the assistant and listen for commands.
    speak("Your assistant is now ready. Say 'activate' to start.")
    while True:
        try:
            print("Listening for activation...")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            activation_word = recognizer.recognize_google(audio).lower()
            if "activate" in activation_word:
                speak("I'm listening for your command.")
                print("Assistant activated. Waiting for a command...")

                # Listen for a command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    process_command(command)

        except sr.UnknownValueError:
            print("Could not understand audio. Please speak clearly.")
            speak("Sorry, I didn't catch that. Could you repeat?")
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            speak("There seems to be an issue with the speech recognition service.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            speak("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting program. Goodbye!")
        speak("Goodbye!")

