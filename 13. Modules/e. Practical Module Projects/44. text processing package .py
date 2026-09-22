# A Program to process text using a custom package for cleaning and analysis

from text_tools import (
    clean_text,
    lowercase,
    word_count,
    character_count,
    sentence_count
)

text = "  Python Modules are useful. They organize code.  "

cleaned_text = clean_text(text)
processed_text = lowercase(cleaned_text)

print("Text:", processed_text)
print("Words:", word_count(processed_text))
print("Characters:", character_count(processed_text))
print("Sentences:", sentence_count(processed_text))

# Explanation:
# The text_tools package separates cleaning and analysis.
# cleaning.py prepares the text.
# analysis.py calculates information about the text.
# The main program combines both stages.

# Real-Life Use:
# Text processing is used in search systems, document processing, analytics, and natural language applications.