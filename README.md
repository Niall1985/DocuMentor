# DocuMentor

This Flask application allows users to upload PDF files, enter queries, and retrieve relevant content from the uploaded PDFs. The application uses Natural Language Processing (NLP) techniques to search for the query within the text extracted from the PDF.

## Features

- Upload a PDF file.
- Enter a query to search within the PDF.
- Retrieve and display relevant sentences from the PDF based on the query.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- PyMuPDF (fitz)
- NLTK

## Installation

1. **Clone the repository** (or download the source code):

   ```bash
   git clone https://github.com/Niall1985/DocuMentor.git
   cd <repository-directory>
   ```

2. **Install the required Python packages**:

   ```bash
   pip install Flask PyMuPDF nltk
   ```

3. **Download NLTK resources**:

   The application uses NLTK for tokenization, lemmatization, and part-of-speech tagging. The necessary resources are automatically downloaded by the application, but you can also download them manually using:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   nltk.download('averaged_perceptron_tagger')
   ```

## Running the Application

1. **Run the Flask application**:

   ```bash
   python model.py
   ```

2. **Access the application**:

   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Upload a PDF**:

   Click on the "Choose File" button to select a PDF file from your computer.

2. **Enter a Query**:

   Type your query into the input field and click "Submit."

3. **View Results**:

   The application will display relevant sentences from the uploaded PDF that match your query.

## Code Overview

- **`model.py`**: The main Flask application file.
  - **`query_processor_function(query)`**: Processes the query using tokenization, stopwords removal, and lemmatization.
  - **`text_extracting_function(pdf)`**: Extracts text from the uploaded PDF file.
  - **`query_check_function(text, query_process)`**: Searches for relevant sentences in the extracted text based on the processed query.
  - **`upload_file()`**: Handles file uploads, processes the query, and renders the results.

- **`templates/upload.html`**: HTML template for uploading PDFs and displaying results.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License. See the [LICENSE](LICENSE) file for details.
