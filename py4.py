# # # # import fitz
# # # # import sys
# # # # import time
# # # # import warnings
# # # # from sentence_transformers import SentenceTransformer
# # # # from sklearn.metrics.pairwise import cosine_similarity
# # # # import numpy as np
# # # # import spacy
# # # # import io
# # # # import os

# # # # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# # # # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# # # # with warnings.catch_warnings():
# # # #     warnings.simplefilter("ignore")
# # # #     nlp = spacy.load('en_core_web_sm')
# # # #     model = SentenceTransformer('all-MiniLM-L6-v2')


# # # # def read_pdf_with_fitz(file_path):
# # # #     text = ""
# # # #     with fitz.open(file_path) as doc:
# # # #         for page in doc:
# # # #             text += page.get_text()
# # # #     return text

# # # # def split_into_chunks(text, chunk_size=1000):
# # # #     chunks = []
# # # #     while len(text) > chunk_size:
# # # #         split_index = text[:chunk_size].rfind('.') + 1
# # # #         if split_index == 0:
# # # #             split_index = chunk_size
# # # #         chunks.append(text[:split_index])
# # # #         text = text[split_index:]
# # # #     chunks.append(text)
# # # #     return chunks


# # # # def find_top_similar_chunks(query, chunks, top_n=4):
# # # #     chunk_embeddings = model.encode(chunks)
# # # #     query_embedding = model.encode([query])
# # # #     similarities = cosine_similarity(query_embedding, chunk_embeddings)
# # # #     similarities = similarities.flatten()
# # # #     top_indices = np.argsort(similarities)[::-1][:top_n]
    
# # # #     top_chunks = [chunks[index] for index in top_indices]
# # # #     return top_chunks, similarities[top_indices]


# # # # def process_pdf(file_path, query):
# # # #     pdf_text = read_pdf_with_fitz(file_path)
# # # #     chunks = split_into_chunks(pdf_text)
# # # #     top_chunks, top_similarities = find_top_similar_chunks(query, chunks, top_n=1)
    
# # # #     relevant_results = []
# # # #     for chunk, similarity in zip(top_chunks, top_similarities):
# # # #         if similarity > 0.65:
# # # #             relevant_results.append(f"Chunk from {file_path}: {chunk}\nSimilarity Score: {similarity:.2f}\n")
# # # #         else:
# # # #             relevant_results.append(f"Chunk from {file_path}: No relevant content found\n")
    
# # # #     return relevant_results

# # # # def main():
# # # #     if len(sys.argv) > 1:
# # # #         query = sys.argv[1]
# # # #     else:
# # # #         query = input("Enter your query: ")
    
# # # #     pdf_file_path = "#4.pdf"
    

# # # #     start_time = time.time()

# # # #     results = process_pdf(pdf_file_path, query)

# # # #     end_time = time.time()
# # # #     total_time = end_time - start_time

   
# # # #     print("Top Relevant Chunk(s) from the PDF:")
# # # #     for chunk in results:
# # # #         print(chunk)
# # # #     print("\n")
# # # #     print(f"\nTime taken for processing: {total_time:.2f} seconds")

# # # # if __name__ == "__main__":
# # # #     main()

# # # import fitz
# # # import sys
# # # import time
# # # import warnings
# # # import json
# # # import os
# # # import io
# # # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# # # warnings.filterwarnings("ignore", category=UserWarning)
# # # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# # # from sentence_transformers import SentenceTransformer
# # # from sklearn.metrics.pairwise import cosine_similarity
# # # import numpy as np
# # # import spacy

# # # nlp = spacy.load('en_core_web_sm')
# # # model = SentenceTransformer('all-MiniLM-L6-v2')

# # # def read_pdf_with_fitz(file_path):
# # #     text = ""
# # #     try:
# # #         with fitz.open(file_path) as doc:
# # #             for page in doc:
# # #                 text += page.get_text()
# # #     except Exception as e:
# # #         print(f"Error reading the PDF file: {e}")
# # #         return None
# # #     return text

# # # def split_into_chunks(text, chunk_size=1000):
# # #     """Split text into chunks of specified size, prioritizing sentence boundaries."""
# # #     chunks = []
# # #     while len(text) > chunk_size:
# # #         split_index = text[:chunk_size].rfind('.') + 1
# # #         if split_index == 0:  # No sentence found
# # #             split_index = chunk_size
# # #         chunks.append(text[:split_index])
# # #         text = text[split_index:].lstrip()  # Strip leading whitespace
# # #     if text:  # Append any remaining text as the last chunk
# # #         chunks.append(text)
# # #     return chunks

