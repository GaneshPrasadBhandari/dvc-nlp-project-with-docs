# Featurization stage

```python
corpus = [
    "zebra apple ball cat",
    "ball cat dog elephant",
    "very very unique"
]

# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(corpus)
# print(X.toarray())
# print(vectorizer.get_feature_names_out())



max_features = 100
ngrams = 3 #tri gram

vectorizer = CountVectorizer(max_features=max_features, ngram_range=(1, ngrams))
X = vectorizer.fit_transform(corpus)
print(X.toarray())
print(vectorizer.get_feature_names_out())

```