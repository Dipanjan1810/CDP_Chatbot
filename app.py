import streamlit as st
from chatbot import get_chatbot_response

st.set_page_config(page_title="CDP Support Chatbot", page_icon="🤖", layout="wide")

st.title("Support Agent Chatbot 🤖")
st.write("Powered By Groq")
st.write("Ask me questions about Segment, mParticle, Lytics, or Zeotap!")
st.write("Made By Dipanjan Dhar")

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize session state for conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Sidebar for conversation history
with st.sidebar:
    st.subheader("Conversation History")
    if st.session_state.conversation:
        for i, chat in enumerate(st.session_state.conversation):
            # Limit the answer to 100 characters
            truncated_answer = chat['answer'][:100] + "..." if len(chat['answer']) > 100 else chat['answer']
            
            st.markdown(f"**Q{i+1}:** {chat['question']}")
            st.markdown(f"**A{i+1}:** {truncated_answer}")
            st.markdown("---")
    else:
        st.write("No history yet.")

    # Clear conversation history
    if st.button("Clear History"):
        st.session_state.conversation = []
        st.success("Conversation history cleared!")

# Main content area for the most recent question and answer
st.subheader("Ask a Question")
question = st.text_area("Enter your question:", placeholder="How do I set up a new source in Segment?")

if st.button("Submit"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):
            try:
                # Get the chatbot's response
                response = get_chatbot_response(question, GROQ_API_KEY)

                # Add the question and response to the conversation history
                st.session_state.conversation.append({"question": question, "answer": response})

                # Display the most recent question and answer at the top
                st.subheader("Here is what I found:-")
                st.markdown(f"""<p style='font-size:24px;'><b><u>Your Question:</u></b>
                                <p style='font-size:16px;'>{question}</p>""", unsafe_allow_html=True)
                st.markdown(f"""<p style='font-size:24px;'><b><u>My answer:</u></b></p>
                                <p style='font-size:16px;'>{response}</p>""", unsafe_allow_html=True)


            except Exception as e:
                st.error(f"An error occurred: {e}")