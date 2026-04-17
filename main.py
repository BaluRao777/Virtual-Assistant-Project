# @title Default title text
import openai
import pyttsx3
import speech_recognition as speech
import requests  # Add the requests library
from bs4 import BeautifulSoup  # Add BeautifulSoup for web scraping

openai.api_key = "YOUR_API_KEY"

engine = pyttsx3.init()


class VirtualAssistantApp:
    def transcribe_audio_to_text(self, filename):
        recognizer = speech.Recognizer()
        with speech.AudioFile(filename) as source:
            audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except speech.UnknownValueError:
            return "Error: Google Speech Recognition could not understand audio"
        except speech.RequestError as e:
            return f"Error: Could not request results from Google Speech Recognition service; {e}"
        except Exception as e:
            return f"An error occurred during audio transcription: {e}"

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            n=1,
            stop=None,
            temperature=0.7,
            max_tokens=1296,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["text"]

    def speak_text(self, text):
        engine.say(text)
        engine.runAndWait()

    def fetch_website_title(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            return title
        except Exception as e:
            return f"An error occurred while fetching the website title: {e}"

    def process_input(self, transcription):
        if transcription.lower() == "rao":
            filename = "input.wav"
            print("I am Rao. How can I help you?")
            with speech.Microphone() as sources:
                recognizer = speech.Recognizer()
                sources.pause_threshold = 1
                audio = recognizer.listen(sources, phrase_time_limit=None, timeout=None)
                with open(filename, "wb") as f:
                    f.write(audio.get_wav_data())
            text = self.transcribe_audio_to_text(filename)
            if text and not text.startswith("Error"):
                print(f"You said: {text}")
                response = self.generate_response(text)
                print(f"Rao says: {response}")
                self.speak_text(response)
            elif text.startswith("Error"):
                print(text)
            else:
                print("No valid transcription.")

    def main(self):
        print(sr.Microphone.list_microphone_names())
        while True:
            print("Say Rao to start recording your question...")
            with speech.Microphone(device_index=6) as source:
                recognizer = speech.Recognizer()
                audio = recognizer.listen(source)
                try:
                    transcription = recognizer.recognize_google(audio)
                    self.process_input(transcription)
                except speech.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except speech.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")


if __name__ == "__main__":
    app = VirtualAssistantApp()
    app.main()
