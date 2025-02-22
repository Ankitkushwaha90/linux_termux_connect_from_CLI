# client.py
import socket

# Server configuration
SERVER_IP = '192.168.1.100'  # Replace with the IP address of the Linux laptop
SERVER_PORT = 12345          # Port to connect to

def start_client():
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")

        while True:
            # Get user input
            command = input("Enter command (or 'exit' to quit): ")
            if command.lower() == 'exit':
                break

            # Send the command to the server
            client_socket.sendall(command.encode('utf-8'))

            # Receive the output from the server
            output = client_socket.recv(4096).decode('utf-8')
            print(f"Output:\n{output}")

if __name__ == "__main__":
    start_client()
