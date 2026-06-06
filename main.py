from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import SystemMessage, HumanMessage

loader = PyPDFLoader("./story.pdf")
docs = loader.load() #yaha hamne jita contain pdf vo yaha store ho jae ga

# print(docs[0].page_content) #yaha hsirf ek page data print karega
all_text = ""

for doc in docs:
    all_text += doc.page_content + "\n\n"

story = all_text

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

response = model.invoke([
    SystemMessage("<story> " + story + " </story>"),
    HumanMessage("What is the chapter 1 of harsh story?")
])

print(response.text)