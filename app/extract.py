import PyPDF2

def extract_text_from_pdf(pdf_path: str) -> str:
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
