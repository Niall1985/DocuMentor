Here's a detailed README for your **DocuMentor** project:

---

# DocuMentor

DocuMentor is a tool designed to handle document analysis and retrieval with both multi-threaded and sequential processing. The application reads content from multiple PDF files, allowing users to query information either via a high-performance multi-threaded approach or a simpler sequential approach, with both modes delivering responses through a user-friendly web interface.

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
   - [Go Requirements](#go-requirements)
   - [Python Requirements](#python-requirements)
   - [JavaScript Requirements](#javascript-requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [License](#license)

---

## Features

- Supports multi-threaded document processing for faster response times.
- Simple sequential document processing for resource-constrained scenarios.
- Frontend built with React to provide an intuitive user experience.
- Allows users to switch between threaded and non-threaded modes and view relevant information from the uploaded documents.
- Visual feedback for loading and error handling.

## Project Structure

```
DocuMentor/
├── frontend/
│   ├── node_modules/
│   ├── public/
│   └── src/
│       ├── assets/
│       ├── components/
│       │   ├── Content.jsx
│       │   ├── ResponseContainer.jsx
│       │   ├── Response.jsx
│       │   ├── UserEntry.jsx
│       │   ├── WithoutThread.jsx
│       │   └── WithThread.jsx
│       ├── Context/
│       ├── hooks/
│       │   └── useInfo.js
│       ├── App.jsx
│       ├── index.css
│       └── main.jsx
├── mult/
│   ├── #1.pdf
│   ├── #2.pdf
│   ├── #3.pdf
│   ├── #4.pdf
│   ├── #5.pdf
│   └── #6.pdf
├── seq/
├── .env
├── .gitignore
├── debug.py
├── go.mod
├── LICENSE
├── main.go
├── py1.py
├── py2.py
├── py3.py
├── py4.py
├── py5.py
├── py6.py
├── test2.py
├── README.md
└── vite.config.js
```

## Requirements

### Go Requirements

- **Go** (version 1.16 or later)
  - The main Go file (`main.go`) provides backend APIs for handling multi-threaded and sequential document processing. Install Go by following the instructions [here](https://golang.org/doc/install).

### Python Requirements

- **Python** (version 3.7 or later)
  - Install Python packages by running:
    ```bash
    pip install PyMuPDF, fitz, scikit-learn, Sentence Transformers, Warnings, numpy, spacy
    ```
  - **PyMuPDF** (`fitz`): For handling PDF processing.

  
  Each `pyX.py` file in the project is designed to handle a portion of the PDF processing tasks.

### JavaScript Requirements

- **Node.js** (version 14 or later)
  - Install dependencies for the React frontend by running:
    ```bash
    npm install
    ```
  - Key dependencies:
    - **React**: Used for building the frontend.
    - **react-hot-toast**: For displaying notifications.
    - **react-icons**: For including icons in the frontend.
    - **Vite**: Bundler used for frontend development and building.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/DocuMentor.git
   cd DocuMentor
   ```

2. **Setup Go Backend:**
   - Navigate to the root directory containing `main.go`.
   - Run the Go server:
     ```bash
     go run main.go
     ```

3. **Setup Python Scripts:**
   - Ensure all Python dependencies are installed:
     ```bash
   pip install PyMuPDF, fitz, scikit-learn, Sentence Transformers, Warnings, numpy, spacy
     ```

4. **Setup Frontend (React):**
   - Navigate to the `frontend` directory.
   - Install Node.js dependencies:
     ```bash
     npm install
     ```
   - Start the frontend:
     ```bash
     npm run dev
     ```

## Usage

1. **Starting the Application:**
   - Run the backend services (Go and Python) as described in the installation steps.
   - Start the frontend.

2. **Navigating the UI:**
   - Open your browser and go to `http://localhost:5173` to access the frontend.
   - Enter your query in the input field.
   - View responses in the response container and monitor for loading or error messages.

3. **Environment Variables:**
   - Configure your `.env` file for any required environment variables.

## License

This project is licensed under the GNU License.

---