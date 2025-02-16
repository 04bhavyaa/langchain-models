from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
result = llm.invoke("What is the capital of France?") 
print(result) 

# invoke is a method that sends a prompt to the model and returns the response.
# load_dotenv() loads the environment variables from the .env file.
# this is a simple example of using llm models.
# LLMs are language models that can be used to generate text, answer questions, and more. They take strings as input and return strings as output.
# OpenAI is one of the most popular LLMs, and it has a wide range of models that can be used for different tasks.
# In this example, we are using the gpt-3.5-turbo-instruct model to answer the question "What is the capital of France?".
# The result is the response from the model: "The capital of France is Paris."
# LLMs are now an old story, chat models are traditionally newer and more powerful.