# # # def find_top_similar_chunks(query, chunks, top_n=4):
# # #     """Find the top N similar chunks based on cosine similarity."""
# # #     chunk_embeddings = model.encode(chunks)
# # #     query_embedding = model.encode([query])
# # #     similarities = cosine_similarity(query_embedding, chunk_embeddings).flatten()
# # #     top_indices = np.argsort(similarities)[::-1][:top_n]
    
# # #     top_chunks = [chunks[index] for index in top_indices]
# # #     return top_chunks, similarities[top_indices]

# # # def process_pdf(file_path, query):
# # #     """Process the PDF to find relevant chunks for the given query."""
# # #     pdf_text = read_pdf_with_fitz(file_path)
# # #     if pdf_text is None:  # Check if text extraction was successful
# # #         return []

# # #     chunks = split_into_chunks(pdf_text)
# # #     top_chunks, top_similarities = find_top_similar_chunks(query, chunks, top_n=2)  # Use top_n=4 for more options

# # #     relevant_results = []
# # #     for chunk, similarity in zip(top_chunks, top_similarities):
# # #         if similarity > 0.65:
# # #             relevant_results.append({
# # #                 "chunk": chunk,
# # #                 "similarity_score": round(float(similarity), 2),  # Ensure float conversion
# # #                 "source": file_path
# # #             })
    
# # #     # If no relevant content found, append a message
# # #     if not relevant_results:
# # #         relevant_results.append({
# # #             "chunk": "No relevant content found",
# # #             "similarity_score": None,
# # #             "source": file_path
# # #         })
    
# # #     return relevant_results

# # # def main():
# # #     """Main function to run the PDF processing."""
# # #     if len(sys.argv) > 1:
# # #         query = sys.argv[1]
# # #     else:
# # #         query = input("Enter your query: ")
    
# # #     pdf_file_path = "#4.pdf"
    
# # #     start_time = time.time()
# # #     results = process_pdf(pdf_file_path, query)
# # #     end_time = time.time()
# # #     total_time = end_time - start_time

# # #     # Prepare final output
# # #     output = {
# # #         "top_relevant_chunks": results,
# # #         "processing_time_seconds": round(total_time, 2)
# # #     }

# # #     # Return results in JSON format
# # #     # print(json.dumps(output, indent=4, ensure_ascii=False))

# # # if __name__ == "__main__":
# # #     main()

# # import fitz
# # import sys
# # import time
# # import warnings
# # import json
# # import os
# # import io
# # import contextlib
# # import logging

# # # Suppress TensorFlow warnings and other warnings
# # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# # warnings.filterwarnings("ignore", category=UserWarning)

# # # Redirect TensorFlow and other warnings to stderr
# # logging.getLogger('tensorflow').setLevel(logging.ERROR)
# # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# # from sentence_transformers import SentenceTransformer
# # from sklearn.metrics.pairwise import cosine_similarity
# # import numpy as np
# # import spacy

# # nlp = spacy.load('en_core_web_sm')
# # model = SentenceTransformer('all-MiniLM-L6-v2')

# # def read_pdf_with_fitz(file_path):
# #     text = ""
# #     try:
# #         with fitz.open(file_path) as doc:
# #             for page in doc:
# #                 text += page.get_text()
# #     except Exception as e:
# #         print(f"Error reading the PDF file: {e}", file=sys.stderr)  # Direct errors to stderr
# #         return None
# #     return text

# # def split_into_chunks(text, chunk_size=1000):
# #     """Split text into chunks of specified size, prioritizing sentence boundaries."""
# #     chunks = []
# #     while len(text) > chunk_size:
# #         split_index = text[:chunk_size].rfind('.') + 1
# #         if split_index == 0:  # No sentence found
# #             split_index = chunk_size
# #         chunks.append(text[:split_index])
# #         text = text[split_index:].lstrip()  # Strip leading whitespace
# #     if text:  # Append any remaining text as the last chunk
# #         chunks.append(text)
# #     return chunks

