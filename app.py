import os
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# Initialize and cache the QA chain
@st.cache_resource
def setup_qa():
    loader = TextLoader("club_info.txt")
    index = VectorstoreIndexCreator(
        embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
        vectorstore_cls=FAISS
    ).from_loaders([loader])

    llm = Ollama(model="llama3", temperature=0.7)

    retriever = index.vectorstore.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    return qa

# Streamlit UI setup
st.set_page_config(page_title="Coding Club Chatbot", page_icon="🤖")
st.title("🤖 Coding Club Chatbot")

qa_chain = setup_qa()

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

# Chat input
user_input = st.chat_input("Ask me anything about the club, events, and registration!")

if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        response = qa_chain.invoke({"query": user_input})
        bot_reply = response["result"]

    # Add assistant message to chat history
    st.session_state.chat_history.append(("assistant", bot_reply))
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
