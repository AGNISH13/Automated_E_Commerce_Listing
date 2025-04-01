# Install necessary libraries
# !pip install langchain-google-genai google-generativeai

# Import required libraries
# from langchain_google_genai import GoogleGenerativeAI

# # Set up the Google API key
# import google.generativeai as genai
# import os

# genai.configure(api_key="AIzaSyDcMqLyOYK6aqYehP1LNa6LRkIzHCMk5ZM")

# # Initialize the Google Generative AI model (Gemini)
# llm = GoogleGenerativeAI(
#     model="gemini-pro",
#     google_api_key="AIzaSyDcMqLyOYK6aqYehP1LNa6LRkIzHCMk5ZM"
# )

from utils.genai import llm

# Define a function to convert transcript to product description
def generate_product_description(transcript):
    prompt = f"""
    The following is a transcript for a product advertisement. Please rewrite it as a professional and engaging product description suitable for listing on an e-commerce website:

    Transcript:
    {transcript}

    Product Description:
    """
    response = llm(prompt)
    return response