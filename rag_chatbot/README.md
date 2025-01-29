# RAG Chatbot

This repository contains the code for a simple Retrieval-Augmented Generation chatbot.

## Installation

1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a MySQL database and user.
4. Update database credentials in `app.py`.

## Usage

1. Run the Flask app: `python app.py`
2. Send POST requests to `/chat` with the user query in JSON format:

```json
{
    "query": "What is the capital of France?"
}