import os
from dotenv import load_dotenv

from app.extract import extract_text_from_pdf
from app.rag_chain import create_qa_chain
from app.ui import launch_gradio_interface

load_dotenv()

import os
from app.extract import extract_text_from_pdf

# Get absolute path to control.pdf
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(BASE_DIR, "control.pdf")

# Use absolute path
pdf_text = extract_text_from_pdf(pdf_path)


pdf_text = extract_text_from_pdf("control.pdf")
qa_chain = create_qa_chain(pdf_text)
launch_gradio_interface(qa_chain)
