
/*Week 3: Semantic Similarity (Sentence-Transformers)
Instead of matching keywords, we use Sentence-BERT (SBERT). This creates a high-dimensional vector for every sentence. The bot will know "How much do I pay?" is the same as "What is the tuition cost?" because their vectors are close together.

Python*/
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

faqs = ["How do I pay tuition?", "Where is the library?", "When are exams?"]
faq_embeddings = model.encode(faqs)

def semantic_search(query):
    query_enc = model.encode(query)
    # Calculate Cosine Similarity
    hits = util.semantic_search(query_enc, faq_embeddings, top_k=1)
    return faqs[hits[0][0]['corpus_id']]
