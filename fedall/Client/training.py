import numpy as np


def start_training(x_train, y_train, trainval, n0, model):
    # pylint: disable=C0103,R0801
    """TODO

    Args:
        x_train (_type_): _description_
        y_train (_type_): _description_
        trainval (_type_): _description_
        n0 (_type_): _description_
        model (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Non linear sigmoid activation function
    def sigmoid(z):
        sig = 1 / (1 + np.exp(-z))
        return sig

    # Hyper paramters
    learning_rate = 0.1
    iterations = 50

    nx = np.array([n0, 5, 5, 1])

    # initial model
    W1 = model[0]
    W2 = model[1]
    W3 = model[2]

    b1 = model[3]
    b2 = model[4]
    b3 = model[5]

    # Initializing variables
    Z1 = np.zeros([nx[1], trainval])
    A1 = np.zeros([nx[1], trainval])

    Z2 = np.zeros([nx[2], trainval])
    A2 = np.zeros([nx[2], trainval])

    Z3 = np.zeros([nx[3], trainval])
    A3 = np.zeros([nx[3], trainval])

    # Training
    J = np.zeros((iterations, 1))
    for i in range(iterations):
        # Forward Propagation
        Z1 = np.dot(W1, x_train) + b1
        A1 = sigmoid(Z1)

        Z2 = np.dot(W2, A1) + b2
        A2 = sigmoid(Z2)

        Z3 = np.dot(W3, A2) + b3
        A3 = sigmoid(Z3)

        # Loss function
        J[i] = (-1 / trainval) * np.sum(
            y_train * np.log(A3) + (1 - y_train) * np.log(1 - A3)
        )

        # Backward Propagation
        dZ3 = A3 - y_train
        dW3 = (1 / trainval) * np.dot(dZ3, A2.T)
        db3 = (1 / trainval) * np.sum(dZ3, axis=1, keepdims=True)

        dA2 = A2 * (1 - A2)
        dZ2 = np.dot(W3.T, dZ3) * dA2
        dW2 = (1 / trainval) * np.dot(dZ2, A1.T)
        db2 = (1 / trainval) * np.sum(dZ2, axis=1, keepdims=True)

        dA1 = A1 * (1 - A1)
        dZ1 = np.dot(W2.T, dZ2) * dA1
        dW1 = (1 / trainval) * np.dot(dZ1, x_train.T)
        db1 = (1 / trainval) * np.sum(dZ1, axis=1, keepdims=True)

        # Model updates
        W1 = W1 - learning_rate * dW1
        b1 = b1 - learning_rate * db1

        W2 = W2 - learning_rate * dW2
        b2 = b2 - learning_rate * db2

        W3 = W3 - learning_rate * dW3
        b3 = b3 - learning_rate * db3

    # Forward Propagation
    Z1 = np.dot(W1, x_train) + b1
    A1 = sigmoid(Z1)

    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)

    Z3 = np.dot(W3, A2) + b3
    A3 = sigmoid(Z3)

    # Loss function
    Loss = (-1 / trainval) * np.sum(
        y_train * np.log(A3) + (1 - y_train) * np.log(1 - A3)
    )

    pred_test = A3 > 0.5
    Acc = 1 - np.sum(abs(pred_test - y_train)) / trainval

    print("Train Loss: " + str(Loss))
    print("Train Acc: " + str(Acc))

    new_model = []

    new_model.append(W1)
    new_model.append(W2)
    new_model.append(W3)
    new_model.append(b1)
    new_model.append(b2)
    new_model.append(b3)

    return new_model
