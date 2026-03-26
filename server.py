import argparse  # For parsing command line arguments
import grpc
from concurrent import futures   
import json
from time import sleep
import banks_pb2
import banks_pb2_grpc
from branch import Branch
import multiprocessing

# start a gRPC server for a given branch
def serveBranch(branch):
    branch.createStub() 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # Create a gRPC server
    banks_pb2_grpc.add_BanksServicer_to_server(branch, server)  # Add the branch servicer to the server
    port = str(50000 + branch.id) 
    server.add_insecure_port("[::]:" + port) 
    server.start() 
    server.wait_for_termination()  # Wait for the server to finish

# create and manage branch processes
def createProcesses(processes):
    branchIds = []  
    branches = [] 
    branchProcesses = [] 

    # Instantiate Branch objects from the provided processes
    for process in processes:
        if process["type"] == "branch": 
            branch = Branch(process["id"], process["balance"], branchIds)  # Create a new Branch object
            branches.append(branch)  
            branchIds.append(branch.id)  
    
    for branch in branches:
        branch_process = multiprocessing.Process(target=serveBranch, args=(branch,))  # Create a process for each branch
        branchProcesses.append(branch_process) 
        branch_process.start() 

    
    sleep(0.25)  # Sleep for a short period to ensure branches have time to initialize

    return branchProcesses  # Return the list of branch processes

if __name__ == "__main__":
    # Setup command line argument for 'input_file'
    parser = argparse.ArgumentParser() 
    parser.add_argument("input_file")  
    args = parser.parse_args() 

    try:
        with open(args.input_file) as f:
            input = json.load(f)
        
        createProcesses(input) 
    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        exit(1)

    
