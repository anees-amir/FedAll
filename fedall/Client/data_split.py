import numpy as np

def data_x_y(Data):
    m, n = Data.shape
    n0 = n - 1

    # Centered around the mean
    Data[:, 0:n-1] = Data[:, 0:n-1] - np.mean(Data[:, 0:n-1], 0)

    # For unshuffled data, comment the following two lines
    randseq = np.random.permutation(m)
    Data = Data[randseq[0:m], 0:n]

    # Input features
    x_train = Data[:, 0:n0].T

    # Output feature
    y_train = Data[:, n0]

    return x_train, y_train