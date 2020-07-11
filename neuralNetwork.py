from matrix import *
from math import exp


# -- Activation function ---

def sigmoid(x):
    return 1 / (1 + exp(-x))


def dsigmoid(x):
    # derivative of sigmoid function
    # return sigmoid(x) * (1 - sigmoid(x))
    # outputs hav already been passed through sigmoid function so we can just -> return x * (1 - x)

    return x * (1 - x)

# --------------------------

class Neuralnetwork:
    def __init__(self, number_of_input_nodes, number_of_hidden_nodes, number_of_output_nodes):
        self.number_of_input_nodes = number_of_input_nodes
        self.number_of_hidden_nodes = number_of_hidden_nodes
        self.number_of_output_nodes = number_of_output_nodes

        # input layer to hidden layer weights
        self.weights_ih = Matrix(self.number_of_hidden_nodes, self.number_of_input_nodes)

        # hidden layer to output layer weights
        self.weights_ho = Matrix(self.number_of_output_nodes, self.number_of_hidden_nodes)

        # initializing weights
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.number_of_hidden_nodes, 1)
        self.bias_o = Matrix(self.number_of_output_nodes, 1)

        self.bias_h.randomize()
        self.bias_o.randomize()

        # learning rate is a hyper-parameter so you can set it to any number you want
        # you have find the learning rate that works for you
        self.learning_rate = 0.05

    def predict(self, input_array):
        # Feedforward

        # Turning input array in to a matrix
        inputs = Matrix.from_array(input_array)

        # Calculating the value of each hidden layer node
        hidden = Matrix.product(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map_function(sigmoid)
        # -----------------------------------------------

        # Calculating the value of each output layer node
        output = Matrix.product(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map_function(sigmoid)
        # -----------------------------------------------

        # Turn output to an array and return it
        return output.to_array()

    def train(self, input_array, target_array):

        # Feedforward

        # Turning input array in to a matrix
        inputs = Matrix.from_array(input_array)

        # Calculating the value of each hidden layer node
        hidden = Matrix.product(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map_function(sigmoid)

        # Calculating the value of each output layer node
        output = Matrix.product(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map_function(sigmoid)

        # Backpropagation

        # Turning target array in to a matrix
        targets = Matrix.from_array(target_array)

        # Calculate output errors [target - prediction(output)]
        output_errors = Matrix.subtract(targets, output)

        # Calculate output gradients
        output_gradients = Matrix.map_function_static(output, dsigmoid)
        output_gradients.multiply(output_errors)
        output_gradients.multiply(self.learning_rate)

        # calculate weights (from hidden to output layer) delta
        # weights delta is the amount of the change that we are going to apply to the weights
        hidden_T = Matrix.transpose(hidden)
        weight_ho_deltas = Matrix.product(output_gradients, hidden_T)

        # adding weight deltas and adjusting bias
        self.weights_ho.add(weight_ho_deltas)
        self.bias_o.add(output_gradients)

        # calculate hidden layer errors
        # Error of the Hidden layer is basically the dot product of output errors and transposed weights (form hidden layer to output layer)
        # we calculate the dot product because, effect of each hidden layer node on the error of each node in ->
        # the output layer is determined by amount of weight between two nodes (hopefully that makes sense)
        weights_ho_T = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.product(weights_ho_T, output_errors)

        # calculate hidden gradients
        hidden_gradients = Matrix.map_function_static(hidden, dsigmoid)
        hidden_gradients.multiply(hidden_errors)
        hidden_gradients.multiply(self.learning_rate)

        # calculate weights (from input to hidden layer) deltas
        # weights delta is the amount of the change that we are going to apply to the weights
        inputs_T = Matrix.transpose(inputs)
        weight_ih_deltas = Matrix.product(hidden_gradients, inputs_T)

        # adding weight deltas and adjusting bias
        self.weights_ih.add(weight_ih_deltas)
        self.bias_h.add(hidden_gradients)
