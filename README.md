# Hayek RAG

A specialized chat application focused on Friedrich August von Hayek, implementing Retrieval-Augmented Generation (RAG)
to provide contextually relevant responses based on Hayek's works.

## Description

Hayek RAG is a project that allows users to upload PDF documents about Friedrich August von Hayek, processes them to
generate embeddings, and stores this information in a MongoDB database. The application uses these embeddings to
implement RAG, enhancing the chat experience by providing responses with relevant context from Hayek's works. Future
plans include fine-tuning the model to further improve its understanding of Hayek's philosophy and economic theories.

## Features

- PDF document upload and processing
- Text extraction and chunking
- Embedding generation using VoyageAI
- MongoDB storage for documents and embeddings
- RAG-powered chat interface
- Context-aware responses based on Hayek's works

## Installation

### Prerequisites

- Python 3.12 or higher
- MongoDB instance (local or Atlas)
- VoyageAI API key

### Setting up the environment

1. Clone the repository:
   ```bash
   git clone https://github.com/fedeegmz/hayek-rag.git
   cd hayek-rag
   ```

2. Create a virtual environment and install dependencies using `uv`:
   ```bash
   uv sync
   ```

3. Activate a virtual environment:
   ```bash
   source .venv/bin/activate  # On Linux/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```

### Configuration

Create a `.env` file in the project root with the following variables:

```
MONGODB_URI="your_atlas_connection_string"
EMBEDDING_API_KEY="your_embedding_api_key"
```

## Running the Application

Start the FastAPI server:

```bash
  fastapi dev app/main.py
```

The application will be available at http://localhost:8000

API documentation is available at:

- http://localhost:8000/docs (Swagger UI)

## Project Structure

```
hayek-rag/
├── app/                      # Main application code
│   ├── core/                 # Core configuration
│   ├── document/             # Document processing module
│   │   ├── application/      # Application services
│   │   ├── domain/           # Domain models and interfaces
│   │   └── infrastructure/   # Implementation details
│   ├── shared/               # Shared components
│   │   ├── domain/           # Shared domain models
│   │   └── infrastructure/   # Shared infrastructure
│   └── main.py               # Application entry point
├── notebooks/                # Jupyter notebooks for experimentation
├── temp/                     # Temporary files
├── .env                      # Environment variables (create this file)
├── pyproject.toml            # Project dependencies
├── README.md                 # This file
└── uv.lock                   # Lock file for dependencies
```

## Development

For development, the project uses:

- Ruff and Black for code formatting
- Ruff for linting
- pre-commit for Git hooks

To set up the development environment:

```bash
  pre-commit install
```
