import socket


def create_socket(server_address):
    """TODO

    Args:
        server_address (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        # Creating TCP Socket
        # socket.AF_INET: This constant represents the address family for IPv4
        # socket.SOCK_STREAM: This constant represents the socket type for a TCP
        # (Transmission Control Protocol) socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Splitting the IP address and the Port number
        server_ip, server_port = server_address.split(":")

        # Connecting to the server
        client_socket.connect((server_ip, int(server_port)))
        print("Connection established with the server")

        # Wrap the socket with SSL/TLS
        # client_socket = ssl.wrap_socket(client_socket)

        return client_socket

    except socket.error as e:
        print("Socket error occurred while connecting:", e)
        return None

    except ValueError as e:
        print("Invalid server address format:", e)
        return None

    # TODO: more specific exception handling
    except Exception as e:
        print("An unexpected error occurred while creating the socket:", e)
        return None


def close_socket(skt):
    """TODO

    Args:
        skt (_type_): _description_
    """
    try:
        skt.close()

    # TODO: more specific exception handling
    except Exception as e:
        print("An error occurred while closing the socket:", e)
