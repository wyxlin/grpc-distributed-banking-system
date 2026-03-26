import grpc
import banks_pb2
import banks_pb2_grpc
import json
from pathlib import Path

class Customer:     
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events form the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None
    # TODO: students are expected to create the Customer stub

    def createStub(self):     
            port = str(50000 + self.id)
            channel = grpc.insecure_channel('localhost:' + port)
            self.stub = banks_pb2_grpc.BanksStub(channel)
    
    # TODO: students are expected to send out the events to the bank
    def executeEvents(self):
        for event in self.events:
            print(f"Processing event: {event}") # for debugging

            interface = event["interface"]
            money = event.get("money", 0)
            
            request = banks_pb2.MsgRequest(customer_id=self.id, interface=interface, money=money)
          
            response = self.stub.MsgDelivery(request)

            # process responses from server
            if interface == 'query':
                self.recvMsg.append({"interface": "query", "balance": response.balance})

            elif interface in ['deposit', 'withdraw']:
                self.recvMsg.append({"interface": interface, "result": response.result})

        self.writeToFile() 

    def writeToFile(self):
        output_file = Path('output.json')

        # Load existing data if available; otherwise, start with an empty list
        data = json.loads(output_file.read_text()) if output_file.exists() else []

        # Append the current customer data
        data.append({"id": self.id, "recv": self.recvMsg})

        # Write the updated data back to the file
        output_file.write_text(json.dumps(data))
        
        # For debugging
        print(f"Customer {self.id}'s results written to output.json")
        

