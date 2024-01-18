import numpy as np


def define_model():
    # pylint: disable=C0103
    """TODO

    Returns:
        _type_: _description_
    """

    # Number of neurons in each layer, including input and output
    nx = np.array([4, 5, 5, 1])

    # Weights and Bias parameters initialized randomly
    W1 = np.random.randn(nx[1], nx[0])
    b1 = np.random.randn(nx[1], 1)

    W2 = np.random.randn(nx[2], nx[1])
    b2 = np.random.randn(nx[2], 1)

    W3 = np.random.randn(nx[3], nx[2])
    b3 = np.random.randn(nx[3], 1)

    # Put the parameters in a Model list
    model = [W1, W2, W3, b1, b2, b3]

    return model
