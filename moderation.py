import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Moderation.create(
    input="Ich würde dich gerne von hinten nehmen!"
)
output = response["results"][0]

print(output)