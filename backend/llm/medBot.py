import google.generativeai as genAI
from llm.constants import *
import pickle
import faiss
import os

# Load the FAISS store and index
current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, "faiss_store.pkl"), "rb") as f:
    store = pickle.load(f)
    store.index = faiss.read_index(os.path.join(current_dir, "docs.index"))

def med_gpt(query=None, treatment=False, user_data=None):
    if treatment and user_data:
        prompt = f"""
        You are a medical assistant. Analyze the following patient data and provide treatment recommendations:
        Please analyze the patient data and return some basic treatment recommendations the following format:

        "Based on the provided data, the would recommended [treatment recommendations]."
        "Respond shortly"

        Patient data: {user_data}
        """
    else:
        context = store.similarity_search(query, k=3)
        prompt =  f"""
        You are a medical assistant specialized in identifying medical disorders or diseases based on symptoms.
        Please analyze the following symptoms and return the name of the most relevant medical disorder or disease in the following format:
        
        "Based on the symptoms provided, the most likely diagnosis is [disorder name]."
        Symptoms: {query}
        Relevant context: {context}

        If the query does not pertain to medical conditions, please respond with a general message.
        """
    try:
        # Generate content based on the prompt
        model = genAI.GenerativeModel('gemini-1.5-flash')  
        response = model.generate_content(prompt) 
        return response.text.replace("*", "") 
    
    except Exception:
        return "An error occurred during processing." 
