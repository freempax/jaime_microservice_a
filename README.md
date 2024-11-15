Zip Code Zone Finder

This application allows a user to input a zip code, and return back a list of zones that match that zip code. It uses the customer's provided csv file for the data source. 

The modules needed for this application are pyzipcode, zmq, and pandas. If you do not have these modules installed, you can install them on your own, or open up CMD, navigate to where you have the files stored and, and run "pip install -r requirements.txt" to install the modules.

The communication method for this application will be ZMQ. The default settings is to use local host on port 5555, but the user can change this address and port as needed. 



Steps to Initiate the calls:
1. The user first needs to start the server that is going to receive this communication so the user needs to initiate the receive.py process. 
2. The user is then able to run the send.py process to enter a zip code or a City/State combination that is translated to a zip code, and sent to the receive.py server. 
3. The user then gets back 5 zip codes that match the zone of the zip code entered in step 2. 

Step to Close the Application:
If you need to exit from the server, and the program, enter quit, q, or exit. It should end both the send, and receive scripts. 


Example of Communication Input, and Out:
C:\Users\Paxton\Documents\Oregon-State-Univ\Soft_Engr 1 CS_361\jaime_microservice_b>python send.py
Please enter a city, a 5-digit zip code, or type 'exit' to quit: 90210
Response from server: {"0":"33026","1":"33028","2":"33030","3":"33031","4":"33034"}

![image](https://github.com/user-attachments/assets/53edcc6e-5037-4792-aabb-e407c6edfe22)
