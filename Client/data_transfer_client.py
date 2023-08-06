import pickle

def receive_model_from_server(socket):
    try:
        # Receiving the average model from the server 
        # in bytes form
        model_bytes = socket.recv(1024)

        # The loads() function in the pickle module is used to deserialize 
        # a byte string (model_bytes) back into a Python object, model
        model = pickle.loads(model_bytes)
        return model

    except pickle.PickleError as e:
        print("Error occurred while receiving the model:", e)
        # Close the socket to avoid any further communication
        socket.close()
        return None

    except Exception as e:
        print("An unexpected error occurred while receiving the model:", e)
        # Close the socket to avoid any further communication
        socket.close()
        return None

def send_model_to_server(socket, model):
    try:
        # The dumps() function in the pickle module is used to serialize
        # model into a byte string representation, required for the socket
        # to send to the server
        data_str_1 = pickle.dumps(model)

        # Send the local model represented as bytes to the server
        socket.sendall(data_str_1)

    except pickle.PickleError as e:
        print("Error occurred while sending the model:", e)
        # Close the socket to avoid any further communication
        socket.close()

    except Exception as e:
        print("An unexpected error occurred while sending the model:", e)
        # Close the socket to avoid any further communication
        socket.close()