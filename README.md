# RAG Pipeline


<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/35aacf93-12f8-4920-87d4-7e62d7fd97ff" />

A practical Retrieval-Augmented Generation (RAG) project with two learning paths:

- `Simple_Rag/`: a small modular Python implementation that separates data loading, embeddings, retrieval, similarity scoring, and generation into individual files.
- `Notebook/document.ipynb`: the earlier notebook-first walkthrough for experimenting with LangChain, ChromaDB, document loading, chunking, and retrieval.

The latest simple version is no longer written as one single notebook. It uses a modular coding style so each part of the RAG flow can be read, changed, tested, and reused independently.

## Features

- Load local text data from `Data/Text_files/`.
- Generate embeddings with Ollama.
- Store embeddings in a simple in-memory vector database.
- Compute cosine similarity for retrieval.
- Retrieve top matching chunks for a natural-language query.
- Generate an answer with an Ollama language model using only retrieved context.
- Keep the original notebook workflow for PDF/text ingestion, LangChain, and ChromaDB experiments.

## Project Structure

```text
RAG_Pipeline/
├── Data/
│   ├── Pdf_files/          # Local PDF documents, ignored by Git
│   └── Text_files/         # Local text documents, ignored by Git
├── Notebook/
│   ├── document.ipynb      # Original notebook RAG walkthrough
│   └── vector_store/       # Generated Chroma index, ignored by Git
├── Simple_Rag/
│   ├── dataset.py          # Loads text data line by line
│   ├── vector.py           # Builds the in-memory vector database
│   ├── cosine.py           # Cosine similarity helper
│   ├── rag.py              # Retrieval logic
│   └── Generation.py       # Final answer generation with retrieved context
├── main.py                 # Minimal Python entry point
├── pyproject.toml          # Project metadata and dependencies
├── uv.lock                 # Locked dependency graph
├── .gitignore
└── README.md
```

## Requirements

- Python 3.14 or newer
- `uv` for dependency management
- Ollama installed and running locally
- Local text or PDF files for ingestion

The simple modular pipeline uses these Ollama models:

```text
hf.co/CompendiumLabs/bge-base-en-v1.5-gguf
hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```

Pull the models before running the simple pipeline if they are not already available:

```bash
ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf
ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```

## Installation

Install dependencies from the project root:

```bash
uv sync
```

## Simple Modular RAG Usage

1. Add a local text file at `Data/Text_files/text2.txt`.
2. Make sure Ollama is running.
3. Run the generation module:

```bash
uv run python Simple_Rag/Generation.py
```

The simple pipeline works like this:

1. `dataset.py` loads text lines from the local dataset file.
2. `vector.py` embeds each non-empty chunk and stores it in `VECTOR_DB`.
3. `cosine.py` calculates similarity between query and chunk embeddings.
4. `rag.py` retrieves the most similar chunks.
5. `Generation.py` sends the retrieved context and user query to the language model.

Example query from `Generation.py`:

```python
input_query = "What is Artificial Intelligence?"
```

## Notebook Usage

Start Jupyter with the project environment:

```bash
uv run jupyter notebook
```

Open the original notebook:

```text
Notebook/document.ipynb
```

Notebook workflow:

1. Add local documents to `Data/Text_files/` or `Data/Pdf_files/`.
2. Open `Notebook/document.ipynb`.
3. Run the notebook cells in order.
4. Review the generated chunks and embeddings.
5. Store the embeddings in ChromaDB.
6. Query the retriever to fetch relevant document context.

## Git Ignore Policy

Local source documents, secrets, generated vector stores, notebook checkpoints, and Python caches are ignored because they can be large, private, or reproducible.

Ignored project paths include:

- `.env`
- `.venv/`
- `Data/Pdf_files/`
- `Data/Text_files/`
- `*.pdf`
- `*.txt`
- `Notebook/vector_store/`
- `Simple_Rag/vector_store/`
- `Simple_Rag/.cache/`
- `.ipynb_checkpoints/`

## Notes

- The simple modular code currently uses an absolute path in `Simple_Rag/dataset.py`. If the project is moved to another machine, update that path or convert it to a relative path.
- `Simple_Rag/vector.py` builds the vector database at import time, so running `Generation.py` will first load and embed the dataset.
- Chroma vector store files from the notebook are generated artifacts and should be rebuilt locally instead of committed.
- Keep source documents out of version control unless they are small, public, and intentionally part of the project.

## Notebook Updates

Recent changes to `Notebook/document.ipynb`:

- The notebook loads environment variables from the project root `.env`.
- The setup cell reads `GOOGLE_API_KEY` first and falls back to `GEMINI_API_KEY`.
- You can override the Gemini model name with `GEMINI_MODEL` in your `.env` file.
- The LLM setup cell no longer auto-runs generation.
- Retriever and context assembly handle both dict outputs and Document-like objects.
