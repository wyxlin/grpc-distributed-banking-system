# gRPC Distributed Banking System

## Overview
This project implements a distributed banking system using Python and gRPC. It simulates communication between multiple client processes (customers) and server nodes (branches), where each branch maintains a replicated account balance.

## Tech Stack
- Python
- gRPC
- Protocol Buffers

## Features
- Implemented RPC communication between clients and servers using gRPC  
- Designed and defined services using Protocol Buffers (.proto)  
- Supported core banking operations: Query, Deposit, Withdraw  
- Implemented branch-to-branch communication to propagate updates  
- Maintained consistency across distributed replicas  

## Architecture
- Each customer communicates with a specific branch  
- Branch servers process requests and propagate updates to other branches  
- All branches maintain a consistent account balance  

## Project Structure
- banks.proto
- Server.py
- client.py
- branch.py
- customer.py
- input.json
- output.json

## How to Run
```bash
python server.py input.json
python client.py input.json

  
