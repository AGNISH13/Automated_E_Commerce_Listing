from utils.load_llm import llm

# Define a function to identify the product from the transcript and object detections
def identify_product(transcript, object_ids):
    # Format the prompt
    prompt = f"""
    You are an AI assistant that identifies the advertised product from visual object detections and textual descriptions.

    Given the following information:

    Transcript of an advertisement:
    {transcript}

    MSCOCO object ids:
    {object_ids}

    Identify the product being advertised in terms of given object ids and rank them from most likely to least likely. Select only the top class and return the output class name as a python list of strings.
    """
    # Generate the response
    response = llm(prompt)
    return response