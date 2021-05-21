# coding: utf-8

import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
import random
from PIL import Image
from scipy import ndimage

def load_data(train_set_percentage):
    """
    Arguments:
    train_set_percentage -- python float indicating the percentage of the data to be used as training set
    
    Returns:
    train_set_x -- numpy array which represent the training set (digit images)
    train_set_y -- numpy array which represent the label of the training set
    test_set_x -- numpy array which represent the testing set (digit images)
    test_set_y -- numpy array which represent the label of the testing set
    """
    dataset = h5py.File('dataset.h5', "r")
    
    total_num = np.shape(np.array(dataset["digit_images"][:]))[1]
    train_num = int(total_num * train_set_percentage)
    test_num = total_num - train_num
    
    digits = dataset["digit_images"][:]
    labels = dataset["digit_labels"][:]
    
    train_set_x = np.zeros((np.shape(digits)[0], train_num))
    train_set_y = np.zeros((1, train_num))
    
    test_set_x = np.zeros((np.shape(digits)[0], test_num))
    test_set_y = np.zeros((1, test_num))
    
    training_samples = []
    random.seed(0)
    
    for i in range(train_num):
        found = False
        while not found:
            sample_index = random.randint(0, total_num - 1)
            if sample_index not in training_samples:
                training_samples.append(sample_index)
                found = True
                train_set_x[:, i] = digits[:, sample_index]
                train_set_y[:, i] = labels[:, sample_index]
    
    test_index = 0
    for i in range(total_num):
        if i not in training_samples:
            test_set_x[:, test_index] = digits[:, i]
            test_set_y[:, test_index] = labels[:, i]
            test_index += 1
    
    dataset.close()
    
    return train_set_x, train_set_y, test_set_x, test_set_y

def reshape_Y(Y):
    """
    Arguments:
    Y -- numpy array which represents the labels,
         example, [0, 1, 2, 3, ...]
    
    Returns:
    Y_output -- numpy array which represent the labels in a different way (corresponding to the output layer)
         example corresponding to above:
         [[1, 0, 0, 0, ...],
          [0, 1, 0, 0, ...],
          [0, 0, 1, 0, ...],
          [0, 0, 0, 0, ...],
          [0, 0, 0, 1, ...],
          [0, 0, 0, 0, ...],
          [0, 0, 0, 0, ...],
          [0, 0, 0, 0, ...],
          [0, 0, 0, 0, ...],
          [0, 0, 0, 0, ...],
    """    
    num_samples = int(np.shape(Y)[1])
    Y_output = np.zeros((10, num_samples))
    
    for i in range(np.shape(Y)[1]):
        Y_output[int(np.squeeze(Y[:, i])), i] = 1

    return Y_output

def display_digit_image(image_set, label_set, index, figure_index):
    """
    Arguments:
    image_set -- numpy array which represents the image
    label_set -- numpy array which represents the label
    index -- the index of the image to be shown
    figure_index -- the index of the figure to show upon (every time when calling plt.figure function, a new figure_index needs to be assigned to get a new figure rather than draw on the original figure)
    """   
    plt.figure(figure_index)
    image = image_set[:, index].reshape(20, 20).T
    plt.imshow(image)
    plt.title("digit is " + str(int(label_set[0, index])))
    plt.xlim(0, 19)
    plt.ylim(19, 0)
    plt.xticks(np.arange(0, 20, 2))
    plt.yticks(np.arange(0, 20, 2))

def initialize_parameters(layer_dims):
    """
    Arguments:
    layer_dims -- python array (list) containing the dimensions of each layer in our network
    
    Returns:
    parameters -- python dictionary containing your parameters "W1", "b1", ..., "WL", "bL":
                    Wl -- weight matrix of shape (layer_dims[l], layer_dims[l-1])
                    bl -- bias vector of shape (layer_dims[l], 1)
    """
    
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)            # number of layers in the network

    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) * 0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
        
        assert(parameters['W' + str(l)].shape == (layer_dims[l], layer_dims[l-1]))
        assert(parameters['b' + str(l)].shape == (layer_dims[l], 1))

    return parameters

def sigmoid(Z):
    """
    Implements the sigmoid activation in numpy
    
    Arguments:
    Z -- numpy array of any shape
    
    Returns:
    A -- output of sigmoid(z), same shape as Z
    """
    return 1 / (1 + np.exp(-Z))

