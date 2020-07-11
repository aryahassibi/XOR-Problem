from matrix import *
from neuralNetwork import *
from random import randint

# creating a neural network with 2 inputs and 10 nodes in hidden layer and 1 output
nn = Neuralnetwork(2, 10, 1)

inputs = [[0, 0], [1, 0], [1, 1], [0, 1]]
targets = [[0], [1], [0], [1]]

# Training neural network to learn to solve XOR problem
for j in range(10000):
    i = randint(0, 3)
    nn.train(inputs[i], targets[i])

# Printing predictions of neural network after training
for i in range(4):
    o = nn.predict(inputs[i])
    print("XOR", inputs[i], " ≈ ", o[0])
