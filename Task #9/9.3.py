import os
import re
import string
import math
import csv
import random

movie_names = {}
movie_matrix = {}
movie_normalized_values = {}
avg_film_ratings = {}
tags_genres = {}
film_id = 47
size = 0
max_similar_film_id = 0
max_dot_product = 0

def process_data():
	global movie_names
	global max_dot_product
	global max_similar_film_id
	global film_id
	global movie_normalized_values
	global avg_film_ratings
	global movie_matrix
	global size
	global tags_genres
	#Defining genres
	file = open("./Dataset/movies.csv","r")
	with open('./Dataset/movies.csv') as csv_file:
		file = csv.reader(csv_file)
		lines = list(file)
	for i in range(1,len(lines)):
		movie_names[int(lines[i][0])]=lines[i][1]
		genres = lines[i][2].split('|')
		genre_list = []
		for genre in genres:
			if(genre.lower() not in tags_genres):
				tags_genres[genre.lower()]=size
				size+=1
			genre_list.append(tags_genres[genre.lower()])
		movie_matrix[int(lines[i][0])] = genre_list

	#Defining tags
	file = open("./Dataset/tags.csv","r")
	with open('./Dataset/tags.csv') as csv_file:
		file = csv.reader(csv_file)
		lines = list(file)
	for i in range(1,len(lines)):
		tag = lines[i][2]
		if(tag.lower() not in tags_genres):
			tags_genres[tag.lower()]=size
			size+=1
		if(lines[i][0] in movie_matrix):
			value_with_tag = []
			for genre in movie_matrix[lines[i][0]]:
				value_with_tag.append(genre)
			value_with_tag.append(tags_genres[tag.lower()])
			movie_matrix[int(lines[i][0])] = value_with_tag

	#Normalization
	for movie in movie_matrix:
		movie_normalized_values[movie] = 1/math.sqrt(len(movie_matrix[movie]))

	#Defining average rating for films
	file = open("./Dataset/ratings.csv","r")
	with open('./Dataset/ratings.csv') as csv_file:
		file = csv.reader(csv_file)
		lines = list(file)
	for i in range(1,len(lines)):
		film = int(lines[i][1])
		sum = 0
		counter = 0
		if(film not in avg_film_ratings):
			for j in range(1,len(lines)):
				if(float(lines[j][1])==film):
					counter+=1
					sum+=float(lines[j][2])
			avg_rating = float(sum)/counter
			avg_film_ratings[film] = avg_rating

	#Selecting films for user1
	film_values = []
	for value in movie_matrix[film_id]:
		film_values.append(value)
	for movie in movie_matrix:
		if(movie!=film_id):
			dot_product = 0
			for value in movie_matrix[movie]:
				if(value in film_values):
					dot_product+=movie_normalized_values[film_id]*movie_normalized_values[movie]
			if(dot_product>max_dot_product and avg_film_ratings[movie]>=4):
				max_dot_product = dot_product
				max_similar_film_id = movie
				print(movie_names[max_similar_film_id])

process_data()
