from src.pdf_loader import load_pdf
from src.chunker import clean_text

pdf_path = "data/sample.pdf"

raw_text = load_pdf(pdf_path)

cleaned_text = clean_text(raw_text)

print(cleaned_text[:1000])