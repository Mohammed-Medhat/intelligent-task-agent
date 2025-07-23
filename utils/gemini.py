import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def gemini_chat(prompt, history=None):
    history = history or []
    chat = model.start_chat(history=history)
    response = chat.send_message(prompt)
    return response.text
