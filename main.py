import threading
from clients import Clients
from server import Server
from utilities import DataItems


# Data Items
TOTAL_DATA_ITEMS = 50
THETA = 0.8
MIN_DATA_SIZE = 10
MAX_DATA_SIZE = 40
DATA_SEED = 100

# Clients
CLIENTS = 10
MIN_DATA_ITEMS = 2
MAX_DATA_ITEMS = 10
CLIENT_SEED = 18 
CLIENT_SLEEP_INTERVAL = 1 

# Server
TIME_SLOT = 1
BANDWIDTH = 100
DELTA = 4

DOWN_STREAM = []

if __name__ == '__main__':

  # Create a list of all available data items used for data selection based on their probabilities
  data_items = DataItems(TOTAL_DATA_ITEMS, THETA, MIN_DATA_SIZE, MAX_DATA_SIZE, DATA_SEED)

  # Create list of requests of data items for clients 
  clients = Clients(CLIENTS, data_items, DOWN_STREAM, MIN_DATA_ITEMS, MAX_DATA_ITEMS, CLIENT_SEED, CLIENT_SLEEP_INTERVAL)
  
  # Clients are connected to the server
  server = Server(clients, data_items, DOWN_STREAM, BANDWIDTH, TIME_SLOT, DELTA)

  # Send requests to server
  clients.send_requests()
  
  # Server responds to clients
  server.send_response()


  # for i in clients.get_clients():
  #   i.semaphore.release()


