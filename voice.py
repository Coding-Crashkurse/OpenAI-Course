import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("sample.m4a", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)
print(transcript["text"])


audio_file= open("sample.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript["text"])