from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.5)
result = model.invoke("What is the capital of France?")
print(result.content)

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)
result = model.invoke("Tell me a joke.")
print(result.content)

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=1.5, max_completion_tokens=10)
result = model.invoke("What is the meaning of life?")
print(result.content)

