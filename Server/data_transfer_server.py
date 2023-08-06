import pickle

def send_model_to_clients(avg_model, sockets):
    try:
        # The dumps() function in the pickle module is used to serialize
        # avg_model into a byte string representation, required for the sockets
        # to send to the clients
        model_str = pickle.dumps(avg_model)

        # Send the avg_model represented as bytes to all the clients
        for sock in sockets:
            sock.sendall(model_str)
    
    except pickle.PickleError as pe:
        print(f"Error during model serialization: {pe}")
    except OSError as oe:
        print(f"Error during socket communication: {oe}")
    except Exception as e:
        print(f"Error during sending model to clients: {e}")

def receive_models_from_clients(sockets):
    all_models = []
    try:
        for i, sock in enumerate(sockets):
            # print("Client No.: " + str(i + 1))

            # Receiving the local model from the client 
            # in bytes form
            model_bytes = sock.recv(1024)

            # The loads() function in the pickle module is used to deserialize 
            # a byte string (model_bytes) back into a Python object, model_data
            model_data = pickle.loads(model_bytes)

            # print("Model Received: ", model_data)

            # Putting all the received models in one big list
            all_models.append(model_data)

        return all_models
    
    except pickle.PickleError as pe:
        print(f"Error during model deserialization: {pe}")
        return []
    except OSError as oe:
        print(f"Error during socket communication: {oe}")
        return []
    except Exception as e:
        print(f"Error during receiving models from clients: {e}")
        return []