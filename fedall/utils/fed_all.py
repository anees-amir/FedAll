from fedall.client import comp_part_client as cp_client
from fedall.server import comp_part_server as cp_server
from fedall.server import ml_model as md
from fedall.client import tcp_sockets_client as tcp_client
from fedall.server import tcp_sockets_server as tcp_server


def initialize_model_server():
    """TODO

    Returns:
        _type_: _description_
    """
    try:
        # At this moment, the model values are hardcoded
        # In future, this function will be expanded to accept the model architecture from the user
        model = md.define_model()
        return model
    # TODO: more specific exception handling
    except Exception as e:
        print(f"Error initializing the model server: {e}")
        return None


def start_server(
    num_clients, num_rounds, model, test_data, certfile=None, keyfile=None
):
    """TODO

    Args:
        num_clients (_type_): _description_
        num_rounds (_type_): _description_
        model (_type_): _description_
        test_data (_type_): _description_
        certfile (_type_, optional): _description_. Defaults to None.
        keyfile (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    try:
        # Connections are established between the server and the clients
        # The number of connections is defined by the number of clients
        sockets = tcp_server.create_sockets(num_clients, certfile, keyfile)

        # Once the connections are established, the model is exchanged
        # and the average model is computed
        avg_model = cp_server.compute_avg(sockets, num_rounds, model, test_data)

        # Once the communication is done, the connections are closed
        tcp_server.close_sockets(sockets)

        return avg_model
    # TODO: more specific exception handling
    except Exception as e:
        print(f"Error during server execution: {e}")
        return None


def client_start(server_address, data, num_rounds):
    """TODO

    Args:
        server_address (_type_): _description_
        data (_type_): _description_
        num_rounds (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        # Connection is established between the server and the client
        socket = tcp_client.create_socket(server_address)

        # The client computes the local model on its local data
        avg_model = cp_client.comp_model(socket, data, num_rounds)

        # The client will close the connection once the communication is done
        tcp_client.close_socket(socket)

        return avg_model
    # TODO: more specific exception handling
    except Exception as e:
        print(f"Error during client execution: {e}")
        return None
