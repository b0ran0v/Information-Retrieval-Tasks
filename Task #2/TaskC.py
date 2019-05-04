import os
import re
import math
import decimal

file_1 = open('./count_1w.txt')
words1 = file_1.read().split('\n')
file_2 = open('./count_2w.txt')
words2 = file_2.read().split('\n')
sum1 = 0
sum2 = 0
line_num = 0;

result = 1

def per_count(word1, word2):
    numerator = 0
    denominator = 0
    for word in words1:
        wor = word.split('\t')[0]
        if(word1==wor):
            denominator = denominator + int(word.split('\t')[1])
            break 
    for word in words2:
        wor = word.split('\t')[0]
        if(word1+' '+word2==wor):
            numerator = numerator + int(word.split('\t')[1])
            break
    return (numerator+1)/(denominator+line_num)


sentence = input('Enter sentence:')

# Reading count_1
for word in words1:
    line_num +=1;
    wor = word.split('\t')[0]
    sum1 = sum1 + int(word.split('\t')[1])
    
# Reading count_2
for word in words2:
    wor = word.split('\t')[0]
    sum2 = sum2 + int(word.split('\t')[1])
    

words_splited = sentence.split(' ')    
for i in range(len(words_splited)-1):
    word1 = words_splited[i]
    word2 = words_splited[i+1]
    result = result * per_count(word1,word2)

print(line_num)
print(result)
    
