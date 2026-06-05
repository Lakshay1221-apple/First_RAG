import ollama

from dataset import dataset

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

VECTOR_DB = []

def add_chunk_to_database(chunk):
    if not chunk.strip():
        return

    embedding = ollama.embed(
        model=EMBEDDING_MODEL,
        input=chunk
    )['embeddings'][0]

    VECTOR_DB.append((chunk, embedding))


for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk)
    print(f"Chunk {i+1} added to vector database.")