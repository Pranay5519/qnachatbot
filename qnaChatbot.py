import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
 
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# gemini pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history = [])

def get_gemini_response(question):
    response = chat.send_message(question  , stream = True)
    response.resolve()
    return response.text



def main():
    st.set_page_config("Q&A chatbot")
    st.header("-Chatbot-")

    if 'messages' not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    # user input 
    user_question = st.chat_input("Type Here ....")
    
    if user_question:
        response = get_gemini_response(user_question)
        
        
        with st.chat_message("user"):
            st.markdown(user_question)
            
        st.session_state.messages.append({'role' : 'user' , 'content' : user_question})
        
        
        
        with st.chat_message('assistant'):
            st.markdown(response)
            
        st.session_state.messages.append({'role' : 'assistant' , 'content' : response})

    
if __name__ == "__main__":
    main()