def sigmoid_gradient(A):
    """
    Implements the inverse of the sigmoid
    
    Arguments:
    A -- numpy array
    
    Returns:
    Z -- output of inverse of sigmoid(A), same shape as Z
    """    
    return sigmoid(A) * (1 - sigmoid(A))

def linear_activation_forward(A_prev, W, b):
    """
    Implement the forward propagation for one layer

    Arguments:
    A_prev -- activations from previous layer (or input data): (size of previous layer, number of examples)
    W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)
    b -- bias vector, numpy array of shape (size of the current layer, 1)

    Returns:
    Z -- the result of linear calculation
    A -- the output of the activation function, also called the post-activation value 
    """
    # Inputs: "A_prev, W, b". Outputs: "A, activation_cache".
    Z = np.matmul(W, A_prev) + b
    A = sigmoid(Z)
    
    assert(Z.shape == (W.shape[0], A.shape[1]))
    assert (A.shape == (W.shape[0], A_prev.shape[1]))

    return Z, A

def feedforward(X, parameters):
    """
    Implement forward propagation. The activation functions are all sigmoid functions.
    
    Arguments:
    X -- data, numpy array of shape (input size, number of examples)
    parameters -- output of initialize_parameters(layer_dims)
    
    Returns:
    AL -- last post-activation value
    caches -- a python dictionary containing "a1", "z2", "a2", "z3", ...;
             stored for computing the backward pass efficiently
    """

    caches = {}
    caches["a1"] = X
    A = X
    L = len(parameters) // 2                  # number of layers in the neural network
    
    for l in range(1, L + 1):
        A_prev = A 
        Z, A = linear_activation_forward(A_prev, parameters['W' + str(l)], parameters['b' + str(l)])
        caches["z" + str(l + 1)] = Z
        caches["a" + str(l + 1)] = A
    
    assert(A.shape == (10, X.shape[1]))
            
    return A, caches

def compute_cost(AL, Y):
    """
    Implement the cost function.

    Arguments:
    AL -- probability vector corresponding to your label predictions, shape (10, number of examples)
    Y -- true "label" vector after reshape by reshape_Y function, shape (10, number of examples)

    Returns:
    cost -- cross-entropy cost
    """
    
    m = Y.shape[1]

    # Compute loss from aL and y.
    cost = -np.sum(Y * np.log(AL) + (1 - Y) * np.log(1 - AL)) / m

    cost = np.squeeze(cost)     # To make sure your cost's shape is what we expect (e.g. this turns [[17]] into 17).
    assert(cost.shape == ())
    
    return cost

def display_cost(costs, learning_rate, figure_index):
    """
    display the cost in a figure
    
    Arguments:
    costs -- a list of floats with the costs of each iteration
    learning_rate -- learning rate to be displayed on the figure
    figure_index -- figure_index -- the index of the figure to show upon (every time when calling plt.figure function, a new figure_index needs to be assigned to get a new figure rather than draw on the original figure)
    """    
    plt.figure(figure_index)
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title("Learning rate = " + str(learning_rate))
    plt.show()    
    plt.savefig('plot.png')

def predict(parameters, X):
    """
    Using the learned parameters, predicts a class for each example in X
    
    Arguments:
    parameters -- python dictionary containing your parameters 
    X -- input data of size (n_x, m)
    
    Returns
    predictions -- vector of predictions of our model (0, 1, 2, 3 ...)
    """
    A2, cache = feedforward(X, parameters)
    predictions = np.argmax(A2, axis = 0)
    np.reshape(predictions, (1, np.shape(predictions)[0]))
    
    return predictions

def compute_accuracy(predictions, results):
    """
    Arguments:
    predictions -- output of predict
    results -- true labels
    
    Returns
    accuracy -- how accurate this model is to predict the digits
    """    
    comparison = predictions == results
    return np.sum(comparison) / np.shape(results)[1]

