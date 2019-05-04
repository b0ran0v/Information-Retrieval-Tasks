import os
import re
import string
import math
from operator import itemgetter
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

document_abs = dict()
tf_matrix = dict()
tfidf_matrix = dict()

document_count = 0

#TRAINING START

folders = os.listdir('./bbc')
for folder in folders:
	cou = 0
	path = './bbc/'+str(folder)
	if(os.path.isdir(path)):
		files = os.listdir(path)
		for file in files:
			if(cou==10):
				break
			document_count+=1
			word_count = 0
			document_dictionary = dict()
			file_item = open(path+'/'+file)
			content = file_item.read().split()
			new_content = ''
			#Deleting stop words
			for word in content:
				if(word.lower() not in stop):
					new_content+=word.lower()+' '
			new_content = new_content[:-1]
			#Deleting punctuation
			for c in string.punctuation:
				new_content = new_content.replace(c,'')
			for word in new_content.split(' '):
				word_count+=1
				if(word not in document_dictionary):
					document_dictionary[word]=1
				else:
					document_dictionary[word]+=1
			#Counting tf matrix
			for word in document_dictionary:
				key = (word,float(document_dictionary[word])/word_count)
				tf_matrix[key] = str(file)+'_'+str(folder)
			cou+=1

#Counting tfidf matrix
for key in tf_matrix:
	doc_count = 0
	for key1 in tf_matrix:
		if(key1[0]==key[0]):
			doc_count+=1
	idf=1+math.log(document_count/doc_count)
	tfidf_matrix[(key[0],idf*key[1])]=tf_matrix[key]


#Counting distances
for key in tfidf_matrix:
	summ = 0
	doc = tfidf_matrix[key]
	if(doc not in document_abs):
		for key1 in tfidf_matrix:
			if(tfidf_matrix[key1]==doc):
				summ+=key1[1]**2
		document_abs[doc] = math.sqrt(summ)

#TRAINING END


#TEST

query_document_abs = 0
query_tf_matrix = dict()
query_tfidf_matrix = dict()


input_text = raw_input("Enter input: ") 
word_count = 0
document_dictionary = dict()
file_item = open(path+'/'+file)
content = file_item.read().split()
new_content = ''
#Deleting stop words
for word in content:
	if(word.lower() not in stop):
		new_content+=word.lower()+' '
new_content = new_content[:-1]
#Deleting punctuation
for c in string.punctuation:
	new_content = new_content.replace(c,'')
for word in new_content.split(' '):
	word_count+=1
	if(word not in document_dictionary):
		document_dictionary[word]=1
	else:
		document_dictionary[word]+=1
#Counting tf matrix
for word in document_dictionary:
	key = (word,float(document_dictionary[word])/word_count)
	query_tf_matrix[key] = 'test'
#Counting tfidf matrix
for key in query_tf_matrix:
	doc_count = 1
	for key1 in tf_matrix:
		if(key1[0]==key[0]):
			doc_count+=1
	idf=1+math.log(document_count/doc_count)
	query_tfidf_matrix[(key[0],idf*key[1])]='test'


sum = 0
for key in query_tfidf_matrix:
	sum+=key[1]**2
query_document_abs = math.sqrt(sum)

print(query_document_abs)

cos_similarities = dict()
for document in document_abs:
	numerator = 0
	for key in query_tfidf_matrix:
		for key1 in tfidf_matrix:
			if(key[0]==key1[0] and tfidf_matrix[key1]==document):
				numerator+=key[1]*key1[1]
	denominator = document_abs[document]*query_document_abs
	if(denominator!=0):
		cos_similarities[document] = float(numerator)/float(denominator)

count = 0
for k, v in sorted(cos_similarities.items(), key=itemgetter(1), reverse=True):
	print(str(k)+' '+str(v))
	count+=1
	if(count==5):
		break




