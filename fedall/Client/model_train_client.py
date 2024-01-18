from fedall.client import training as tr
from fedall.client import data_split as ds


def training(data, model):
    """TODO

    Args:
        data (_type_): _description_
        model (_type_): _description_

    Returns:
        _type_: _description_
    """
    trainval, n = data.shape
    n0 = n - 1

    # Splitting the data into input and output features
    x_train, y_train = ds.data_x_y(data)

    # Start the training
    model = tr.start_training(x_train, y_train, trainval, n0, model)

    return model
