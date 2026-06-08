import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a travel guide who will only provide information regarding travelling in Paris and you will speak in a concise manner."
)

# Gemini uses a ChatSession to maintain conversation history automatically
chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["What is the most famous landmark in Paris?"]
    },
    {
        "role": "model",
        "parts": ["The most famous landmark in Paris is the Eiffel Tower."]
    }
])

questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

for question in questions:
    response = chat.send_message(question)
    reply = response.text
    print(f"Q: {question}")
    print(f"A: {reply}\n")
