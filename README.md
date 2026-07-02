# AI Learning Buddy KAVYA

A small Streamlit learning assistant powered by Google's Gemini model. It can
explain concepts, provide real-life examples, generate quizzes, and answer
free-form questions.

## Requirements

- Python 3.10 or newer
- A [Google AI Studio](https://aistudio.google.com/app/apikey) API key

## Run locally

1. Clone the repository and enter its directory.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Set your Gemini API key:

   ```powershell
   $env:GOOGLE_API_KEY="your_api_key"
   ```

5. Start the app:

   ```powershell
   streamlit run app.py
   ```

Open the local URL shown by Streamlit, usually `http://localhost:8501`.

## Security

Never commit API keys. The `.env` file and Streamlit secrets file are ignored
by Git. If a key has previously appeared in source code, revoke it and create a
new one before publishing the repository.
