# 🧠 Local AI Agent (Ollama + LlamaIndex)

A fully local AI agent that generates structured user data from natural language prompts and saves it as JSON — no OpenAI or external APIs required.

---

## 🚀 Features

- Fully offline AI (runs on Ollama)
- Natural language → structured data
- Tool-based agent architecture
- JSON generation & file saving
- Beginner-friendly but production-style design

---

## 🧩 Tech Stack

- Python
- LlamaIndex
- Ollama (TinyLlama / local models)
- ReAct-style tool execution

---

## 🏗️ Architecture

```
User Input
   ↓
LLM (Ollama - TinyLlama)
   ↓
Agent (LlamaIndex)
   ↓
Tools (Generate Users / Save JSON)
   ↓
Output (users.json)
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/local-ai-agent.git
cd local-ai-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Run Project

### 1. Start Ollama

```bash
"C:\Users\YOUR_NAME\AppData\Local\Programs\Ollama\ollama.exe" run tinyllama
```

### 2. Run agent

```bash
python main.py
```

---

## 💬 Example Prompts

```text
generate users
save users
```

---

## 📦 Output

```json
[
  {
    "name": "John",
    "email": "john@gmail.com",
    "age": 25
  }
]
```

Saved at:

```
outputs/users.json
```

---

## 📸 Demo

### Agent Output
![Agent Output]("C:\Users\91837\Pictures\Screenshots\Terminal-Demo.png")

---

## 🎯 What I Learned

- Building local LLM applications
- Using Ollama for offline inference
- Tool-based agent design
- Python automation workflows
- Structuring AI projects for production

---

## 📌 Future Improvements

- Dynamic user input parsing
- Web UI (Streamlit)
- Multiple tools (file reader, summarizer)
- Better LLM (Qwen / Llama 3 8B)

---

## ⭐ License

MIT License
