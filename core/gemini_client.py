import google.generativeai as genai
from config import GEMINI_API_KEY

def initialize_gemini():
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name='models/gemini-2.5-flash')
    return model
