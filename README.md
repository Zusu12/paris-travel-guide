# 🗼 Paris Travel Guide Chatbot

A multi-turn AI chatbot that acts as a Paris travel guide — built with both **OpenAI (GPT-4o-mini)** and **Google Gemini (Gemini 1.5 Flash)**.

---

## 📁 Project Structure

```
paris-travel-guide/
├── openai/
│   └── chatbot.py        # GPT-4o-mini version
├── gemini/
│   └── chatbot.py        # Gemini 1.5 Flash version
├── requirements.txt
├── .env.example          # Template for your API keys
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/Zusu12/paris-travel-guide.git
cd paris-travel-guide
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API keys
```bash
cp .env.example .env
```
Then open `.env` and fill in your keys:
```
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key
```

> 🔑 Get a free Gemini API key at [aistudio.google.com](https://aistudio.google.com)

---

## ▶️ Run

**OpenAI version:**
```bash
python openai/chatbot.py
```

**Gemini version:**
```bash
python gemini/chatbot.py
```

---

## 💡 How it works

Both versions maintain a **conversation history** — each question and answer is appended to the chat so the model has full context for follow-up questions. The system prompt restricts the guide to Paris-related topics only.

| Feature | OpenAI | Gemini |
|---|---|---|
| Model | gpt-4o-mini | gemini-1.5-flash |
| History | Manual list append | `ChatSession` (auto) |
| Free tier | Limited | Yes (Google AI Studio) |
"# paris-travel-guide" 
