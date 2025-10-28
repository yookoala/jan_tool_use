from deepgram import DeepgramClient
import dotenv

def text_to_speech(text: str, api_key: str, output_filename: str = "output.wav"):
    client = DeepgramClient(api_key=api_key)
    response_generator = client.speak.v1.audio.generate(text=text)
    
    with open(output_filename, "wb") as f:
        for audio_chunk in response_generator:
            f.write(audio_chunk)

    return output_filename

if __name__ == "__main__":
    dotenv.load_dotenv()
    api_key = dotenv.get_key(".env", "DEEPGRAM_API_KEY")
    if not api_key:
        print("DEEPGRAM_API_KEY not found in .env file.")
        exit(1)

    input_text = input("Enter the text to convert to speech: ")
    output_file = text_to_speech(input_text, api_key)
    if output_file:
        print(f"Audio saved to: {output_file}")
    else:
        print("Failed to generate audio")
