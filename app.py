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
from src.chunker import clean_text, chunk_text

pdf_path = "data/sample.pdf"

# Load PDF
raw_text = load_pdf(pdf_path)

# Clean text
cleaned_text = clean_text(raw_text)

# Create chunks
chunks = chunk_text(cleaned_text)

# Print stats
print(f"\nTotal chunks: {len(chunks)}")

# Print first chunk
print("\nFIRST CHUNK:\n")
print(chunks[0])

# Print second chunk
print("\nSECOND CHUNK:\n")
print(chunks[1])

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(f"Length: {len(chunk)}")