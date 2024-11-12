# This script receives a zip code, and returns the top 5 matching entries from teh phzm_us_zipcode_2023.csv file provided by the customer. 

import pandas as pd
import zmq

file = 'phzm_us_zipcode_2023.csv'
df = pd.read_csv(file)

#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back

zip_code = 80201
matching_zone = df.loc[df['zipcode'] == 72719, 'zone'].values[0]
print(matching_zone)


print(df.loc[df['zone'] == matching_zone],'zipcode')


# context = zmq.Context()

# #  Socket to talk to server
# print("Connecting to hello world server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")

# #  Do 10 requests, waiting each time for a response
# for request in range(10):
#     print(f"Sending request {request} …")
#     socket.send(b"Hello")

#     #  Get the reply.
#     message = socket.recv()
#     print(f"Received reply {request} [ {message} ]")
