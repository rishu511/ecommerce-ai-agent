import streamlit as st
from agent import agent

st.set_page_config(page_title="E-commerce AI Agent", layout="centered")

st.title("🛒 E-commerce AI Agent")

# Input
question = st.text_input("Ask your question:")

# Toggle to show SQL
show_sql = st.checkbox("Show SQL Query (Debug)")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            answer, sql = agent(question)

            st.markdown(f"### ✅ Answer:\n{answer.strip()}")

            if show_sql:
                st.code(sql, language="sql")