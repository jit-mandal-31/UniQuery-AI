# UniQuery-AI

UniQuery AI is a unified multi-LLM comparison platform that allows users to ask one question and receive answers from multiple AI models simultaneously in a single interface.
It eliminates the need to repeat the same query across different AI tools, saving time and improving productivity.

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

# 🏗️ Architecture
### 🔹 High-Level Architecture Diagram

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

---

# 🔄 System Flow

1. User enters a query in the Streamlit UI
2. Query is sent to FastAPI /ask endpoint

3. Backend calls multiple LLMs using a single unified function

4. OpenRouter routes requests to respective models

5. Responses are collected and normalized

6. Failed or unavailable responses are filtered

7. Final results are displayed side-by-side in the UI
