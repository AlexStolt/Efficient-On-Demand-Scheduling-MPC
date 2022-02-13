import threading
from clients import Clients
from server import Server
from utilities import DataItems
import timeit
import random

# Data Items
TOTAL_DATA_ITEMS = 1000
THETA = 0.8
MIN_DATA_SIZE = 10000
MAX_DATA_SIZE = 30000
DATA_SEED = 100

# Clients
CLIENTS = 100
MIN_DATA_ITEMS = 10
MAX_DATA_ITEMS = 30
CLIENT_SEED = 10
CLIENT_SLEEP_INTERVAL = 1 

# Server
TIME_SLOT = random.randint(1, 3)
BANDWIDTH = 1000
DELTA = 30 # Must allow at least one full request to be downloaded   

DOWN_STREAM = []

if __name__ == '__main__':
 
  # Create a list of all available data items used for data selection based on their probabilities
  data_items = DataItems(TOTAL_DATA_ITEMS, THETA, MIN_DATA_SIZE, MAX_DATA_SIZE, DATA_SEED)

  # Start of execution time
  start = timeit.default_timer()

  # Create list of requests of data items for clients 
  clients = Clients(CLIENTS, data_items, DOWN_STREAM, MIN_DATA_ITEMS, MAX_DATA_ITEMS, CLIENT_SEED, CLIENT_SLEEP_INTERVAL)
  
  # Clients are connected to the server
  server = Server(clients, data_items, DOWN_STREAM, BANDWIDTH, TIME_SLOT, DELTA)

  # Send requests to server
  clients.send_requests()
  
  # Server responds to clients
  server.send_response()

  # End of execution time
  stop = timeit.default_timer()
  

  print('Total Time of Execution: ', stop - start)  
