import openai
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# result = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Hallo GPT, wie geht es?",
#   max_tokens=7,
#   temperature=0
# )
#
# print(result)
# print(result["choices"][0]["text"])

result2 = openai.Edit.create(
  model="text-davinci-edit-001",
  input="What day of the wek is it?",
  instruction="Fix the spelling mistakes"
)

print(result2)
print(result2["choices"][0]["text"])


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="We´re writing to ",
  suffix=". How are you?",
  temperature=1,
  max_tokens=10,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)