# # def find_top_similar_chunks(query, chunks, top_n=4):
# #     """Find the top N similar chunks based on cosine similarity."""
# #     chunk_embeddings = model.encode(chunks)
# #     query_embedding = model.encode([query])
# #     similarities = cosine_similarity(query_embedding, chunk_embeddings).flatten()
# #     top_indices = np.argsort(similarities)[::-1][:top_n]
    
# #     top_chunks = [chunks[index] for index in top_indices]
# #     return top_chunks, similarities[top_indices]

# # def process_pdf(file_path, query):
# #     """Process the PDF to find relevant chunks for the given query."""
# #     pdf_text = read_pdf_with_fitz(file_path)
# #     if pdf_text is None:  # Check if text extraction was successful
# #         return []

# #     chunks = split_into_chunks(pdf_text)
# #     top_chunks, top_similarities = find_top_similar_chunks(query, chunks, top_n=2)  # Use top_n=4 for more options

# #     relevant_results = []
# #     for chunk, similarity in zip(top_chunks, top_similarities):
# #         if similarity > 0.65:
# #             relevant_results.append({
# #                 "chunk": chunk,
# #                 "similarity_score": round(float(similarity), 2),  # Ensure float conversion
# #                 "source": file_path
# #             })
    
# #     # If no relevant content found, append a message
# #     if not relevant_results:
# #         relevant_results.append({
# #             "chunk": "No relevant content found",
# #             "similarity_score": None,
# #             "source": file_path
# #         })
    
# #     return relevant_results

# # def main():
# #     """Main function to run the PDF processing."""
# #     if len(sys.argv) > 1:
# #         query = sys.argv[1]
# #     else:
# #         query = input("Enter your query: ")
    
# #     pdf_file_path = "#4.pdf"
    
# #     start_time = time.time()
# #     results = process_pdf(pdf_file_path, query)
# #     end_time = time.time()
# #     total_time = end_time - start_time

# #     # Prepare final output
# #     output = {
# #         "top_relevant_chunks": results,
# #         "processing_time_seconds": round(total_time, 2)
# #     }

# #     # Capture JSON output cleanly without TensorFlow warnings
# #     json_output = json.dumps(output, indent=4, ensure_ascii=False)
# #     print(json_output)  # This will be the only output sent to stdout

# # if __name__ == "__main__":
# #     with contextlib.redirect_stderr(io.StringIO()):  # Redirect stderr to discard warnings
# #         main()

# import fitz
# import sys
# import time
# import warnings
# import json
# import os
# import io
# import logging
# import contextlib
# # Suppress TensorFlow warnings and other warnings
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# warnings.filterwarnings("ignore", category=UserWarning)

# # Set TensorFlow logger to ERROR to suppress its warnings
# logging.getLogger('tensorflow').setLevel(logging.ERROR)
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import spacy

# nlp = spacy.load('en_core_web_sm')
# model = SentenceTransformer('all-MiniLM-L6-v2')

# def read_pdf_with_fitz(file_path):
#     text = ""
#     try:
#         with fitz.open(file_path) as doc:
#             for page in doc:
#                 text += page.get_text()
#     except Exception as e:
#         print(f"Error reading the PDF file: {e}", file=sys.stderr)  # Direct errors to stderr
#         return None
#     return text

# def split_into_chunks(text, chunk_size=1000):
#     """Split text into chunks of specified size, prioritizing sentence boundaries."""
#     chunks = []
#     while len(text) > chunk_size:
#         split_index = text[:chunk_size].rfind('.') + 1
#         if split_index == 0:  # No sentence found
#             split_index = chunk_size
#         chunks.append(text[:split_index])
#         text = text[split_index:].lstrip()  # Strip leading whitespace
#     if text:  # Append any remaining text as the last chunk
#         chunks.append(text)
#     return chunks

# def find_top_similar_chunks(query, chunks, top_n=4):
#     """Find the top N similar chunks based on cosine similarity."""
#     chunk_embeddings = model.encode(chunks)
#     query_embedding = model.encode([query])
#     similarities = cosine_similarity(query_embedding, chunk_embeddings).flatten()
#     top_indices = np.argsort(similarities)[::-1][:top_n]
    
#     top_chunks = [chunks[index] for index in top_indices]
#     return top_chunks, similarities[top_indices]

