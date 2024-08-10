import fitz
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import string
from nltk.stem import WordNetLemmatizer

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
                lemmatized_Word = lemmatizer.lemmatize(word,pos)
                filtered_words.append(lemmatized_Word)
    return filtered_words

def text_extracting_function(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def query_check_function(text, query_process):
    sentences = sent_tokenize(text)
    relevant_Sentence = []
    for sent in sentences:
        sentence_words = query_processor_function(sent)
        if any(word in sentence_words for word in query_process):
            relevant_Sentence.append(sent)
    return relevant_Sentence

def main():
    pdf_path = "data.pdf"
    query = input("Enter a query: ").lower()
    query_process = query_processor_function(query)
    text_extract = text_extracting_function(pdf_path)

    relevant_info = query_check_function(text_extract, query_process)

    if relevant_info:
        print("\nRelevant content for the Query:")
        for content in relevant_info:
            print(content)
    else:
        print("No relevant content found.")


if __name__ == "__main__":
    main()