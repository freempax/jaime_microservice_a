from pyzipcode import ZipCodeDatabase
import zmq

def send():
    """
    This function continuously prompts the user to send a zip code to the receive function.
    It will keep running until the user enters 'exit'.
    """
    zcdb = ZipCodeDatabase()
    zmq_address = "tcp://localhost:5555"
    
    state_abbreviations = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", 
        "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", 
        "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", 
        "WI", "WY"
    ]

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(zmq_address)

    while True:
        func_input = input("Please enter a city, a 5-digit zip code, or type 'exit' to quit: ").strip()
        
        # Exit condition
        if func_input.lower() in ["exit", "quit", "q", "kill"]:
            socket.send_string("exit")
            print("Exiting the send function.")
            break

        elif func_input.isdigit() and len(func_input) == 5:
            zip_code = func_input
        else:
            state_input = input("Please enter the 2-character abbreviation for the state: ").upper().strip()
            while state_input not in state_abbreviations:
                state_input = input("Invalid State entry. Please enter a valid 2-character abbreviation: ").upper().strip()
            if state_input in ["exit", "quit", "q", "kill"]:
                socket.send_string("exit")
                print("Exiting the send function.")
                break

            zip_code_result = zcdb.find_zip(city=func_input, state=state_input)
            if zip_code_result:
                zip_code = zip_code_result[0].zip
            else:
                print("No ZIP code found for the given input.")
                continue

        # Send the zip code to the specified server
        socket.send_string(zip_code)
        response = socket.recv_string()  # Wait for response (optional)
        print(f"Response from server: {response}")

    # Close the socket and terminate the context when done
    socket.close()
    context.term()

if __name__ == "__main__":
    send()