# def process_pdf(file_path, query):
#     """Process the PDF to find relevant chunks for the given query."""
#     pdf_text = read_pdf_with_fitz(file_path)
#     if pdf_text is None:  # Check if text extraction was successful
#         return []

#     chunks = split_into_chunks(pdf_text)
#     top_chunks, top_similarities = find_top_similar_chunks(query, chunks, top_n=2)  # Use top_n=4 for more options

#     relevant_results = []
#     for chunk, similarity in zip(top_chunks, top_similarities):
#         if similarity > 0.65:
#             relevant_results.append({
#                 "chunk": chunk,
#                 "similarity_score": round(float(similarity), 2),  # Ensure float conversion
#                 "source": file_path
#             })
    
#     # If no relevant content found, append a message
#     if not relevant_results:
#         relevant_results.append({
#             "chunk": "No relevant content found",
#             "similarity_score": None,
#             "source": file_path
#         })
    
#     return relevant_results

# def main():
#     """Main function to run the PDF processing."""
#     if len(sys.argv) > 1:
#         query = sys.argv[1]
#     else:
#         query = input("Enter your query: ")
    
#     pdf_file_path = "#4.pdf"
    
#     start_time = time.time()
#     results = process_pdf(pdf_file_path, query)
#     end_time = time.time()
#     total_time = end_time - start_time

#     # Prepare final output
#     output = {
#         "top_relevant_chunks": results,
#         "processing_time_seconds": round(total_time, 2)
#     }

#     # Print JSON output to stdout
#     print(json.dumps(output, indent=4, ensure_ascii=False))

# if __name__ == "__main__":
#     # Suppress TensorFlow warnings and keep JSON output intact
#     with open(os.devnull, 'w') as devnull:
#         with contextlib.redirect_stderr(devnull):
#             main()


import fitz
import sys
import time
import warnings
import json
import os
import io
# Suppress TensorFlow warnings and other warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore", category=UserWarning)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy

nlp = spacy.load('en_core_web_sm')
model = SentenceTransformer('all-MiniLM-L6-v2')

def read_pdf_with_fitz(file_path):
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading the PDF file: {e}")
        return None
    return text

def split_into_chunks(text, chunk_size=1000):
    """Split text into chunks of specified size, prioritizing sentence boundaries."""
    chunks = []
    while len(text) > chunk_size:
        split_index = text[:chunk_size].rfind('.') + 1
        if split_index == 0:  # No sentence found
            split_index = chunk_size
        chunks.append(text[:split_index])
        text = text[split_index:].lstrip()  # Strip leading whitespace
    if text:  # Append any remaining text as the last chunk
        chunks.append(text)
    return chunks

def find_top_similar_chunks(query, chunks, top_n=4):
    """Find the top N similar chunks based on cosine similarity."""
    chunk_embeddings = model.encode(chunks)
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, chunk_embeddings).flatten()
    top_indices = np.argsort(similarities)[::-1][:top_n]
    
    top_chunks = [chunks[index] for index in top_indices]
    return top_chunks, similarities[top_indices]

def process_pdf(file_path, query):
    """Process the PDF to find relevant chunks for the given query."""
    pdf_text = read_pdf_with_fitz(file_path)
    if pdf_text is None:  # Check if text extraction was successful
        return []

    chunks = split_into_chunks(pdf_text)
    top_chunks, top_similarities = find_top_similar_chunks(query, chunks, top_n=2)  # Use top_n=4 for more options

    relevant_results = []
    for chunk, similarity in zip(top_chunks, top_similarities):
        if similarity > 0.65:
            relevant_results.append({
                "chunk": chunk,
                "similarity_score": round(float(similarity), 2),  # Ensure float conversion
                "source": file_path
            })
    
    # If no relevant content found, append a message
    if not relevant_results:
        relevant_results.append({
            "chunk": "No relevant content found",
            "similarity_score": None,
            "source": file_path
        })
    
    return relevant_results

def main():
    """Main function to run the PDF processing."""
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = input("Enter your query: ")
    
    pdf_file_path = "#4.pdf"
    
    start_time = time.time()
    results = process_pdf(pdf_file_path, query)
    end_time = time.time()
    total_time = end_time - start_time

    # Prepare final output
    output = {
        "top_relevant_chunks": results,
        "processing_time_seconds": round(total_time, 2)
    }

    # Return results in JSON format
    print(json.dumps(output, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
