import google.generativeai as genAI
from langchain_huggingface import HuggingFaceEmbeddings

# Configure the Google Generative AI with your API key
genAI.configure(api_key="YOUR_API_KEY")

# Initialize the generative model (Gemini 1.5 Flash)
model = genAI.GenerativeModel("gemini-1.5-flash")

# Set up embeddings using Hugging Face's MiniLM model for text representation
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