def backpropogation(AL, Y, parameters, caches, layers_dims):
    """
    Implement the backward propagation
    
    Arguments:
    AL -- probability vector, output of the forward propagation
    Y -- true "label" vector after reshaping by reshape_Y
    caches -- output of feedforward function
    
    Returns:
    grads -- A dictionary with the gradients
             grads["dA" + str(l)] = ... 
             grads["dW" + str(l)] = ...
             grads["db" + str(l)] = ... 
    """
    grads = {}
    L = len(layers_dims)
    m = AL.shape[1]

    # Initializing the backpropagation, by calculating dAL and save it to grads with the key "dA*" where * is the index of the layer
    # pleaes do not hard code to 3 here, as we will later play with neural networks with other configurations (e.g., more layers)
    ### START CODE HERE ###
    grads["dA" + str(L)] = AL - Y
    ### END CODE HERE ###
    
    for l in reversed(range(1, L)):
        # Inputs: "grads["dA" + str(l + 2)], caches". Outputs: "grads["dA" + str(l + 1)] , grads["dW" + str(l + 1)] , grads["db" + str(l + 1)]
        ### START CODE HERE ###
        if l > 1: 
            grads["dA" + str(l)] = np.multiply(np.matmul(parameters["W" + str(l)].T, grads["dA" + str(l + 1)]), sigmoid_gradient(caches["z" + str(l)]))
        grads["dW" + str(l)] = np.matmul(grads["dA" + str(l + 1)], caches["a" + str(l)].T) / m
        grads["db" + str(l)] = np.matmul(grads["dA" + str(l + 1)], np.ones((1, caches["a" + str(l)].shape[1])).T) / m
        ### END CODE HERE ###

    return grads

def update_parameters(parameters, grads, learning_rate):
    """
    Update parameters using gradient descent
    
    Arguments:
    parameters -- python dictionary containing your parameters 
    grads -- python dictionary containing your gradients, output of backpropagation
    
    Returns:
    parameters -- python dictionary containing your updated parameters 
                  parameters["W" + str(l)] = ... 
                  parameters["b" + str(l)] = ...
                  
    """
    
    L = len(parameters) // 2 # number of layers in the neural network

    # Update rule for each parameter. Use a for loop.
    ### START CODE HERE ###
    for l in range(1, L+1):
        parameters["W" + str(l)] -= learning_rate * grads["dW" + str(l)]
        parameters["b" + str(l)] -= learning_rate * grads["db" + str(l)]
    ### END CODE HERE ###
    
    return parameters

def deep_NN(X, Y, layers_dims, learning_rate, num_iterations, print_cost=False):
    """
    Implements a L-layer neural network: [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID.
    
    Arguments:
    X -- data, numpy array of shape (number of examples, num_px * num_px * 3)
    Y -- true "label" vector (containing 0 if cat, 1 if non-cat), of shape (1, number of examples)
    layers_dims -- list containing the input size and each layer size, of length (number of layers + 1).
    learning_rate -- learning rate of the gradient descent update rule
    num_iterations -- number of iterations of the optimization loop
    print_cost -- if True, it prints all the cost
    
    Returns:
    parameters -- parameters learnt by the model. They can then be used to predict.
    """

    np.random.seed(1)
    costs = []                         # keep track of cost
    
    # Parameters initialization.
    parameters = initialize_parameters(layers_dims)
    
    # Loop (gradient descent)
    for i in range(0, num_iterations):

        # Forward propagation:
        ### START CODE HERE ###
        AL, caches = feedforward(X, parameters)
        ### END CODE HERE ###
        
        # Compute cost.
        ### START CODE HERE ###
        cost = compute_cost(AL, Y)
        ### END CODE HERE ###
    
        # Backward propagation.
        ### START CODE HERE ###
        grads = backpropogation(AL, Y, parameters, caches, layers_dims)
        ### END CODE HERE ###
 
        # Update parameters.
        ### START CODE HERE ###
        parameters = update_parameters(parameters, grads, learning_rate)
        ### END CODE HERE ###
        
        if print_cost:
            print ("Cost after iteration %i: %f" %(i, cost))
        
        costs.append(cost)

    # # Q2    
    # print(parameters["W1"].shape)
    # print(parameters["b1"].shape)
    # print(parameters["W2"].shape)
    # print(parameters["b2"].shape)

    # # Q3
    # print(X.shape)
    # print(Y.shape) 
    # print(caches["a1"].shape)
    # print(caches["z2"].shape)
    # print(caches["a2"].shape)
    # print(caches["z3"].shape)
    # print(caches["a3"].shape)
    # # train_y shape -> train_y.shape
    return parameters, costs
    
