# gRPC Distributed Banking System

## Overview

This project implements a distributed banking system using Python and gRPC. It simulates communication between multiple client processes (customers) and server nodes (branches), where each branch maintains a replicated account balance.

The system supports basic banking operations and ensures consistency across distributed replicas through inter-node communication.

---

## Tech Stack

* Python
* gRPC
* Protocol Buffers

---

## Key Features

* Implemented RPC-based communication between clients and server nodes using gRPC
* Designed service interfaces using Protocol Buffers (.proto)
* Developed core banking operations: Deposit, Withdraw, and Query
* Implemented branch-to-branch communication to propagate updates
* Maintained consistency across distributed replicas
* Simulated distributed behavior using multiple Python processes

---

## System Design

* Each client communicates with a specific branch node
* Branch nodes process client requests and propagate updates to other branches
* All branches maintain a consistent account balance across the system
* Sequential execution is used to simplify consistency handling

---

## Project Structure

```
protos/
  banks.proto
server.py
client.py
branch.py
customer.py
input.json
output.json
requirements.txt
```

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the system

```bash
python server.py input.json
python client.py input.json
```

---

## Highlights

* Designed and implemented a distributed system with replicated state
* Applied RPC communication patterns using gRPC
* Demonstrated understanding of distributed system consistency and inter-process communication
* Built a multi-process system simulating real-world distributed interactions

---

## Notes

* The system assumes no concurrent updates for simplicity
* All operations are executed sequentially to ensure correctness
