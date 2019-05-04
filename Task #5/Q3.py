import os
import re
import nltk
import string
import math
import csv
import random
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

dictionary_genre = dict()
dictionary_origin = dict()
unique_words = []
total_film_count = 0
film_genre_count = dict()
film_origin_count = dict()

random_film = ''

def percentage_count_origin(word, clas):
	count_w_c = 0
	count_c = 0
	for key in dictionary_origin:
		if(dictionary_origin[key]==clas):
			for w in key.split():
				count_c+=1
				if(w==word):
					count_w_c+=1
	numerator = count_w_c + 1
	denominator = count_c + len(unique_words)
	return float(numerator)/float(denominator)

def percentage_count_genre(word, clas):
	count_w_c = 0
	count_c = 0
	for key in dictionary_genre:
		if(dictionary_genre[key]==clas):
			for w in key.split():
				count_c+=1
				if(w==word):
					count_w_c+=1
	numerator = count_w_c + 1
	denominator = count_c + len(unique_words)
	return float(numerator)/float(denominator)


def process_data():
	global stop
	global dictionary_genre
	global dictionary_origin
	global unique_words
	global total_film_count
	global film_genre_count
	global film_origin_count
	global random_film
	file = open("wiki_movie_plots_deduped.csv","r")
	with open('wiki_movie_plots_deduped.csv') as csv_file:
		file = csv.reader(csv_file)
		lines = list(file)
	total_film_count=1
	for i in range(1,len(lines)):
		random_index = random.randint(0,len(lines)-1)
		line = lines[random_index]
		if(line[2] not in film_origin_count):
			film_origin_count[line[2]] = 1
		else:
			film_origin_count[line[2]] += 1
		if(line[5] not in film_genre_count):
			film_genre_count[line[5]] = 1
		else:
			film_genre_count[line[5]] += 1
		plot = line[7]
		for i in range(0,10):
			plot = plot.strip('\['+str(i)+'\]')
		plot = plot.split()
		new_content = ''
		#Deleting stop words
		for word in plot:
			if(word.lower() not in stop):
				new_content+=word.lower()+' '
		new_content = new_content[:-1]
		#Removing punctuation
		for c in string.punctuation:
			new_content = new_content.replace(c,'')
		#Did this word come before?
		for temp in new_content.split(' '):
			if(temp not in unique_words):
				unique_words.append(temp)
		dictionary_origin[new_content] = line[2]
		dictionary_genre[new_content] = line[5]
		if(total_film_count==2000):
			random_film = lines[random.randint(0,len(lines)-1)]
			break
		total_film_count+=1

process_data()
print('Finished processing data.')


print(random_film)
plot = random_film[7]
for i in range(0,10):
	plot = plot.strip('\['+str(i)+'\]')
plot = plot.split()
new_content = ''
for word in plot:
	if(word.lower() not in stop):
		new_content+=word.lower()+' '
	for c in string.punctuation:
		new_content = new_content.replace(c,'')
new_content = new_content[:-1]


max_value = float("-inf")
max_key = ''
for key in film_genre_count:
	result = 0
	result = result + math.log10(float(film_genre_count[key])/float(total_film_count))
	for word in new_content.split():
		a = percentage_count_genre(word, key)
		result = result + math.log10(a)
	if(max_value<result):
		max_value = result
		max_key = key
	# print(key+":"+str(result))
print('Classified as:'+max_key)


max_value = float("-inf")
max_key = ''
for key in film_origin_count:
	result = 0
	result = result + math.log10(float(film_origin_count[key])/float(total_film_count))
	for word in new_content.split():
		a = percentage_count_origin(word, key)
		result = result + math.log10(a)
	if(max_value<result):
		max_value = result
		max_key = key
	# print(key+":"+str(result))
print('Classified as:'+max_key)
