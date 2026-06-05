# RAG Pipeline

A practical Retrieval-Augmented Generation (RAG) project for loading text and PDF documents, splitting them into retrievable chunks, generating semantic embeddings, storing them in a Chroma vector database, and retrieving the most relevant context for a user query.

The project is organized as an interactive notebook-first workflow so each stage of the RAG pipeline can be inspected, tested, and adapted independently.

## Features

- Load plain text files with LangChain `TextLoader`.
- Load PDF documents with LangChain `PyPDFLoader`.
- Batch-ingest files from local directories.
- Split documents into semantic chunks with `RecursiveCharacterTextSplitter`.
- Generate embeddings with Sentence Transformers.
- Persist embeddings and document chunks in ChromaDB.
- Retrieve top matching chunks for a natural-language query.
- Build query context from retrieved documents for downstream LLM use.

## Project Structure

```text
RAG_Pipeline/
├── Data/
│   ├── Pdf_files/          # Local PDF documents, ignored by Git
│   └── Text_files/         # Local text documents, ignored by Git
├── Notebook/
│   ├── document.ipynb      # Main RAG walkthrough
│   └── vector_store/       # Generated Chroma index, ignored by Git
├── main.py                 # Minimal Python entry point
├── pyproject.toml          # Project metadata and dependencies
├── uv.lock                 # Locked dependency graph
└── README.md
```

## Requirements

- Python 3.14 or newer
- `uv` for dependency management
- Local text or PDF files for ingestion

## Installation

Install dependencies from the project root:

```bash
uv sync
```

Start Jupyter with the project environment:

```bash
uv run jupyter notebook
```

Open the main notebook:

```text
Notebook/document.ipynb
```

## Usage

1. Add local documents to `Data/Text_files/` or `Data/Pdf_files/`.
2. Open `Notebook/document.ipynb`.
3. Run the notebook cells in order.
4. Review the generated chunks and embeddings.
5. Store the embeddings in ChromaDB.
6. Query the retriever to fetch relevant document context.

Example query from the notebook:

```python
retriever.retrieve("Explain Encoder-Decoder Architecture?", top_k=3)
```

## Pipeline Overview

The notebook follows this workflow:

1. Create and inspect LangChain `Document` objects.
2. Load individual text files.
3. Load all text files from a directory.
4. Load PDF documents from a directory.
5. Split long documents into overlapping chunks.
6. Generate dense vector embeddings.
7. Store chunks and embeddings in ChromaDB.
8. Retrieve relevant chunks for a query.

## Git Ignore Policy

Local PDF files, text files, and generated vector stores are ignored by Git because they can be large, private, or reproducible from the notebook workflow.

Ignored paths include:

- `Data/Pdf_files/`
- `Data/Text_files/`
- `*.pdf`
- `*.txt`
- `Notebook/vector_store/`

## Notes

- The notebook currently uses absolute local paths. If the project is moved to another machine, update those paths or convert them to relative paths.
- Chroma vector store files are generated artifacts and should be rebuilt locally instead of committed.
- Keep source documents out of version control unless they are small, public, and intentionally part of the project.

## Notebook Updates

Recent changes to `Notebook/document.ipynb` (apply before running the notebook):

- The notebook now loads environment variables from the project root `.env` (works when running from the `Notebook/` folder).
- The setup cell reads `GOOGLE_API_KEY` first and falls back to `GEMINI_API_KEY` for compatibility with different deployment setups.
- You can override the Gemini model name with the `GEMINI_MODEL` variable in your `.env` file (do this if your account does not support the default model).
- The LLM setup cell no longer auto-runs generation; run a separate test cell after confirming a supported `GEMINI_MODEL` to avoid runtime model errors.
- Retriever and context assembly were made more robust: the retriever output may be dicts or Document-like objects, and the code now handles both shapes.

Quick steps to run after pulling these updates:

1. Add your API key to `.env` at the project root. Example:

```
GOOGLE_API_KEY=your_api_key_here
# optionally override model
GEMINI_MODEL=your_preferred_model_name
```

2. Open `Notebook/document.ipynb` and run the setup cells (do not run an LLM generation cell until you confirm the model is available for your key).

3. Run a dedicated test cell to call the LLM after confirming `GEMINI_MODEL` is valid for your account.

If you want, I can also add a small example test cell to the notebook that checks model availability without sending a full generation request.
