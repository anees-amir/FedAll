from fedall.Client import model_train_client as md
from fedall.Client import data_transfer_client as dt

def comp_model(socket, Data, NumofRounds):
    try:
        for r in range(NumofRounds):
            # Receive the average model from the server
            model = dt.receive_model_from_server(socket)

            print("Round: " + str(r + 1))

            # Start the training on the local data
            model = md.training(Data, model)

            # Send the local model to the server
            dt.send_model_to_server(socket, model)
        
        return model

    except dt.DataTransferError as e:
        print("Data transfer error occurred:", e)
        # Close the socket to avoid any further communication
        socket.close()
        return None

    except md.TrainingError as e:
        print("Training error occurred:", e)
        # Close the socket to avoid any further communication
        socket.close()
        return None

    except Exception as e:
        print("An unexpected error occurred:", e)
        # Close the socket to avoid any further communication
        socket.close()
        return None