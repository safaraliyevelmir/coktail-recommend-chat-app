# Cocktail Search API

This project allows you to search for cocktail recipes using a FastAPI backend. It utilizes Sentence Transformers for encoding queries and FAISS for fast similarity search. The system returns cocktail names and descriptions based on user input.

## Features

- Search cocktails by name or description.
- Use Sentence Transformers to convert queries into embeddings.
- Fast similarity search with FAISS.
- Web interface powered by FastAPI and Jinja2 templates.

## Installation

Follow the steps below to get your environment set up.

### Requirements

- Python 3.8+
- FAISS (for similarity search)
- Sentence-Transformers
- FastAPI
- Uvicorn (for running the FastAPI app)
- Numpy

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/cocktail-search.git
cd cocktail-search
```

### Step 2: Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate


pip install -r requirements.txt

pip install numpy sentence-transformers faiss-cpu fastapi uvicorn
```

### Step 3: Run the FastAPI Application

```bash
uvicorn app.main:app --reload
```


### Step 5: Access the Web Interface

```bash
Open your browser and navigate to http://127.0.0.1:8000. You'll see a simple interface where you can input your query to search for cocktails.
```


### Step 6: Example Request Cocktail Search with Ingredients


You can request a cocktail search using specific ingredients, such as lime and rum, by posting to the `/chat` endpoint.

Example Request (using `curl`):

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/chat' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "I like cocktails with lime and rum."
}

{
    "response": "I'll remember them for recommendations!"
}
```