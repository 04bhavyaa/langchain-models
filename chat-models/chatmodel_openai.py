from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.5)
result = model.invoke("What is the capital of France?")
print(result.content)

model = ChatOpenAI(model="gpt-4", temperature=0.7)
result = model.invoke("Tell me a joke.")
print(result.content)

model = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=10)
result = model.invoke("What is the meaning of life?")
print(result.content)


'''
    The  ChatOpenAI  class is a subclass of  OpenAI  and inherits all of its methods and
    attributes. It also adds additional functionality specific to chat-based models, such as
    the ability to send and receive messages between the user and the model.
    
    The  model = ChatOpenAI(model="gpt-4")  statement is used to create an instance
    of the ChatOpenAI class with the "gpt-4" model. This model is then used to interact with
    the OpenAI API.
    
    .content  is used to extract the content of the response from the API. The response is
    a dictionary with the following keys: "id", "object", "created", "model", "choices", and
    "usage". The "choices" key contains the actual response from the model, which is then
    printed to the console.

    temperature  is a hyperparameter that controls the randomness of the model's output. A
    higher temperature means the model is more likely to produce more creative and diverse
    responses, while a lower temperature means the model is more likely to produce more
    predictable and repetitive responses.

    factual answers(math,code,facts):0.0-0.3
    balanced responce(general qa,explanation):0.5-0.7
    creative writing, story telling, jokes:0.9-1.2
    maximum randomness(wild ideas, brainstorming):1.5+

    max completion tokens  is a hyperparameter that controls the maximum number of tokens
    that the model can generate in the response. A higher number means the model is more
    likely to generate longer responses, while a lower number means the model is more likely
    to generate shorter responses.

    In summary, this code snippet demonstrates how to use the ChatOpenAI class to interact
    with the OpenAI API and send and receive messages between the user and the model.

'''