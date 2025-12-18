import pdfplumber
from docx import Document

def load_text_from_pdf(file):
    """Load text from a PDF file."""
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def load_text_from_docx(file):
    """Load text from a DOCX file."""
    doc = Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text
