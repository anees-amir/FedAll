import numpy as np

from fedall.Server import data_transfer_server as dt 
from fedall.Server import compute_loss_acc as la 

def compute_avg(sockets, NumofRounds, avg_model, Data):
    try:
        def avg_models(all_models):
            # The variable "all_models" is a nested list
            # Each row represents the whole model of a single client
            # Each column represents a specific model parameter belongs
            # to all the clients

            # Get the number of matrices in each row
            num_matrices_in_row = len(all_models[0])

            # Compute the average of model at each column position
            # The avg_model will be a list consisting of model parameters
            avg_model = []
            for col in range(num_matrices_in_row):
                col_matrices = [row[col] for row in all_models]
                average_matrix = np.mean(col_matrices, axis=0)
                avg_model.append(average_matrix)

            return avg_model
        
        for r in range(NumofRounds):
            print("Round: " + str(r + 1))

            # Send the average model to all the clients
            dt.send_model_to_clients(avg_model, sockets)

            # Receive the local models from all the clients
            all_models = dt.receive_models_from_clients(sockets)

            # Average the local models received from the clients
            avg_model = avg_models(all_models)
            
            # Compute metrics on the testing data situated at the server
            # to observe the performance of the average model in each round
            [loss, acc] = la.loss_acc(avg_model, Data)
            print("Loss: "+str(loss))
            print("Accuracy: "+str(acc))
        
        return avg_model
    
    except dt.TransferError as te:
        print(f"Error during data transfer: {te}")
        return None
    except dt.ConnectionError as ce:
        print(f"Error during socket connection: {ce}")
        return None
    except la.ModelEvaluationError as me:
        print(f"Error during model evaluation: {me}")
        return None
    except Exception as e:
        print(f"Error during computation: {e}")
        return None