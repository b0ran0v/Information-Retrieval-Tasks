import os

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ["the cat is running","the dog is running","this is beautiful day for running", "cats and dogs are home animal"]
tfidf = TfidfVectorizer()
features = tfidf.fit_transform(corpus)
data = pd.DataFrame(features.todense(),columns=tfidf.get_feature_names())
data.to_csv('answer.csv')
