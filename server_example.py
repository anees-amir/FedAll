import FedAll as fa
import pandas

# Load the self-signed certificate and private key
# In case where authenticationa and encrytpion are required

certfile = 'certificate/server_certificate.crt'
keyfile = 'certificate/server_private_key.key'

# The server can set the values for the following hyper parameters
NumofClients = 2
NumofRounds = 50

# The following function will initialize the model
# At this moment, the model values are hardcoded
# There are two hidden layers and each hidden layer has 5 neurons
# In future, this function will be expanded to accept the model architecture from the user
# Also, we will incorporate the NN models of PyTorch and Tensorflow

initial_model = fa.initialize_model_server()

# Load the data for testing purposes
# The data contains both the input features and the output feature
# The features are represented as columns
# The data points are represented as rows

test_data = pandas.read_csv('test_data.csv', header=None)
test_data = test_data.to_numpy()

# The following function accepts certificate and keyfile as last two parameters
# By default their values are set to None

avg_model = fa.start_server(NumofClients, NumofRounds, initial_model, test_data) 