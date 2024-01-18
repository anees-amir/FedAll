## Simple example

The following is a simple example for using `FedAll`. It allows 2 clients to connect to a central server and train nueral networks using some test data.
This is a simulation where the clients and server are all being run from the same machine and localhost network.

### Run the Example

We assume that you have installed `FedAll` (instructions can be found [here]()).

1. Open one terminal, and the run the following:

```
python3 server_example.py
```

you should be able to see a confirmation print from the server that it is awaiting incoming connections. 

2. Open a second terminal, and the run the following:

```
python3 client_example_1.py
```

you should be able to see a confirmation print from the client that it has established a connection with the server.

3. Open another terminal, and the run the following:

```
python3 client_example_2.py
```

You should be able to see numerous prints of Training losses and accuracies for all terminals. When the federated
learning example is complete, all terminal executions should be complete. Congratulations, you have ran a `FedAll` simple example! 
