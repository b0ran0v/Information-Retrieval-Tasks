from nltk.corpus import names
from nltk import NaiveBayesClassifier
from nltk import classify

names = [('Aidar','boy'), ('Marat','boy'), ('Aslan','boy'), ('Nurbek','boy'), ('Nurlan','boy'), ('Rakhman','boy'), ('Rustam','boy'), ('Islam','boy'), ('Daulet','boy'),('Yerkebulan','boy'), ('Gaziz','boy'), ('Aigerim','girl'), ('Aidana','girl'), ('Zhansaya','girl'),('Karina','girl'), ('Zarina','girl'), ('Aiman','girl'), ('Sholpan','girl'), ('Kamshat','girl'),('Aisulu','girl'),('Alina','girl'),
('Rauan','boy'),('Raikhan','girl')]
def gender_features(word):
	return {'last_letter': word[-1]}

featuresets = [(gender_features(n), g) for (n, g) in names]
train_set, test_set = featuresets[:17], featuresets[17:]

nb_classifier = NaiveBayesClassifier.train(train_set)
print(nb_classifier.classify(gender_features('Leyla')))
print(classify.accuracy(nb_classifier, test_set))
print(nb_classifier.show_most_informative_features(5))