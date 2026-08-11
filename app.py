from google.genai import types
from prompts import SYSTEM_PROMPT
from config import client
from messages import WELCOME_MESSAGE, EMPTY_MESSAGE, EXIT_MESSAGE, ERROR_MESSAGE


chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT
    )
)

print(WELCOME_MESSAGE)

while True:

    question = input("🧠 Ask LearnMate: ")

    if question.strip().lower() == "exit":
        print(EXIT_MESSAGE)
        break

    if not question.strip():
        print(EMPTY_MESSAGE)
        continue
    try:
        response = chat.send_message(question)

        print("\n🧠 LearnMate:")
        print(response.text)
        print()

    except Exception:
        print(ERROR_MESSAGE)