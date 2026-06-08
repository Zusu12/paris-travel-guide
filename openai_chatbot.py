import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = "gpt-4o-mini"
client = OpenAI()  # reads OPENAI_API_KEY from environment

conversation = [
    {
        "role": "system",
        "content": "You are a travel guide who will only provide information regarding travelling in Paris and you will speak in a concise manner."
    },
    {"role": "user", "content": "What is the most famous landmark in Paris?"},
    {"role": "assistant", "content": "The most famous landmark in Paris is the Eiffel Tower."}
]

questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

for question in questions:
    input_dict = {"role": "user", "content": question}
    conversation.append(input_dict)

    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_tokens=100
    )

    reply = response.choices[0].message.content
    print(f"Q: {question}")
    print(f"A: {reply}\n")

    response_dict = {"role": "assistant", "content": reply}
    conversation.append(response_dict)
