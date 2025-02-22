---
title: "Client-Server Setup with Termux and Linux Laptop"
description: "A step-by-step guide to setting up a client-server system using a Linux laptop and a mobile device with Termux."
date: "2025-02-22"
categories: ["Networking", "Python", "Linux", "Termux"]
---

## Step 1: Prerequisites

### Linux Laptop
- Ensure Python (Python 3.x) is installed.

### Mobile Device (Termux)
- Install Python and necessary tools in Termux:
  ```bash
  pkg install python
  ```

### Network
- Both devices must be on the same network (Wi-Fi or hotspot).

## Step 2: Server Script (Linux Laptop)
The server script listens for incoming connections and executes commands sent by the client.

```python
# server.py
import socket
import subprocess

# Server configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345       # Port to listen on

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")

        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        with client_socket:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"Received command: {data}")
                try:
                    output = subprocess.getoutput(data)
                except Exception as e:
                    output = str(e)
                client_socket.sendall(output.encode('utf-8'))

if __name__ == "__main__":
    start_server()
```

## Step 3: Client Script (Termux)
The client script connects to the server and sends commands to be executed.

```python
# client.py
import socket

# Server configuration
SERVER_IP = '192.168.1.100'  # Replace with the actual IP address of the Linux laptop
SERVER_PORT = 12345          # Port to connect to

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")
        
        while True:
            command = input("Enter command (or 'exit' to quit): ")
            if command.lower() == 'exit':
                break
            client_socket.sendall(command.encode('utf-8'))
            output = client_socket.recv(4096).decode('utf-8')
            print(f"Output:\n{output}")

if __name__ == "__main__":
    start_client()
```

## Step 4: Running the Scripts

### On the Linux Laptop (Server)
1. Save the server script as `server.py`.
2. Run the server script:
   ```bash
   python3 server.py
   ```
3. Note the IP address of the laptop using:
   ```bash
   ifconfig
   ```
   or
   ```bash
   ip a
   ```

### On the Mobile Device (Termux)
1. Save the client script as `client.py`.
2. Replace `SERVER_IP` in the client script with the laptop's IP address.
3. Run the client script:
   ```bash
   python3 client.py
   ```

## Step 5: Usage
- Enter commands in the Termux client (e.g., `ls`, `pwd`, `whoami`).
- The server executes the commands and sends back the output.

## Step 6: Security Considerations
This setup lacks security features and is intended for educational purposes.

### To secure the setup:
- Use **SSH** instead of raw sockets.
- Implement encryption (e.g., **TLS/SSL**).
- Restrict access to trusted devices.

## Flow Explanation
1. The server listens on a specific IP and port.
2. The client connects using the server's IP and port.
3. The client sends commands to the server.
4. The server executes the commands and returns the output.
5. The client displays the output.

This setup allows you to control your Linux laptop from a mobile device using Termux. Let me know if you need further assistance!
