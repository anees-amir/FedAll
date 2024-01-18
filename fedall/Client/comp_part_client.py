from fedall.client import model_train_client as md
from fedall.client import data_transfer_client as dt


def comp_model(socket, data, num_rounds):
    """TODO

    Args:
        socket (_type_): _description_
        data (_type_): _description_
        num_rounds (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        for r in range(num_rounds):
            # Receive the average model from the server
            model = dt.receive_model_from_server(socket)

            print("Round: " + str(r + 1))

            # Start the training on the local data
            model = md.training(data, model)

            # Send the local model to the server
            dt.send_model_to_server(socket, model)

        return model

    # TODO: Add exception in appropraite modules. currently, these don't exist in their respective
    # modules...

    # except dt.dataTransferError as e:
    #     print("data transfer error occurred:", e)
    #     # Close the socket to avoid any further communication
    #     socket.close()
    #     return None

    # except md.TrainingError as e:
    #     print("Training error occurred:", e)
    #     # Close the socket to avoid any further communication
    #     socket.close()
    #     return None

    # TODO: more specific exception handling
    except Exception as e:
        print("An unexpected error occurred:", e)
        # Close the socket to avoid any further communication
        socket.close()
        return None
