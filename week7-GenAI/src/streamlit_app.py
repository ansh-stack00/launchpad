import streamlit as st
import requests


if "prev_mode" not in st.session_state:
    st.session_state.prev_mode = None

if "question" not in st.session_state:
    st.session_state.question = ""

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Advanced RAG System", layout="wide")

st.title("🧠 Advanced RAG + SQL Agent")


st.sidebar.header("Mode Selection")

mode = st.sidebar.radio(
    "Choose query type",
    ["📄 Document RAG", "🗄️ SQL Agent"],
    key="mode"
)

# Clear input when mode changes
if st.session_state.prev_mode != mode:
    st.session_state.question = ""
    st.session_state.prev_mode = mode

# take input from user 

question = st.text_input(
    "Ask your question:",
    key="question"
)

# document RAG
if mode == "📄 Document RAG":
    if st.button("Ask RAG"):
        if not question:
            st.warning("Please enter a question")
        else:
            with st.spinner("Thinking..."):
                response = requests.post(
                    f"{API_URL}/ask",
                    json={"question": question}
                )

            if response.status_code == 200:
                data = response.json()

                st.subheader("Answer")
                st.write(data["answer"])

                st.subheader("Hallucination Detected?")
                st.write("Yes" if data["hallucinated"] else "No")

            else:
                st.error("Error from RAG API")

# SQL Agent 
if mode == "🗄️ SQL Agent":
    if st.button("Ask SQL Agent"):
        if not question:
            st.warning("Please enter a question")
        else:
            with st.spinner("Generating SQL & executing..."):
                response = requests.post(
                    f"{API_URL}/ask-sql",
                    json={"question": question}
                )

            if response.status_code == 200:
                data = response.json()

                if data.get("error"):
                    st.error(data["error"])
                else:
                    st.subheader("Generated SQL")
                    st.code(data["sql"], language="sql")

                    st.subheader("Query Result")
                    st.dataframe(
                        {col: [row[i] for row in data["rows"]]
                         for i, col in enumerate(data["columns"])}
                    )

                    st.subheader("Summary")
                    st.write(data["summary"])

            else:
                st.error("Error from SQL API")
