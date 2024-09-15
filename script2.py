import fitz  
import sys  
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy
import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


load_dotenv()
key = os.getenv('key')
genai.configure(api_key=key)
model1 = genai.GenerativeModel('gemini-pro')

nlp = spacy.load('en_core_web_sm')
model = SentenceTransformer('all-MiniLM-L6-v2')

def read_pdf_with_fitz(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def split_into_chunks(text, chunk_size=1000):
    chunks = []
    while len(text) > chunk_size:
        split_index = text[:chunk_size].rfind('.') + 1
        if split_index == 0:
            split_index = chunk_size
        chunks.append(text[:split_index])
        text = text[split_index:]
    chunks.append(text)
    return chunks

def find_top_similar_chunks(query, chunks, top_n=4):
    chunk_embeddings = model.encode(chunks)
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, chunk_embeddings)
    similarities = similarities.flatten()
    top_indices = np.argsort(similarities)[::-1][:top_n]
    
    top_chunks = [chunks[index] for index in top_indices]
    return top_chunks, similarities[top_indices]


def gemini_content1(query, chunks):
    prompt_text = f"Document excerpt: {' '.join(chunks)}\nQuery: {query}"
    response = model1.generate_content(prompt_text)
    return response.text


# This takes the first argument (query) passed from the Go program
if len(sys.argv) > 1:
    query1 = sys.argv[1]
else:
    query1 = input("Enter your query: ")  

pdf_file_path = "#2.pdf"

pdf_text = read_pdf_with_fitz(pdf_file_path)
chunks = split_into_chunks(pdf_text)

top_chunks, top_similarities = find_top_similar_chunks(query1, chunks, top_n=1)
print("Top Relevant Chunk(s):")
for chunk1, similarity1 in zip(top_chunks, top_similarities):
    if similarity1>0.70:
        print(f"Chunk: {chunk1}")
        print(f"Similarity Score: {similarity1:.2f}")
        print()
    else:
        print("No relevant content found")

gemini_response1 = gemini_content1(query1, top_chunks)
print("Gemini Enhanced Response:")
print(gemini_response1)
