import pandas
import numpy as np

def loss_acc(avg_model, Data):

    # Assigning specific model parameters to the Weights matrices
    # and Bias vectors
    W1 = avg_model[0]
    W2 = avg_model[1]
    W3 = avg_model[2]

    b1 = avg_model[3]
    b2 = avg_model[4]
    b3 = avg_model[5]

    trainval, n = Data.shape
    n0 = n - 1

    x_test = Data[:, 0:n0].T
    y_test = Data[:, n0]

    # Non linear sigmoid activation function
    def sigmoid(z):
        sig = 1 / (1 + np.exp(-z))
        return sig

    # Computing forward propagation on testing data
    Z1 = np.dot(W1, x_test) + b1
    A1 = sigmoid(Z1)

    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)

    Z3 = np.dot(W3, A2) + b3
    A3 = sigmoid(Z3)

    # Computing loss on testing data
    Loss = (-1/trainval)*np.sum(y_test*np.log(A3) + (1-y_test)*np.log(1-A3))

    # Computing accuracy on testing data
    pred_train = A3 > 0.5
    Acc = 1 - np.sum(abs(pred_train - y_test))/trainval 

    return Loss, Acc