import streamlit as st
import time
from google.genai import types
from config import client, PRIMARY_MODEL,FALLBACK_MODEL
from prompts import SYSTEM_PROMPT

st.set_page_config(
    page_title = "LearnMate",
    page_icon = "🧠"
)


if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model = PRIMARY_MODEL,
        config = types.GenerateContentConfig(

system_instruction = SYSTEM_PROMPT
        )
    )


if "messages" not in st.session_state:
    st.session_state.messages = []



st.title("🧠 LearnMate")
st.write("Your AI Study Assistant -- ask questions and learn step by step.")

st.sidebar.title("⚙️ Controls")
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []

    st.session_state.chat = client.chats.create(
        model = PRIMARY_MODEL,
        config = types.GenerateContentConfig(
            system_instruction = SYSTEM_PROMPT
        )
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask LearnMate anything...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    try:
        for attempt in range(3):
            try:
                response = st.session_state.chat.send_message(question)
                break

            except Exception as e:
                if attempt < 2:
                    time.sleep(2)
                else:
                    st.session_state.chat = client.chats.create(
                        model=FALLBACK_MODEL,
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_PROMPT
                        )
                    )
                    response = st.session_state.chat.send_message(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": response.text}
        )

        with st.chat_message("assistant"):
            st.write(response.text)

    except Exception as e:
        st.error(
            "LearnMate is temporarily unavailable. Please try again in a moment."
        )
        print("REAL ERROR:", e)