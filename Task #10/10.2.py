import os
import re

out_arrow_number = {}
last_iteration_values = {}
current_iteration_values = {}

def get_delta(input, node_id):
        sum = 0
        for row in range(0,len(input)):
                if(input[row][node_id]==1):
                        sum+=last_iteration_values[row+1]/out_arrow_number[row+1]
        return sum


def get_value(alpha, page_number, delta):
        return ((1-alpha)/page_number)+alpha*delta

def process_input(input):
        global out_arrow_number
        global current_iteration_values
        global last_iteration_values
        #Defining initial values
        for i in range(0,len(input)):
                last_iteration_values[i+1]=1.0/len(input)

        #Defining number of outgoing arrows
        for row in range(0,len(input)):
                count = 0
                for column in range(0,len(input[row])):
                        if(input[row][column]==1):
                                count+=1
                out_arrow_number[row+1] = count

        #Making 2 iterations
        for i in range(0,4):
                for node_id in range(0,len(input)):
                        delta = get_delta(input, node_id)
                        new_value = get_value(0.85, len(input), delta)
                        current_iteration_values[node_id+1] = new_value
                last_iteration_values = current_iteration_values
                current_iteration_values = {} 

def rank_pages(page_names):
        place = 1
        for key, value in sorted(last_iteration_values.items(), key=lambda item: item[1], reverse=True):
                print(str(place)+' '+"%s: %s" % (page_names[key], value))
                place+=1

matrix = [[0,0,1,1,0],[1,0,1,0,0],[0,0,0,1,0],[1,1,1,0,1],[0,0,1,0,0]]
page_names = {1:'Amazon', 2:'Facebook', 3:'Twitter', 4:'Wikipedia', 5:'Myspace'}
process_input(matrix)
rank_pages(page_names)
