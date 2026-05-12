from pypdf import PdfReader


def load_pdf(file_path):
    reader = PdfReader(file_path)

    # Handle encrypted PDFs
    if reader.is_encrypted: # Checks if the PDF is encrypted.
        reader.decrypt("") # Attempts to decrypt PDFs with an empty password.

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted: # Prevents crashes from pages with no text.
            text += extracted

    return text