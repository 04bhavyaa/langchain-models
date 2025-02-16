from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is the captain of the Indian cricket team.",
    "Messi is a football player who plays for Barcelona.",
    "MS Dhoni is a former captain of the Indian cricket team.",
    "Ronaldo is a football player who plays for Manchester United.",
    "Sachin Tendulkar is a former cricketer who played for India.",
    "Roger Federer is a tennis player from Switzerland.",
    "Jasprit Bumrah is a fast bowler who plays for the Indian cricket team.",
    "Nadal is a tennis player from Spain."
]

query = input("Enter a query: ")

doc_embeddings = embedding.embed_documents(documents) # This isn't efficient for large datasets, hence, vector databases are used in production.
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
index, scores = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(f"Query: {query}")
print(f"Most similar document: {documents[index]}")
print(f"Similarity score: {scores}")

