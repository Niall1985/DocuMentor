# # import fitz  # PyMuPDF
# # from sentence_transformers import SentenceTransformer
# # from sklearn.metrics.pairwise import cosine_similarity
# # import numpy as np
# # import spacy

# # # Load spaCy model
# # nlp = spacy.load('en_core_web_sm')

# # # Load sentence transformer model
# # model = SentenceTransformer('all-MiniLM-L6-v2')

# # # Function to read text from a PDF file using fitz
# # def read_pdf_with_fitz(file_path):
# #     text = ""
# #     with fitz.open(file_path) as doc:
# #         for page in doc:
# #             text += page.get_text()
# #     return text

# # # Function to split text into chunks (e.g., paragraphs)
# # def split_into_chunks(text, chunk_size=1000):
# #     chunks = []
# #     while len(text) > chunk_size:
# #         split_index = text[:chunk_size].rfind('.') + 1
# #         if split_index == 0:
# #             split_index = chunk_size
# #         chunks.append(text[:split_index])
# #         text = text[split_index:]
# #     chunks.append(text)
# #     return chunks

# # # Function to find the top N similar chunks of text
# # def find_top_similar_chunks(query, chunks, top_n=4):
# #     # Generate embeddings for the chunks
# #     chunk_embeddings = model.encode(chunks)

# #     # Generate embedding for the query
# #     query_embedding = model.encode([query])

# #     # Calculate cosine similarities
# #     similarities = cosine_similarity(query_embedding, chunk_embeddings)

# #     # Flatten the array to get a 1D array
# #     similarities = similarities.flatten()

# #     # Get the indices of the top similar chunks
# #     top_indices = np.argsort(similarities)[::-1][:top_n]

# #     # Display the top results
# #     print("Top Similar Chunks:")
# #     for index in top_indices:
# #         print(f"Chunk: {chunks[index]}")
# #         print(f"Similarity Score: {similarities[index]:.2f}")
# #         print()

# # # File path to the PDF document
# # pdf_file_path = "C:\\Users\\Niall Dcunha\\Desktop\\3rd SEM ka tatti\\docs\\disease_information_data.pdf"

# # # Read the PDF file using fitz
# # pdf_text = read_pdf_with_fitz(pdf_file_path)

# # # Split the text into chunks
# # chunks = split_into_chunks(pdf_text)

# # # User query
# # query = "information about diabetes"

# # # Find and display the top 4 similar chunks
# # find_top_similar_chunks(query, chunks, top_n=1)










# # from flask import Flask, request, render_template, redirect
# # import fitz
# # from nltk.corpus import stopwords, wordnet
# # from nltk.tokenize import word_tokenize, sent_tokenize
# # import nltk
# # import string
# # from nltk.stem import WordNetLemmatizer
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from sklearn.metrics.pairwise import cosine_similarity

# # app = Flask(__name__)

# # nltk.download('punkt')
# # nltk.download('stopwords')
# # nltk.download('wordnet')
# # nltk.download('averaged_perceptron_tagger')

# # lemmatizer = WordNetLemmatizer()

# # def get_wordnet_tag(treebank_tag):
# #     if treebank_tag.startswith('J'):
# #         return wordnet.ADJ
# #     elif treebank_tag.startswith('V'):
# #         return wordnet.VERB
# #     elif treebank_tag.startswith('N'):
# #         return wordnet.NOUN
# #     elif treebank_tag.startswith('R'):
# #         return wordnet.ADV
# #     else:
# #         return wordnet.NOUN
    
# # def query_processor_function(query):
# #     token = word_tokenize(query)
# #     stopword = set(stopwords.words('english'))
# #     filtered_words = []
# #     for word, wordtag in nltk.pos_tag(token):
# #         if word not in string.punctuation:
# #             if word.lower() not in stopword:
# #                 pos = get_wordnet_tag(wordtag)
# #                 lemmatized_Word = lemmatizer.lemmatize(word, pos)
# #                 filtered_words.append(lemmatized_Word)
# #     return filtered_words

# # def text_extracting_function(pdf):
# #     text = ""
# #     doc = fitz.open(stream=pdf.read(), filetype="pdf")
# #     for page in doc:
# #         text += page.get_text('text')
# #     return text

