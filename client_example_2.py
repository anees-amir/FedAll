import FedAll as fa
import pandas

# Specify the server address in terms of IP and Port number
server_address = "localhost:6005"

# Load the data for training purposes
# The data contains both the input features and the output feature
# The features are represented as columns
# The data points are represented as rows
Data = pandas.read_csv('train_data_2.csv', header=None)
Data = Data.to_numpy()

NumofRounds = 50
# The following will start the training and will return the final model
final_model = fa.client_start(server_address, Data, NumofRounds)