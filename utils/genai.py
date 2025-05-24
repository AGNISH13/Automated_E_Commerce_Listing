# Import required libraries
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('google_api_key')) # Set your Google API key here

# Initialize the Google Generative AI model (Gemini)
llm = GoogleGenerativeAI(
    model="gemini-2.0-flash-lite", # gemini-1.5-pro
    google_api_key=os.getenv('google_api_key')
)