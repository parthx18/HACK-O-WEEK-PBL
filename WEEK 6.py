#Week 6: Entity Extraction for Dates & Courses
#The Goal: Instead of just knowing a user asked about an exam, you want to extract which exam (CS101) and which semester (SEM 5). This is called Named Entity Recognition (NER).

#The Technical Implementation (spaCy)
#We will use spaCy’s Matcher or a custom NER model to pull specific patterns from the student's query.

#Python
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Define patterns for Course Codes (e.g., CS101) and Semesters (e.g., SEM 5)
patterns = [
    [{"LOWER": "sem"}, {"IS_DIGIT": True}],
    [{"TEXT": {"REGEX": "^[A-Z]{2,3}\d{3}$"}}] # Matches CS101, MAT202
]
matcher.add("STUDENT_INFO", patterns)

def extract_entities(text):
    doc = nlp(text)
    matches = matcher(doc)
    entities = {"semester": None, "course": None}
    
    for match_id, start, end in matches:
        span = doc[start:end]
        if "sem" in span.text.lower():
            entities["semester"] = span.text
        else:
            entities["course"] = span.text
    return entities

# Example: "When is the CS101 exam for SEM 3?" 
# Output: {'semester': 'SEM 3', 'course': 'CS101'}