# # def retrieve_relevant_passages(text, query, top_n=2):
# #     sentences = sent_tokenize(text)
# #     vectorizer = TfidfVectorizer(stop_words='english')
# #     tfidf_matrix = vectorizer.fit_transform(sentences + [query])
# #     similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
# #     relavant_index = similarities[0].argmax()
# #     start_index = max(relavant_index - 1, 0)
# #     end_index = min(relavant_index + top_n, len(sentences))
# #     return sentences[start_index:end_index]

# # def response_generation_func(relevant_passages, query):
# #     response = f"Based on your query: '{query}', here is some relevant content from the document:"
# #     print("\n")
# #     for passage in relevant_passages:
# #         response += f"\n{passage}\n"
# #     return response

# # @app.route('/', methods=['GET', 'POST'])
# # def upload_file():
# #     if request.method == 'POST':
# #         if 'file' not in request.files:
# #             return redirect(request.url)
# #         file = request.files['file']
# #         if file.filename == '':
# #             return redirect(request.url)
# #         if file and file.filename.lower().endswith('.pdf'):
# #             query = request.form.get('query', '').lower()
# #             text_extract = text_extracting_function(file)
# #             relevant_passages = retrieve_relevant_passages(text_extract, query)
# #             response = response_generation_func(relevant_passages, query)
# #             return render_template('upload.html', results=[response])
# #     return render_template('upload.html')

# # if __name__ == "__main__":
# #     app.run(debug=True)


# # # Retrieve PDF files from environment variable
# # pdf_files = os.getenv('PDF_FILES').split(',')


# # import numpy as np

# # def f(x):
# #     return np.sin(x) #passing the function sin(x)

# # def trapezoidal_with_simpson(a, b, n):
# #     if n % 2 != 0:
# #         raise ValueError("The number of intervals should be an even number.")

# #     h = (b - a) / n
# #     x = np.linspace(a, b, n + 1)
# #     y = f(x)

# #     result = []
# #     integral_using_trap = 0.5 * h * (y[0] + 2 * np.sum(y[1:-1]) + y[-1]) #trapezoidal method formula
    
# #     simpson_integral = 0
# #     for i in range(0, n, 2):
# #         simpson_calculation = (h / 3) * (y[i] + 4 * y[i + 1] + y[i + 2]) #simpson method formula
# #         simpson_integral += simpson_calculation

# #         result.append(simpson_calculation)
# #     print(result)
# #     return integral_using_trap, simpson_integral

# # a = 0
# # b = np.pi
# # n = 4

# # trap_result, simpson_result = trapezoidal_with_simpson(a, b, n)
# # print("Trapezoidal Result:", trap_result)
# # print("Simpson's Result:", simpson_result)
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# # Sample sentence
# sentence = "What is the role of gps systems in agriculture"

# # Downloading stopwords (only needs to be done once)
# nltk.download('punkt')

# # Tokenize the sentence
# words = word_tokenize(sentence)

# # Get the list of English stopwords
# stop_words = set(stopwords.words('english'))

# # Remove stopwords
# filtered_sentence = [word for word in words if word.lower() not in stop_words]

# # Join the filtered words back into a sentence
# filtered_sentence = ' '.join(filtered_sentence)

# print("Original Sentence:", sentence)
# print("Filtered Sentence:", filtered_sentence)


# import google.generativeai as genai

# # Hardcode your API key here
# API_KEY = "AIzaSyCMxlqvYhULYj1v425VJ_j63RcimB5Xhfw"

# # Configure the API with your hardcoded API key
# genai.configure(api_key=API_KEY)

# # Initialize the Gemini model
# model = genai.GenerativeModel('gemini-1.5-flash')

# # Path to the PDF file in the 'files' folder
# file_path = "#1.pdf"
# sample_file = genai.upload_file(path=file_path, display_name="My File PDF")

# # Confirm upload
# print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")


# query = input("Enter: ")

# # Generate content using the uploaded document
# response = model.generate_content([sample_file, query])

# # Print the generated content
# print(response.text)

