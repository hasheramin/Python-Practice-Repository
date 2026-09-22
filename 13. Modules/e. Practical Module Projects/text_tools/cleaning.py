# A Program to create text cleaning functions

def clean_text(text):
    return " ".join(text.strip().split())


def lowercase(text):
    return text.lower()