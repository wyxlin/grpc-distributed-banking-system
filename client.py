import grpc
import json
import banks_pb2
import banks_pb2_grpc
import time
from customer import Customer     

def initialize_customers(input_file):
    # Reads input data and returns initialized Customer instances for each 'customer' entry.
    with open(input_file) as f:
        input_data = json.load(f)
    
    return [
        Customer(item['id'], item['events'])
        for item in input_data if item['type'] == 'customer'
    ]

# iterates over each customer in the customers list and runs their transactions one by one
def process_transactions(customers):   
    for customer in customers:
        customer.createStub()
        customer.executeEvents()
        time.sleep(0.25)           # ensure sequential processing

if __name__ == '__main__':
    customers = initialize_customers('input.json')
    process_transactions(customers)
