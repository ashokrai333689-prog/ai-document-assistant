# from src.pdf_loader import load_pdf

# pdf_path = "data/sample.pdf"

# text = load_pdf(pdf_path)

# print(text[:1000])

# from src.pdf_loader import load_pdf
# from src.chunker import clean_text

# pdf_path = "data/sample.pdf"

# raw_text = load_pdf(pdf_path)

# cleaned_text = clean_text(raw_text)

# print(cleaned_text[:1000])

from src.pdf_loader import load_pdf
from src.chunker import clean_text

pdf_path = "data/sample.pdf"

raw_text = load_pdf(pdf_path)

cleaned_text = clean_text(raw_text)

print("\n RAW TEXT:\n")
print(raw_text[:500])

print("\n CLEANED TEXT:\n")
print(cleaned_text[:500])