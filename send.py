# This code is to send the zip code to the receive.py script
# The code should take the input of either a zip code, or a city and state
# reference a csv to correlate a city name to a zip code, and send a zip code to the receive.py file

import pandas as pd
from pyzipcode import ZipCodeDatabase
import zmq




# # df["state"] = df["zp"].map(lambda x: zcdb[x].state)
# # print(zcdb.find_zip(city="Dallas"))
# dal = zcdb.find_zip(city="Dallas", state="ATX)[0]
# # for zip in dal:
# #     print(zip)
# print(dal)
# # print(dallas)

def send(func_input, zmq_address):
    zcdb = ZipCodeDatabase()
    
    state_abbreviations = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", 
    "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", 
    "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", 
    "WI", "WY"]


    if func_input.isdigit():
        zip_code = func_input
        # print(f"Entry is a zip code: {zip_code}")
        return zip_code
    else:
        state_input = input("Please enter 2 character abbreviation for the state (No need to worry about Upper/Lower case!): ").upper()
        # if state not in state_abbreviations:
        while state_input not in state_abbreviations:
            state_input = input("Invalid State entry.\nPlease enter 2 character abbreviation for the state (No need to worry about Upper/Lower case!): ").upper()
        zip_code = zcdb.find_zip(city=func_input, state=state_input)
        if zip_code:
            # zip_code = zip_code[0]['zip']
            zip_code = zip_code[0].zip
            # print(zip_code)
            # print(zip_code.zip)
            # print(type(zip_code))
            # for data in zip_code:
            #     print(data)
            # return zip_code
            context = zmq.Context()
            socket = context.socket(zmq.REQ)  # Use REQ to send a request
            socket.connect(zmq_address)
            socket.send_string(zip_code)
            # Wait for a response (optional)
            response = socket.recv_string()
            print(f"Response from server: {response}")
        else:
            print("No ZIP code found for the given input.")
    # Close the socket and terminate the context
        socket.close()
        context.term()


    


if __name__ == "__main__":
    zmq_address_input = input("Please enter the ZMQ server address: ") # Example ("tcp://localhost:5555")
    zmq_address_input = "tcp://localhost:5555"
    usr_input = input("Please enter a city, or a zip code: ")
    send(usr_input, zmq_address_input)












import pandas as pd
from pyzipcode import ZipCodeDatabase
import zmq

def send(func_input, zmq_address):
    zcdb = ZipCodeDatabase()
    
    state_abbreviations = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", 
    "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", 
    "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", 
    "WI", "WY"]

    if func_input.isdigit():
        zip_code = func_input
        return zip_code
    else:
        state_input = input("Please enter 2 character abbreviation for the state (No need to worry about Upper/Lower case!): ").upper()
        # if state not in state_abbreviations:
        while state_input not in state_abbreviations:
            state_input = input("Invalid State entry.\nPlease enter 2 character abbreviation for the state (No need to worry about Upper/Lower case!): ").upper()
        zip_code = zcdb.find_zip(city=func_input, state=state_input)
        if zip_code:
            zip_code = zip_code[0].zip
            context = zmq.Context()
            socket = context.socket(zmq.REQ)  # Use REQ to send a request
            socket.connect(zmq_address)
            socket.send_string(zip_code)
            # Wait for a response (optional)
            response = socket.recv_string()
            print(f"Response from server: {response}")
        else:
            print("No ZIP code found for the given input.")
    # Close the socket and terminate the context
        socket.close()
        context.term()


if __name__ == "__main__":
    zmq_address_input = "tcp://localhost:5555"
    usr_input = input("Please enter a city, or a zip code: ")
    send(usr_input, zmq_address_input)

    