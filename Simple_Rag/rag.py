import ollama

from cosine import cosine_similarity
from vector import EMBEDDING_MODEL, VECTOR_DB


def retrieve(query, top_n=3):
  
  query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]

  similarities = []

  for chunk, embedding in VECTOR_DB:
    similarity = cosine_similarity(query_embedding, embedding)
    similarities.append((chunk, similarity))

  similarities.sort(key=lambda x: x[1], reverse=True)
  return similarities[:top_n]
