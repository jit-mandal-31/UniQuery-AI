import streamlit as st
import requests

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="UniQuery AI", layout="wide")

# ---------------------------
# Session State
# ---------------------------
if "chats" not in st.session_state:
    st.session_state.chats = []   # [{"query": str, "results": list}]

if "current_query" not in st.session_state:
    st.session_state.current_query = ""

# ---------------------------
# Sidebar (ChatGPT-style)
# ---------------------------
with st.sidebar:
    st.title("🧠 UniQuery AI")

    if st.button("➕ New Chat"):
        st.session_state.current_query = ""
        st.rerun()

    st.markdown("---")
    st.subheader("📜 Previous Chats")

    for i, chat in enumerate(st.session_state.chats):
        if st.button(chat["query"][:30] + "...", key=f"chat_{i}"):
            st.session_state.current_query = chat["query"]
            st.rerun()

# ---------------------------
# Main UI
# ---------------------------
st.title("🤖 UniQuery AI")
st.write("Ask once, get answers from multiple AI models")

# 🔹 Query input + Edit button (side by side)
col1, col2 = st.columns([6, 1])

with col1:
    query = st.text_input(
        "Enter your question:",
        value=st.session_state.current_query,
        key="query_input"
    )

with col2:
    st.write("")  # spacing
    if st.button("✏️ Edit"):
        st.session_state.current_query = query
        st.rerun()

# ---------------------------
# Search
# ---------------------------
if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a query")
    else:
        with st.spinner("Querying multiple AI models..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    params={"query": query},
                    timeout=120
                )
            except Exception as e:
                st.error(f"Backend not reachable: {e}")
                st.stop()

        if response.status_code != 200:
            st.error("Backend error occurred")
            st.stop()

        data = response.json()
        results = data.get("results", [])

        if not results:
            st.warning("All models are temporarily unavailable.")
            st.stop()

        # Save chat
        st.session_state.chats.append({
            "query": query,
            "results": results
        })
        st.session_state.current_query = query
        st.rerun()

# ---------------------------
# Show current chat
# ---------------------------
if st.session_state.current_query:
    st.subheader("🔍 AI Responses")

    chat_data = next(
        (c for c in reversed(st.session_state.chats)
         if c["query"] == st.session_state.current_query),
        None
    )

    if chat_data:
        cols = st.columns(len(chat_data["results"]))

        for col, res in zip(cols, chat_data["results"]):
            with col:
                st.markdown(f"### {res['model']}")
                st.write(res["response"])
                st.caption(f"Length: {res['length']} characters")

                st.download_button(
                    label="⬇️ Download Answer",
                    data=res["response"],
                    file_name=f"{res['model'].replace(' ', '_')}.txt",
                    mime="text/plain"
                )
