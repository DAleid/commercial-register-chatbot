import os
import google.generativeai as genai
import streamlit as st

# Load API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Please set the environment variable GOOGLE_API_KEY.")
    st.stop()

# Configure the API key
genai.configure(api_key=api_key)

# Initialize the model with a system instruction
try:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are an assistant to answer people's questions about the Law of Commercial Register in general."
    )
except Exception as e:
    st.error(f"Error initializing model: {e}")
    st.stop()

# Streamlit interface
st.title("Ask Chatbot")

# Conversation log
if 'conversation_log' not in st.session_state:
    st.session_state.conversation_log = []

# Display previous conversation
for message in st.session_state.conversation_log:
    st.chat_message(message['role']).markdown(message['content'])

# User input
prompt = st.chat_input('Enter your question here')

# Generate response
if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.conversation_log.append({'role': 'user', 'content': prompt})

    try:
        response = model.generate_content(prompt)
        st.chat_message('assistant').markdown(response.text)
        st.session_state.conversation_log.append({'role': 'assistant', 'content': response.text})
    except Exception as e:
        st.error(f"Error generating response: {e}")
