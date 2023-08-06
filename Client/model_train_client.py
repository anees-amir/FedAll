import Client.training as tr

import Client.data_split as ds
def training(Data, model):
    trainval, n = Data.shape
    n0 = n - 1

    # Splitting the data into input and output features
    x_train, y_train = ds.data_x_y(Data)

    # Start the training
    model = tr.start_training(x_train, y_train, trainval, n0, model)

    return model