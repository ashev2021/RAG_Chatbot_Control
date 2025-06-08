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


load_dotenv()


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
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
