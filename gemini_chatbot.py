"""
Paris Travel Guide Chatbot — Google Gemini 2.5 Flash
Multi-turn conversation using the new google-genai SDK
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Create the client using the new SDK style
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Start a chat session with seed history + system instruction
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a travel guide who will only provide information "
            "regarding travelling in Paris and you will speak in a concise manner."
        ),
        max_output_tokens=100,
    ),
    history=[
        types.Content(role="user", parts=[types.Part(text="What is the most famous landmark in Paris?")]),
        types.Content(role="model", parts=[types.Part(text="The most famous landmark in Paris is the Eiffel Tower.")])
    ]
)

questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

for question in questions:
    response = chat.send_message(question)
    print(f"Q: {question}")
    print(f"A: {response.text}\n")
