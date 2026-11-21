import streamlit as st
question=st.chat_input("Ask me something")
if question:
    st.chat_message("user").write(f"i got your question as {question}, let me help you")
st.chat_message("assistant").write(f"i have received  your question let me help youb")