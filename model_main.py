import queue
import threading
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import string
import time

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

input_queue = queue.Queue()
output_queue = queue.Queue()

def input_string():
    query = input("Enter your query:")
    input_queue.put(query)

def text_extracting_function(pdf_file):
    topic = input_queue.get() 
    
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        content = ""
        for page in reader.pages:
            text = page.extract_text()
            if topic in text:  
                content += text
    
    output_queue.put(content)

def output_string():
    structured_content = ""
    content  = output_queue.get()
    while True:
        if content == "DONE":
            break
        structured_content += content + "\n"
    print("Final Structured output:\n",structured_content)

pdf_files = []

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