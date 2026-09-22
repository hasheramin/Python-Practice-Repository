# A Program to create text analysis functions

def word_count(text):
    return len(text.split())


def character_count(text):
    return len(text)


def sentence_count(text):
    sentences = [sentence for sentence in text.split(".") if sentence.strip()]
    return len(sentences)