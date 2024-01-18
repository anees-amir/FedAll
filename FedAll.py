import Server.comp_part_server as cp_server
import Server.tcp_sockets_server as tcp_server
import Server.ml_model as md

import Client.tcp_sockets_client as tcp_client
import Client.comp_part_client as cp_client

def initialize_model_server():
    try:
        # At this moment, the model values are hardcoded
        # In future, this function will be expanded to accept the model architecture from the user
        model = md.define_model()
        return model
    except Exception as e:
        print(f"Error initializing the model server: {e}")
        return None

def start_server(NumofClients, NumofRounds, model, test_data, certfile=None, keyfile=None):
    try:
        # Connections are established between the server and the clients
        # The number of connections is defined by the number of clients
        sockets = tcp_server.create_sockets(NumofClients, certfile, keyfile)

        # Once the connections are established, the model is exchanged
        # and the average model is computed
        avg_model = cp_server.compute_avg(sockets, NumofRounds, model, test_data)

        # Once the communication is done, the connections are closed
        tcp_server.close_sockets(sockets)

        return avg_model
    except Exception as e:
        print(f"Error during server execution: {e}")
        return None

def client_start(server_address, Data, NumofRounds):
    try:
        # Connection is established between the server and the client
        socket = tcp_client.create_socket(server_address)

        # The client computes the local model on its local data
        avg_model = cp_client.comp_model(socket, Data, NumofRounds)

        # The client will close the connection once the communication is done
        tcp_client.close_socket(socket)

        return avg_model
    except Exception as e:
        print(f"Error during client execution: {e}")
        return None