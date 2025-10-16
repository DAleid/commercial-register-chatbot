Law of Commercial Register Chatbot

A Streamlit-based chatbot powered by Google Gemini 1.5 that answers questions about the Law of Commercial Register. The app maintains conversation history, provides AI-generated responses, and uses environment variables for secure API key management.

Features

Interactive chat interface

AI-powered legal guidance (informational purposes only)

Conversation memory

Secure API key handling

Installation
git clone <repo-url>
cd <repo-folder>
pip install streamlit google-generativeai
export GOOGLE_API_KEY="YOUR_API_KEY"  # Windows: setx GOOGLE_API_KEY "YOUR_API_KEY"
streamlit run app.py

Usage

Enter your question in the chat box, and the AI will respond while storing the conversation for context.
