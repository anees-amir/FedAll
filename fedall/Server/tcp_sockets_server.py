import ssl


def create_sockets(num_clients, certfile=None, keyfile=None):
    # pylint: disable=C0415
    """TODO

    Args:
        num_clients (_type_): _description_
        certfile (_type_, optional): _description_. Defaults to None.
        keyfile (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    # import placed here, as it cannot be read from outside of the fujnction (not sure why...)
    import socket

    # Port Number
    port = 6005

    try:
        # Creating TCP Socket
        # socket.AF_INET: This constant represents the address family for IPv4
        # socket.SOCK_STREAM: This constant represents the socket type for a TCP
        # (Transmission Control Protocol) socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # The SO_REUSEADDR option allows reusing local addresses
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # The following will get the hostname (IP)
        # host = socket.getaddrinfo(socket.gethostname(), 1)[6][4][0]

        # The socket is bind with the specified hostname and the port
        server_socket.bind(("localhost", port))

        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        if certfile is not None:
            context.load_cert_chain(certfile=certfile, keyfile=keyfile)

        # The socket is listening to the incoming connections request
        # with the specified hostname and the port
        server_socket.listen(1)

        # Accepting connections from the clients
        # It will wait for the specified number of requests
        # defined by the number of the clients
        sockets_client = []
        for _ in range(num_clients):
            print("Waiting for incoming connections...")
            # The new connection is stored in a socket variable
            # The future communication will take place via this socket variable
            socket, client_address = server_socket.accept()

            print("Accepted connection from", client_address)

            # Putting all the sockets in one list
            sockets_client.append(socket)

        # Wrapping all the sockets around SSL Layer
        # If the certificate and key files are provided
        if (certfile is not None) and (keyfile is not None):
            sockets = []
            for sock in sockets_client:
                socket = context.wrap_socket(sock, server_side=True)
                sockets.append(socket)
            sockets_client = sockets

        return sockets_client

    except socket.error as e:
        print("Error occurred while creating sockets:", e)
        # Close the sockets if any were opened before the error
        for sock in sockets_client:
            sock.close()
        return None


def close_sockets(sockets):
    """TODO

    Args:
        sockets (_type_): _description_
    """
    try:
        for sock in sockets:
            sock.close()
    # TODO: more specific exception handling
    except Exception as e:
        print("Error occurred while closing sockets:", e)
