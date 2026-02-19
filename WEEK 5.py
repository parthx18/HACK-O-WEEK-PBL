/*Week 5: Intent Classification (SVM + Confidence Threshold)
We use a Support Vector Machine (SVM) because it handles high-dimensional text data better than most algorithms. We also add a Null Intent logic: if the probability is too low, the bot asks for clarification.

Python*/
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

# 1. Build the Pipeline
clf = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2))),
    ('svm', SVC(probability=True, kernel='linear'))
])

# 2. Training Data
X = ["apply for admission", "pay my fees", "exam dates", "lost my ID"]
y = ["admission", "finance", "academic", "it_support"]
clf.fit(X, y)

def classify_intent(text):
    probs = clf.predict_proba([text])[0]
    if max(probs) < 0.4: # Confidence Threshold
        return "out_of_scope"
    return clf.predict([text])[0]
