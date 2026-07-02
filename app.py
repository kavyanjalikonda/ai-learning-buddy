import os

import google.generativeai as genai
import streamlit as st


st.set_page_config(page_title="AI Learning Buddy KAVYA", page_icon="🎓")
st.title("🎓 AI Learning Buddy KAVYA")

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY is not configured. See the README for setup instructions.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

topic = st.text_input("Enter a topic")
activity = st.selectbox(
    "Choose an activity",
    ["Explain Concept", "Real-Life Example", "Generate Quiz", "Ask Anything"],
)

prompts = {
    "Explain Concept": "Explain {topic} in simple language for a beginner.",
    "Real-Life Example": "Give one simple real-life example of {topic}.",
    "Generate Quiz": "Create 5 multiple-choice questions on {topic}, with answers.",
    "Ask Anything": "{topic}",
}

if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        try:
            with st.spinner("Thinking..."):
                prompt = prompts[activity].format(topic=topic.strip())
                response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as exc:
            st.error(f"Could not generate a response: {exc}")
