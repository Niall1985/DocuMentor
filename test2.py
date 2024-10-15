import time
import fitz
import sys
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy
import io

# Set stdout encoding to UTF-8 for proper character handling
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load necessary models
nlp = spacy.load('en_core_web_sm')
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to read PDF using PyMuPDF (fitz)
def read_pdf_with_fitz(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Function to split the text into chunks for easier processing
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

# Function to find top N chunks based on cosine similarity with the query
def find_top_similar_chunks(query, chunks, top_n=4):
    chunk_embeddings = model.encode(chunks)
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, chunk_embeddings)
    similarities = similarities.flatten()
    top_indices = np.argsort(similarities)[::-1][:top_n]
    
    top_chunks = [chunks[index] for index in top_indices]
    return top_chunks, similarities[top_indices]

# Main script to handle PDF reading and query processing
def main():
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = "Advantages of Using Computer Application in Agriculture"

    # List of 6 PDF file paths (replace with actual file paths)
    pdf_file_paths = [
        "#1.pdf", "#2.pdf", "#3.pdf", "#4.pdf", "#5.pdf", "#6.pdf"
    ]
    
    # Start timing for all PDFs
    start_time_all = time.time()
    
    # Process each PDF sequentially
    results = []
    for file_path in pdf_file_paths:
        # Start timing for this specific PDF
        start_time_pdf = time.time()
        
        pdf_text = read_pdf_with_fitz(file_path)
        chunks = split_into_chunks(pdf_text)
        top_chunks, top_similarities = find_top_similar_chunks(query, chunks, top_n=1)
        
        relevant_results = []
        for chunk, similarity in zip(top_chunks, top_similarities):
            if similarity > 0.65:
                relevant_results.append(f"Chunk from {file_path}: {chunk}\nSimilarity Score: {similarity:.2f}\n")
            else:
                relevant_results.append(f"Chunk from {file_path}: No relevant content found\n")
        
        results.append(relevant_results)

        # End timing for this specific PDF
        end_time_pdf = time.time()
        time_taken_pdf = end_time_pdf - start_time_pdf
        
        # Print the time taken for this PDF
        print(f"Time taken to process {file_path}: {time_taken_pdf:.2f} seconds\n")

    # End timing for all PDFs
    end_time_all = time.time()
    total_time = end_time_all - start_time_all
    
    # Display top relevant chunks from all PDFs
    print("Top Relevant Chunk(s) from all PDFs:")
    for result in results:
        for chunk in result:
            print(chunk)

    # Display total time taken for processing all PDFs
    print(f"\nTotal time taken for processing all PDFs: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
