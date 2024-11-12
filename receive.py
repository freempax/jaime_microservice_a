import zmq
import pandas as pd




def receive(zmq_address):
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Use REP to receive requests
    socket.bind(zmq_address)
    
    file = 'phzm_us_zipcode_2023.csv'
    df = pd.read_csv(file)

    print("Server is ready to receive messages...")
    while True:
    # while True and not KeyboardInterrupt:
        # Wait for the next message from the client
        message = socket.recv_string()
        # print(f"Received ZIP code: {message}")
        if message.isdigit():
            message = int(message)
            matching_zone = df.loc[df['zipcode'] == message, 'zone'].values[0]
            # matching_zips = df.loc[df['zone'] == matching_zone].head(5),'zipcode'
            # matching_zips = df.loc[df['zone'] == matching_zone, 'zipcode'].head(5).reset_index(drop=True).astype(str).str.zfill(5)
            matching_zips = df.loc[df['zone'] == matching_zone, 'zipcode'].head(5).astype(str).str.zfill(5).reset_index(drop=True)
            # matching_zips = df.loc[df['zone'] == matching_zone, 'zipcode'].head(5).reset_index(drop=True).zfill(5)
            print(matching_zips)
            matching_zips_json = matching_zips.to_json()
            socket.send_string(matching_zips_json)
            print(f"Response Message Sent: {matching_zips_json}")
        elif not message.isdigit():
            print(f"Invalid entry. Not numerical character detected. Disregarding! ")
        elif message in ["exit", "quit", "q", "kill"]:
            print(f"Ending this session")
            break
        # if message in ['q', 'quit', 'kill', 'exit']:
        #     print(f"Ending this session")
        #     break
            

        # Respond to the client (optional)
        # response_message = f"ZIP code {message} received successfully."
        # socket.send_string(response_message)
        # print(f"Response Message Sent: {response_message}")

if __name__ == "__main__":
    # zmq_address_input = "tcp://*:5555"  # Use * to bind to all interfaces
    # zmq_address_input = "tcp://127.0.0.1:5555"  # Use * to bind to all interfaces
    zmq_address_input = "tcp://localhost:5555"  # Use * to bind to all interfaces
    receive(zmq_address_input)
