import os
import gradio as gr
import PyPDF2

from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader

from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.chat_models import ChatOpenAI




load_dotenv()

# Embedding and vectorestore, then retrieval chaining

def create_qa_chain(text: str):
    document = Document(page_content=text)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    docs = splitter.split_documents([document])

    embedding = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embedding)

    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4")

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
