# Node Selector
This project implements a node selection algorithm using Python with multithreading and TCP sockets. It simulates a communication topology with three nodes: N1 (Server), N2 (Client), and N3 (Client).

## Files Overview:
### 1. main.py:
Contains the server-client communication logic.
  * N1 (Server) increments a number and sends it to N2 and N3.
  * N2 checks if the number is divisible by 3 and sends an ACK.
  * N3 checks if the number is divisible by 5 and sends an ACK.
### 2. tcp.py:
Provides utility functions for creating and managing TCP server and client connections.

## Process Overview:
### N1 (Server):
Increments a number from 1 to 100 and sends it to N2 and N3 every 0.5 seconds.
### N2 (Client):
Sends an ACK if the number is divisible by 3.
### N3 (Client):
Sends an ACK if the number is divisible by 5.
