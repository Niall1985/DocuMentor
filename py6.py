import fitz
import sys
import time
import warnings
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


with warnings.catch_warnings():
    warnings.simplefilter("ignore")

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


def process_pdf(file_path, query):
    pdf_text = read_pdf_with_fitz(file_path)
    chunks = split_into_chunks(pdf_text)
    top_chunks, top_similarities = find_top_similar_chunks(query, chunks, top_n=1)
    
    relevant_results = []
    for chunk, similarity in zip(top_chunks, top_similarities):
        if similarity > 0.65:
            relevant_results.append(f"Chunk from {file_path}: {chunk}\nSimilarity Score: {similarity:.2f}\n")
        else:
            relevant_results.append(f"Chunk from {file_path}: No relevant content found\n")
    
    return relevant_results


def main():
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = input("Enter your query: ")
    
    pdf_file_path = "#6.pdf"
    
   
    start_time = time.time()

    results = process_pdf(pdf_file_path, query)

    end_time = time.time()
    total_time = end_time - start_time


    print("Top Relevant Chunk(s) from the PDF:")
    for chunk in results:
        print(chunk)
    print("\n")
    print(f"\nTime taken for processing: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
