import zmq
import pandas as pd




def receive():
    """
    This function receives the zip code from send.py and returns back the first 5 matching zip codes that match the zone received. 
    """

    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Use REP to receive requests
    socket.bind("tcp://localhost:5555")
    
    file = 'phzm_us_zipcode_2023.csv'
    df = pd.read_csv(file)

    print("Server is ready to receive messages...")
    while True:
        message = socket.recv_string()

        # Error-Handling
        if message in ["exit", "quit", "q", "kill"]:
            print(f"Ending this receive session")
            break
        elif not message.isdigit():
            print(f"Invalid entry. Not numerical character detected. Disregarding! ")

        elif message.isdigit():
            message = int(message)
            matching_zone = df.loc[df['zipcode'] == message, 'zone'].values[0]
            if matching_zone:
                matching_zips = df.loc[df['zone'] == matching_zone, 'zipcode'].head(5).astype(str).str.zfill(5).reset_index(drop=True)
                matching_zips_json = matching_zips.to_json()
                socket.send_string(matching_zips_json)
                print(f"Response Message Sent: {matching_zips_json}")
            else: 
                print(f"Unable to find zip code in phzm DB.")
                socket.send_string("No return from phzm DB.")
        
        # Exit condition
        
if __name__ == "__main__":
    receive()
