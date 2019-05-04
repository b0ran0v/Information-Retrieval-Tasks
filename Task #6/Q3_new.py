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
	cou = 1
	path = './bbc/'+str(folder)
	if(os.path.isdir(path)):
		files = os.listdir(path)
		for file in files:
			if(cou==51):
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
				key = (word,document_dictionary[word]/word_count)
				tf_matrix[key] = str(file)+'_'+str(folder)
			cou+=1
	cou+=1	

#Computing IDF
for key in tf_matrix:
	count = 0
	for key1 in tf_matrix:
		if(key1[0]==key[0]):
			count+=1
	idf = 1 + math.log(document_count/count)
	tfidf_matrix[key[0],key[1]*idf]=str(file)+'_'+str(folder)
