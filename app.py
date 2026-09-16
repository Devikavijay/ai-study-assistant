from google.genai import types
from prompts import SYSTEM_PROMPT
from config import client
from messages import WELCOME_MESSAGE, EMPTY_MESSAGE, EXIT_MESSAGE, ERROR_MESSAGE
from utils import is_exit_command, is_empty_input


chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT
    )
)

print(WELCOME_MESSAGE)

while True:

    question = input("🧠 Ask LearnMate: ")

    if is_exit_command(question):
        print(EXIT_MESSAGE)
        break

    if is_empty_input(question):
        print(EMPTY_MESSAGE)
        continue
    try:
        response = chat.send_message(question)

        print("\n🧠 LearnMate:")
        print(response.text)
        print()

    except Exception:
        print(ERROR_MESSAGE)