import pandas as pd
from pyzipcode import ZipCodeDatabase
import zmq

def send():
    """
    This function sends a zip code to the receive function. It is 
    """
    zcdb = ZipCodeDatabase()
    zmq_address = "tcp://localhost:5555"
    
    state_abbreviations = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", 
        "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", 
        "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", 
        "WI", "WY"
    ]

    func_input = input("Please enter a city, or a 5-digit zip code: ")
    
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(zmq_address)

    while not func_input:
        func_input = input("No input detected. Please re-try entering a city or a 5-digit zip code: ")
    if func_input.isdigit():
        zip_code = func_input
    else:
        state_input = input("Please enter 2 character abbreviation for the state (No need to worry about Upper/Lower case!): ").upper()
        while state_input not in state_abbreviations:
            state_input = input("Invalid State entry.\nPlease enter 2 character abbreviation for the state (No need to worry about Upper/Lower case!): ").upper()

        zip_code_result = zcdb.find_zip(city=func_input, state=state_input)
        if zip_code_result:
            zip_code = zip_code_result[0].zip
        else:
            print("No ZIP code found for the given input.")
            socket.close()
            context.term()
            return

    # Send the zip code to the specified server
    socket.send_string(zip_code)
    response = socket.recv_string()  # Wait for response (optional)
    print(f"Response from server: {response}")

    # Close the socket and terminate the context
    socket.close()
    context.term()

if __name__ == "__main__":
    # zmq_address_input = "tcp://localhost:5555"
    # zmq_address_input = "tcp://127.0.0.1:5555"
    # usr_input = input("Please enter a city, or a 5-digit zip code: ")
    # send(usr_input, zmq_address_input)
    # send(usr_input)
    send()
