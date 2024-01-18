import numpy as np


def data_x_y(data):
    """TODO

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    m, n = data.shape
    n0 = n - 1

    # Centered around the mean
    data[:, 0 : n - 1] = data[:, 0 : n - 1] - np.mean(data[:, 0 : n - 1], 0)

    # For unshuffled data, comment the following two lines
    randseq = np.random.permutation(m)
    data = data[randseq[0:m], 0:n]

    # Input features
    x_train = data[:, 0:n0].T

    # Output feature
    y_train = data[:, n0]

    return x_train, y_train
