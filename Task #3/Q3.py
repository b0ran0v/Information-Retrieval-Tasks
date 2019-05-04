import os
import re

file1 = open('./count_1w.txt')
words1 = file1.read().split('\n')
file1 = open('./count_2w.txt')
words2 = file1.read().split('\n')
sum1 = 0
sum2 = 0
line_num = 0

def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res


def process():
    # Reading count_1
    global line_num, sum1, sum2
    for word in words1:
        line_num += 1
        wor = word.split('\t')[0]
        sum1 += int(word.split('\t')[1])
        
    # Reading count_2
    for word in words2:
        wor = word.split('\t')[0]
        sum2 += int(word.split('\t')[1])


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


def LMP(words_splited):
    result = 1
    for i in range(len(words_splited)-1):
        word1 = words_splited[i]
        word2 = words_splited[i+1]
        result = result * per_count(word1,word2)
    return result



process()
sentence = input('Enter word:')
changed_word = sentence
sentence = 'in '+ sentence+' life'
print(0.05*0.005**LD('dairy',changed_word)*LMP(sentence))

    
