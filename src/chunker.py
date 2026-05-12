import re


def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove repeated newlines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()