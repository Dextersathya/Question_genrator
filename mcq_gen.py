from pdf_text import extracted_text
from langchain.llms import Ollama

# Initialize the Ollama model with the base URL and the specific model
ollama = Ollama(base_url="http://localhost:11434", model="dexter")

# Join the extracted text into a single string if it’s split into sentences
if isinstance(extracted_text, list):
    extracted_text = " ".join(extracted_text)

# Process the entire text with the model
output = ollama(extracted_text)
print(output, flush=True)
