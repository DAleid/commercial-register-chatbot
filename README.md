# Commercial Register Law Chatbot

A conversational AI assistant that answers questions about the Law of Commercial Register, powered by Google Gemini 1.5 Flash.

## Overview

This application provides an interactive chat interface for querying Commercial Register regulations. Users can ask natural language questions and receive accurate, context-aware legal guidance based on the law's provisions.

## Features

- Natural language Q&A about Commercial Register law
- Powered by Google Gemini 1.5 Flash
- Clean conversational Streamlit interface
- Secure API key management via environment variables

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python |
| LLM | Google Gemini 1.5 Flash |
| UI | Streamlit |
| SDK | google-generativeai |

## Getting Started

### Prerequisites

- Python 3.8+
- Google AI API key — [Get one here](https://aistudio.google.com)

### Installation

```bash
git clone https://github.com/DAleid/Chatbot--Gemini-API-.git
cd Chatbot--Gemini-API-
pip install google-generativeai streamlit
```

### Configuration

```bash
# Linux / macOS
export GOOGLE_API_KEY=your_api_key_here

# Windows
set GOOGLE_API_KEY=your_api_key_here
```

### Run

```bash
streamlit run chatbot_GIMINI.py
```

Open `http://localhost:8501` in your browser.

## Usage

Type your question in the chat input and press Enter. The assistant responds with relevant information about Commercial Register law in a conversational format.

## License

MIT License