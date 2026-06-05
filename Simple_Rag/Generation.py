from rag import retrieve
from vector import LANGUAGE_MODEL
import ollama

input_query = "What is Artificial Intelligence?"

retrieved_knowledge = retrieve(input_query)

print('Retrieved knowledge:')
for chunk, similarity in retrieved_knowledge:
    print(f"Chunk: {chunk} | Similarity: {similarity:.4f}")

instruction_prompt = f'''You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{'\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])}
'''
stream = ollama.chat(
  model=LANGUAGE_MODEL,
  messages=[
    {'role': 'system', 'content': instruction_prompt},
    {'role': 'user', 'content': input_query},
  ],
  stream=True,
)

print("=" * 50)
print('Chatbot response:')
print("=" * 50)
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
