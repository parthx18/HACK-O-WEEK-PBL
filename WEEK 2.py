/*Week 2: Linguistic Preprocessing (spaCy Pipeline)
Don't just remove stop words; understand the grammar. We use Lemmatization to turn "flying," "flew," and "flies" into "fly."
*/
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_query(text):
    doc = nlp(text.lower())
    # Lemmatization + removing 'noise' (punctuation/stopwords)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)
