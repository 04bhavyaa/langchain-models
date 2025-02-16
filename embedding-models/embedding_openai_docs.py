from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Paris is the capital of France.",
    "The Eiffel Tower is in Paris.",
    "France is known for its cuisine."
]

result = embedding.embed_documents(documents)
print(str(result))