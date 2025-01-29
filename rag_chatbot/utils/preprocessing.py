import re

def clean_text(text):
    """
    removing extra spaces and special characters
    text: The input text string
    """
    text = re.sub(r'\s+', ' ', text)  #remove extra whitespace
    text = text.strip()
    return text

def chunk_text(text, chunk_size=250):
    """
    Split input text into smaller chunk
    text: The input text string
    chunk_size: The desired size of each chunk
    """
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        if chunk:
            chunks.append(chunk)
    return chunks