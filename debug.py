import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to read text from a PDF file using fitz
def read_pdf_with_fitz(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Function to split text into chunks (e.g., paragraphs)
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

# Function to find the top N similar chunks of text
def find_top_similar_chunks(query, chunks, top_n=4):
    # Generate embeddings for the chunks
    chunk_embeddings = model.encode(chunks)

    # Generate embedding for the query
    query_embedding = model.encode([query])

    # Calculate cosine similarities
    similarities = cosine_similarity(query_embedding, chunk_embeddings)

    # Flatten the array to get a 1D array
    similarities = similarities.flatten()

    # Get the indices of the top similar chunks
    top_indices = np.argsort(similarities)[::-1][:top_n]

    # Display the top results
    print("Top Similar Chunks:")
    for index in top_indices:
        print(f"Chunk: {chunks[index]}")
        print(f"Similarity Score: {similarities[index]:.2f}")
        print()

# File path to the PDF document
pdf_file_path = "C:\\Users\\Niall Dcunha\\Desktop\\3rd SEM ka tatti\\docs\\disease_information_data.pdf"

# Read the PDF file using fitz
pdf_text = read_pdf_with_fitz(pdf_file_path)

# Split the text into chunks
chunks = split_into_chunks(pdf_text)

# User query
query = "information about diabetes"

# Find and display the top 4 similar chunks
find_top_similar_chunks(query, chunks, top_n=1)
