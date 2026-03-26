# gRPC Distributed Banking System

## Overview

Built a distributed banking system using Python and gRPC to simulate communication between multiple clients and server nodes. The system maintains replicated account balances across multiple branches and ensures consistency through inter-node communication.

## Tech Stack

* Python
* gRPC
* Protocol Buffers

## Key Features

* Implemented RPC-based communication between clients and server nodes using gRPC
* Designed service interfaces using Protocol Buffers (.proto)
* Developed core banking operations: Deposit, Withdraw, and Query
* Implemented branch-to-branch propagation to synchronize state across distributed replicas
* Simulated distributed processes using multiple Python processes

## System Design

* Each client interacts with a specific branch node
* Branch nodes handle requests and propagate updates to other branches
* All nodes maintain a consistent account balance across the system

## Project Structure

```
server.py
client.py
branch.py
customer.py
banks.proto
input.json
output.json
```

## How to Run

```bash
python server.py input.json
python client.py input.json
```

## Highlights

* Designed and implemented a distributed system with replicated state
* Applied RPC communication patterns in a real-world simulation
* Demonstrated understanding of distributed system consistency and inter-process communication
  
