import queue
import threading
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import nltk
from sentence_transformers import SentenceTransformer
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import fitz
import numpy as np


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

nlp = spacy.load('en_core_web_sm')

model = SentenceTransformer('all-MiniLM-L6-v2')

input_queue = queue.Queue()
output_queue = queue.Queue()

def input_string():
    query = input("Enter your query:")
    input_queue.put(query)

def text_extracting_function(pdf_file):
    topic = input_queue.get() 
    doc = fitz.open(pdf_file) 
    content = ""
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  
        text = page.get_text()  
        if topic in text:  
            content += text

    if not content.strip():
        print(f"Warning: No content extracted from {pdf_file}.")
        output_queue.put("") 
        return
    
    sentences = sent_tokenize(content)

    if not sentences:
        print(f"Warning: No sentences found in {pdf_file}.")
        output_queue.put("")
        return
    
    query_embedding = model.encode([topic])
    sentence_embedding = model.encode(sentences)


    similarities = cosine_similarity(query_embedding, sentence_embedding)[0]
    threshold = 0.5
    relevant_sentences = [sentences[i] for i in np.argsort(similarities)[::-1] if similarities[i] > threshold]
    relevent_content = ' '.join(relevant_sentences)

    output_queue.put(relevent_content)

def output_string():
    structured_content = ""
    while True:
        content  = output_queue.get()
        if content == "DONE":
            break
        structured_content += content + "\n"
    print("Final Structured output:\n",structured_content)

pdf_files = ['disease_information_data.pdf']

threads = []

input_t = threading.Thread(target=input_string)
threads.append(input_t)
input_t.start()

for pdf in pdf_files:
    t = threading.Thread(target=text_extracting_function, args=(pdf,))
    threads.append(t)
    t.start()

output_t = threading.Thread(target=output_string)
threads.append(output_t)
output_t.start()

for t in threads[1:-1]:
    t.join()

output_queue.put("DONE")  

output_t.join()