# Local AI Agent (No API Key Required)

An AI agent built using LlamaIndex + Ollama that generates structured user data from natural language prompts and saves it as JSON.

---

## 🚀 Features

- Fully local AI (no OpenAI or Gemini API needed)
- Natural language understanding via Llama3
- Tool-based agent architecture
- JSON generation and file saving
- Beginner-friendly but production-style design

---

## 🧠 Architecture

User Input
→ LLM (Ollama - Llama3)
→ ReAct Agent (LlamaIndex)
→ Tools (Generate Users, Save JSON)
→ Output (users.json)

---

## ▶️ Run Project

### 1. Start Ollama
```bash
ollama run tinyllama
```