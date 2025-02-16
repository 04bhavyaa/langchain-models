from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text = "Paris is the capital of France."
vector1 = embedding.embed_query(text)
print(str(vector1))

documents = [
    "Paris is the capital of France.",
    "The Eiffel Tower is in Paris.",
    "France is known for its cuisine."
]
vector2 = embedding.embed_documents(documents)
print(str(vector2))