import re
from langchain_text_splitters import RecursiveCharacterTextSplitter

def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove repeated newlines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks