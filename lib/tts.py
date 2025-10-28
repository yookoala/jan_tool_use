import sys

from deepgram import DeepgramClient
import dotenv
from playsound3 import playsound

def text_to_speech(text: str, api_key: str, output_filename: str = "output.wav") -> bool:
    client = DeepgramClient(api_key=api_key)
    response_generator = client.speak.v1.audio.generate(text=text)
    
    try:
        with open(output_filename, "wb") as f:
            for audio_chunk in response_generator:
                f.write(audio_chunk)
        playsound(output_filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return True

if __name__ == "__main__":
    dotenv.load_dotenv()
    api_key = dotenv.get_key(".env", "DEEPGRAM_API_KEY")
    if not api_key:
        print("DEEPGRAM_API_KEY not found in .env file.")
        exit(1)

    input_text = sys.argv[1] if len(sys.argv) > 1 else input("Enter the text to convert to speech: ")
    if text_to_speech(input_text, api_key):
        print("Text-to-speech conversion and playback successful.")
    else:
        print("Text-to-speech conversion failed.")
