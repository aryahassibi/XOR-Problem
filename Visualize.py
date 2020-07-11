from neuralNetwork import *
from random import randint, random
import pygame
import time

time.sleep(10)

pygame.init()

# width and height of pygame window [pygame window should b a square (width = height)]
width, height = 600, 600

size = [width, height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("XOR")

# creating a neural network with 2 inputs and 10 nodes in hidden layer and 1 output
nn = Neuralnetwork(2, 10, 1)

# inputs and target for training the neural network
inputs = [[0, 0], [1, 0], [1, 1], [0, 1]]
targets = [[0], [1], [0], [1]]

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Training neural network to learn to solve cor problem
    for _ in range(1000):
        index = randint(0, 3)
        nn.train(inputs[index], targets[index])

    # we divide pygame screen into square cells with resolution / height and width of RES
    res = 15

    # number of cells  in each row and column
    cols = width // res
    rows = height // res

    for i in range(cols):
        for j in range(rows):
            first_input = j / cols
            second_input = i / rows
            neural_network_inputs = [first_input, second_input]

            prediction = nn.predict(neural_network_inputs)[0]

            c = int(prediction * 255)
            color_of_each_cell = (c, c, c)
            pygame.draw.rect(screen, color_of_each_cell, (i * res, j * res, res, res))

            # Black cell : 0 (false)
            # White cell : 1 (true)

    # update screen
    pygame.display.flip()

pygame.quit()
