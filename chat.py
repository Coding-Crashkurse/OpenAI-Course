import openai
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt3():
    messages = [
        {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
    ]

    while True:
        user_input = input("User: ")

        if user_input.lower() == "bye":
            print("Assistant: Auf Wiedersehen!")
            break

        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        assistant_message = response['choices'][0]['message']['content']
        print(f"Assistant: {assistant_message}")

        messages.append({"role": "assistant", "content": assistant_message})

chat_with_gpt3()
