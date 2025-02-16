from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0.5)
result = model.invoke("What is the capital of France?")
print(result.content)

model = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0.7)
result = model.invoke("Tell me a joke.")
print(result.content)

model = ChatAnthropic(model="claude-3-haiku-20240307", temperature=1.5, max_completion_tokens=10)
result = model.invoke("What is the meaning of life?")
print(result.content)