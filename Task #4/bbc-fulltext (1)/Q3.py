import os
import re
import nltk
import string
import math
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

dictionary = dict()
unique_words = []
total_articles_num = 0
articles_class_counts = dict()

def percentage_count(word, clas):
	count_w_c = 0
	count_c = 0
	for key in dictionary:
		if(dictionary[key]==clas):
			for w in key.split():
				count_c+=1
				if(w==word):
					count_w_c+=1
	numerator = count_w_c + 1
	denominator = count_c + len(unique_words)
	return float(numerator)/float(denominator)




def process_data():
	global stop
	global dictionary
	global unique_words
	global total_articles_num
	global articles_class_counts
	folders = os.listdir('./bbc')
	for folder in folders:
		path = './bbc/'+str(folder)
		if(os.path.isdir(path)):
			splited = path.split(os.sep)
			class_name = splited[len(splited)-1]
			if(class_name not in articles_class_counts):
				articles_class_counts[class_name] = 0
			files = os.listdir(path)
			for file in files:
				articles_class_counts[class_name] += 1
				total_articles_num+=1
				file_item = open(path+'/'+file)
				content = file_item.read().split()
				new_content = ''
				#Deleting stop words
				for word in content:
					if(word.lower() not in stop):
						new_content+=word.lower()+' '
				#Removing punctuation
				for c in string.punctuation:
					new_content = new_content.replace(c,'')
				new_content = new_content[:-1]
				#Did this word come before?
				for temp in new_content.split(' '):
					if(temp not in unique_words):
						unique_words.append(temp)
				dictionary[new_content] = class_name


process_data()
print('Finished processing data.')

article = open('article_tech.txt')
content = article.read().split()
new_content = ''
for word in content:
	if(word.lower() not in stop):
		new_content+=word.lower()+' '
	for c in string.punctuation:
		new_content = new_content.replace(c,'')
new_content = new_content[:-1]


max_value = float("-inf")
max_key = ''
for key in articles_class_counts:
	result = 0
	result = result + math.log10(float(articles_class_counts[key])/float(total_articles_num))
	for word in new_content.split():
		a = percentage_count(word, key)
		result = result + math.log10(a)
	if(max_value<result):
		max_value = result
		max_key = key
	print(key+":"+str(result))
print('Classified as:'+max_key)










