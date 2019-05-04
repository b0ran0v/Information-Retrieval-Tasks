import sys
import os
import re
import csv
import numpy as np

dictionary = {}
dictionary['sunny']=0
dictionary['ovecast']=1
dictionary['rainy']=2
dictionary['hot']=0
dictionary['mild']=1
dictionary['cold']=2
dictionary['high']=0
dictionary['normal']=1
dictionary['FALSE']=0
dictionary['TRUE']=1
dictionary['no']=0
dictionary['yes']=1

class PartyNN(object):
    
    def __init__(self, learning_rate=0.1):
        self.weights_0_1 = np.random.normal(0.0, 2 ** -0.5, (2, 4))
        self.weights_1_2 = np.random.normal(0.0, 1, (1, 2))
        self.sigmoid_mapper = np.vectorize(self.sigmoid)
        self.learning_rate = np.array([learning_rate])
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def predict(self, inputs):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)
        
        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        return outputs_2
    
    def train(self, inputs, expected_predict):     
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)
        
        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        actual_predict = outputs_2[0]
        
        error_layer_2 = np.array([actual_predict - expected_predict])
        gradient_layer_2 = actual_predict * (1 - actual_predict)
        weights_delta_layer_2 = error_layer_2 * gradient_layer_2  
        self.weights_1_2 -= (np.dot(weights_delta_layer_2, outputs_1.reshape(1, len(outputs_1)))) * self.learning_rate
        
        error_layer_1 = weights_delta_layer_2 * self.weights_1_2
        gradient_layer_1 = outputs_1 * (1 - outputs_1)
        weights_delta_layer_1 = error_layer_1 * gradient_layer_1
        self.weights_0_1 -= np.dot(inputs.reshape(len(inputs), 1), weights_delta_layer_1).T  * self.learning_rate


def MSE(y, Y):
    return np.mean((y-Y)**2)

file = open("tennis.csv","r")
with open('tennis.csv') as csv_file:
	file = csv.reader(csv_file)
	lines = list(file)

print(lines)
train = []

for i in range(1,len(lines)):
    print(lines[i])
    factor[0] = dictionary[factor[0]]
    factor[1] = dictionary[factor[1]]
    factor[2] = dictionary[factor[2]]
    factor[3] = dictionary[factor[3]]
    result = dictionary[result]
	train.append(inp)

print(train)

#epochs = 5000
#learning_rate = 0.05
epochs = 6000
learning_rate = 0.08

network = PartyNN(learning_rate=learning_rate)

for e in range(epochs):
    inputs_ = []
    correct_predictions = []
    for input_stat, correct_predict in train:
        network.train(np.array(input_stat), correct_predict)
        inputs_.append(np.array(input_stat))
        correct_predictions.append(np.array(correct_predict))
    
    train_loss = MSE(network.predict(np.array(inputs_).T), np.array(correct_predictions))
    sys.stdout.write("\rProgress: {}, Training loss: {}".format(str(100 * e/float(epochs))[:4], str(train_loss)[:5]))