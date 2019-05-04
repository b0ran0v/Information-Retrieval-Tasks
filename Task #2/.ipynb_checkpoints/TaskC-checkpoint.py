import os
import re

file_1 = open('./count_1w.txt')
words1 = file_1.read().split('\n')
file_2 = open('./count_2w.txt')
words2 = file_2.read().split('\n')
list1 = []
list2 = []
sum1 = 0
sum2 = 0

result = 0

def per_count(word1, word2):
    numerator = 0
    denominator = 0
    for word in list1:
        wor = word.split('\t')[0]
        if(word1==wor):
            denominator = denominator + int(word.split('\t')[1])
            break 
    for word in list2:
        wor = word.split('\t')[0]
        if(word1+' '+word2==wor):
            numerator = numerator + int(word.split('\t')[1])
            break
    return (numerator+1)/(denominator+sum1)


sentence = str(raw_input("Enter sentence:")).split(' ')

# Reading count_1
for word in words1:
    wor = word.split('\t')[0]
    if wor in sentence:
        list1.append(word)
    sum1 = sum1 + int(word.split('\t')[1])
    
# Reading count_2
for word in words2:
    wor = word.split('\t')[0]
    if wor in sentence:
        list2.append(word)
    sum2 = sum2 + int(word.split('\t')[1])
    
for i in range(len(sentence)-1):
    word1 = sentence[i]
    word2 = sentence[i+1]
    result = result + math.log10(per_count(word1,word2))
    
print(result)