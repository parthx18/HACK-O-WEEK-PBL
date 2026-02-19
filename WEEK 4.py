/*Week 4: The Retrieval System (BM25 vs. TF-IDF)
In professional systems, we use BM25 (the algorithm behind Elasticsearch). It’s better than TF-IDF because it doesn't over-penalize long documents.

Python*/
from rank_bm25 import BM25Okapi

corpus = [
    "Admissions require a high school diploma and SAT scores.",
    "The hostel fee includes laundry and three meals a day.",
    "Exam schedules are posted on the student portal monthly."
]
tokenized_corpus = [doc.split(" ") for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)

def retrieve_document(query):
    tokenized_query = query.split(" ")
    return bm25.get_top_n(tokenized_query, corpus, n=1)[0]