if __name__ == "__main__":
    plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'
    np.random.seed(1)
    
    # the following are parameters to play with
    training_percentage = 1
    digit_sample_index = 0
    learning_rate = 0.5
    layers_dims = [400, 25, 10]
    num_iterations = 2000
    
    # # section 1: one example of how to run the model with the training data
    # train_x, train_y, test_x, test_y = load_data(training_percentage)
    # display_digit_image(train_x, train_y, digit_sample_index, figure_index=1) # you can change the digit_sample_index to display different images
    # parameters, costs = deep_NN(train_x, reshape_Y(train_y), layers_dims, learning_rate, num_iterations, print_cost=True)
    # display_cost(costs, learning_rate, figure_index=2)
    # train_set_predictions = predict(parameters, train_x)
    # train_set_accuracy = compute_accuracy(train_set_predictions, train_y)
    # print("the accuracy on the training set is : ")
    # print(train_set_accuracy)
    
    # section 2: separate dataset into training set and test set
    # training_percentage = 0.8
    # train_x, train_y, test_x, test_y = load_data(training_percentage)
    # display_digit_image(train_x, train_y, digit_sample_index, figure_index=1) # you can change the digit_sample_index to display different images
    # parameters, costs = deep_NN(train_x, reshape_Y(train_y), layers_dims, learning_rate, num_iterations, print_cost=True)
    # display_cost(costs, learning_rate, figure_index=2)
    
    # train_set_predictions = predict(parameters, train_x)
    # train_set_accuracy = compute_accuracy(train_set_predictions, train_y)
    # print("the accuracy on the training set is : ")
    # print(train_set_accuracy)
    
    # test_set_predictions = predict(parameters, test_x)
    # test_set_accuracy = compute_accuracy(test_set_predictions, test_y)
    # print("the accuracy on the testing set is : ")
    # print(test_set_accuracy)
    
    # section 3: modifying the learning_rate
    # training_percentage = 1
    # learning_rate = 10 
    # train_x, train_y, test_x, test_y = load_data(training_percentage)
    # display_digit_image(train_x, train_y, digit_sample_index, figure_index=1) # you can change the digit_sample_index to display different images
    # parameters, costs = deep_NN(train_x, reshape_Y(train_y), layers_dims, learning_rate, num_iterations, print_cost=True)
    # display_cost(costs, learning_rate, figure_index=2)
    # train_set_predictions = predict(parameters, train_x)
    # train_set_accuracy = compute_accuracy(train_set_predictions, train_y)
    # print("the accuracy on the training set is : ")
    # print(train_set_accuracy)    
    
    # section 4: overfitting
    # training_percentage = 0.8
    # learning_rate = 2
    # layers_dims = [400, 50, 25, 10]
    # num_iterations = 30000
    # train_x, train_y, test_x, test_y = load_data(training_percentage)
    # display_digit_image(train_x, train_y, digit_sample_index, figure_index=1) # you can change the digit_sample_index to display different images
    # parameters, costs = deep_NN(train_x, reshape_Y(train_y), layers_dims, learning_rate, num_iterations, print_cost=True)
    # display_cost(costs, learning_rate, figure_index=2)

    # train_set_predictions = predict(parameters, train_x)
    # train_set_accuracy = compute_accuracy(train_set_predictions, train_y)
    # print("the accuracy on the training set is : ")
    # print(train_set_accuracy)
    
    # test_set_predictions = predict(parameters, test_x)
    # test_set_accuracy = compute_accuracy(test_set_predictions, test_y)
    # print("the accuracy on the testing set is : ")
    # print(test_set_accuracy)  
    
    # section 5: your experiment
    training_percentage = 0.8
    learning_rate = 10
    layers_dims = [400, 25, 10]
    num_iterations = 2000
    
    train_x, train_y, test_x, test_y = load_data(training_percentage)
    display_digit_image(train_x, train_y, digit_sample_index, figure_index=1) # you can change the digit_sample_index to display different images
    parameters, costs = deep_NN(train_x, reshape_Y(train_y), layers_dims, learning_rate, num_iterations, print_cost=True)
    display_cost(costs, learning_rate, figure_index=2)

    train_set_predictions = predict(parameters, train_x)
    train_set_accuracy = compute_accuracy(train_set_predictions, train_y)
    print("the accuracy on the training set is : ")
    print(train_set_accuracy)
    
    test_set_predictions = predict(parameters, test_x)
    test_set_accuracy = compute_accuracy(test_set_predictions, test_y)
    print("the accuracy on the testing set is : ")
    print(test_set_accuracy)      