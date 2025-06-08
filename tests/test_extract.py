from app.extract import extract_text_from_pdf

def test_extract_text_from_pdf():
    text = extract_text_from_pdf("control.pdf")
    assert isinstance(text, str)
    assert len(text) > 10
