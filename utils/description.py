from utils.load_llm import llm

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