from flask import Flask, request, render_template, redirect
import fitz
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import string
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

lemmatizer = WordNetLemmatizer()

def get_wordnet_tag(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
def query_processor_function(query):
    token = word_tokenize(query)
    stopword = set(stopwords.words('english'))
    filtered_words = []
    for word, wordtag in nltk.pos_tag(token):
        if word not in string.punctuation:
            if word.lower() not in stopword:
                pos = get_wordnet_tag(wordtag)
                lemmatized_Word = lemmatizer.lemmatize(word, pos)
                filtered_words.append(lemmatized_Word)
    return filtered_words

def text_extracting_function(pdf):
    text = ""
    doc = fitz.open(stream=pdf.read(), filetype="pdf")
    for page in doc:
        text += page.get_text('text')
    return text

def retrieve_relevant_passages(text, query, top_n=4):
    sentences = sent_tokenize(text)
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences + [query])
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    ranked_sentences = [sentences[i] for i in similarities.argsort()[0][-top_n:]]
    return ranked_sentences

def response_generation_func(relevant_passages, query):
    response = f"Based on your query: '{query}', here is some relevant content from the document:"
    print("\n")
    for passage in relevant_passages:
        response += f"\n{passage}\n"
    return response

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and file.filename.lower().endswith('.pdf'):
            query = request.form.get('query', '').lower()
            text_extract = text_extracting_function(file)
            relevant_passages = retrieve_relevant_passages(text_extract, query)
            response = response_generation_func(relevant_passages, query)
            return render_template('upload.html', results=[response])
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
