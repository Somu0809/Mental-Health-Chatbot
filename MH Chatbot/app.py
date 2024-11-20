import streamlit as st
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading
import uvicorn

# Mock chatbot function
def chatbot_response(user_input):
    if "anxiety" in user_input.lower():
        return "I'm here to help you manage your anxiety. Take a deep breath."
    elif "depression" in user_input.lower():
        return "Remember, you're not alone. Let's talk through what you're feeling."
    else:
        return "I'm here to listen. Could you tell me more about what's on your mind?"

# FastAPI setup
app = FastAPI()

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoint for the chatbot
@app.post("/chat")
async def chat_endpoint(data: dict):
    user_input = data.get("message", "")
    response = chatbot_response(user_input)
    return {"response": response}

# Run FastAPI in a separate thread
def run_fastapi():
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Run Streamlit app
def run_streamlit():
    st.set_page_config(page_title="Mental Health Chatbot", layout="centered")

    st.title("Mental Health Chatbot")
    st.write("Welcome to the mental health chatbot. Feel free to share your thoughts and concerns.")
    st.sidebar.title("About the Chatbot")
    st.sidebar.write("This chatbot provides supportive responses to help users with mental health concerns. "
                     "Note that this is not a replacement for professional mental health support.")

    user_input = st.text_input("Your message:")
    if st.button("Send"):
        if user_input.strip():
            # Simulating the response logic (replace with actual API call if needed)
            response = chatbot_response(user_input)
            st.write(f"Chatbot: {response}")

# Main function to run both FastAPI and Streamlit
if __name__ == "__main__":
    # Run FastAPI in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
    fastapi_thread.start()

    # Run Streamlit
    run_streamlit()
