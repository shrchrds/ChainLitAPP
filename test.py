from dotenv import load_dotenv
import os
load_dotenv() 

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.5)

print(llm.invoke("What is Embeddings?"))