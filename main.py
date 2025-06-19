"""
Python Script that loads the embedding model and generates an embedding for one sentence like: 
"Met David, Arsenal Fan" and print out the resulting vector
"""

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [ 
    "Met David, Arsenal Fan", 
    "Had a meeting with Jenn, Loves Knitting",
    "Met Aanu at football networking event, is married"
    ]

stored_embeddings = {}

for sentence in range(len(sentences)):
    embedding = model.encode(sentences[sentence])
    stored_embeddings[sentence] = embedding


for sentence, embedding in stored_embeddings.items():
    print(f"sentence: {sentences[sentence]}")
    print(f"embedding: {embedding}")

