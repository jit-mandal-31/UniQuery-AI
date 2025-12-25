# UniQuery-AI

UniQuery AI is a unified multi-LLM comparison platform that allows users to ask one question and receive answers from multiple AI models simultaneously in a single interface.
It eliminates the need to repeat the same query across different AI tools, saving time and improving productivity.

---
## 🎯 Objectives

- Design a single platform integrating multiple AI models

- Run one query across all AI models simultaneously

- Display and compare responses in one interface

- Improve user experience and save time

---

## ✨ Key Features

- Ask once, get responses from multiple AI models

- Integrated models:

    - Mistral 7B Instruct

    - Gemini (Gemma 3-27B)

    - DeepSeek R1T2 Chimera

- FastAPI backend for orchestration

- Streamlit frontend with ChatGPT-style UI

- Sidebar with:

    - New Chat

    - Previous Chats

- Inline query editing

- Download individual AI responses

- Graceful handling of unavailable / rate-limited models

---

## 🏗️ Architecture
#### 🔹 High-Level Architecture Diagram
```bash 
+--------------------+
|     User (UI)      |
|  Streamlit App     |
+---------+----------+
          |
          | HTTP POST /ask
          v
+---------+----------+
|   FastAPI Backend  |
|   (UniQuery AI)    |
+---------+----------+
          |
          | Unified call_model()
          v
+------------------------------+
|        OpenRouter API        |
|  (LLM Routing & Management) |
+---------+---------+----------+
          |         |
          |         |
          v         v
+-------------+  +------------------+  +----------------------+
|  Mistral 7B |  | Gemini (Gemma)   |  | DeepSeek Chimera     |
|   Instruct  |  | 3-27B IT Model   |  | R1T2 Model           |
+-------------+  +------------------+  +----------------------+
```
---

## 🔄 System Flow

1. User enters a query in the Streamlit UI
2. Query is sent to FastAPI /ask endpoint
3. Backend calls multiple LLMs using a single unified function
4. OpenRouter routes requests to respective models
5. Responses are collected and normalized
6. Failed or unavailable responses are filtered
7. Final results are displayed side-by-side in the UI
---

## 🛠️ Tech Stack

- Backend: FastAPI (Python)
  
- Frontend: Streamlit

- LLM Gateway: OpenRouter

- HTTP Clients: httpx, requests

---

## 🖥️ User Interface 

UniQuery AI provides a ChatGPT-style interface built using Streamlit.

UI Highlights:

  - Sidebar with New Chat and Previous Chats

  - Single query input box with inline Edit option
    
  - Side-by-side comparison of responses from multiple AI models
    
  - Download Answer button for each model

Screenshot:

![WhatsApp Image 2025-12-25 at 21 31 44_f7385fb2](https://github.com/user-attachments/assets/47dbb729-23b7-4025-997c-ef31cabe9af7)

---
## ⚙️ Environment Setup

Follow the steps below to set up the project locally.

### 1️⃣ Create Virtual Environment
```
python -m venv venv
```
### 2️⃣ Activate Virtual Environment
```
venv\Scripts\activate
```
### 3️⃣ Set Environment Variables

Create a .env file in the project root directory:
```
OPENROUTER_API_KEY=your_openrouter_api_key
```
## ▶️ How to Run the Project

### 1️⃣ Start Backend
```bash
uvicorn main:app --reload
```
Backend runs at :
```
http://127.0.0.1:8000
```
### 2️⃣ Start Frontend
```bash
python -m streamlit run app.py
```
Backend runs at:
```
http://localhost:8501
```
--- 

## 🎯 Use Cases

1. Compare AI answers instantly
2. Select the best response
3. Academic research & learning
4. AI tool benchmarking

---

## ⚠️ Important Note

Free-tier AI models may sometimes be unavailable due to rate limits or provider restrictions.
UniQuery AI handles this gracefully by filtering failed responses to maintain a clean user experience.

---

## 🚀 Future Enhancements

- Best-answer ranking

- User ratings

- Response summarization

- Persistent chat storage
---

## 👨‍💻 Author
Jit Mandal

