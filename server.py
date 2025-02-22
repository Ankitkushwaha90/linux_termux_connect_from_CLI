# server.py
import socket
import subprocess

# Server configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345      # Port to listen on

def start_server():
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address and port
        server_socket.bind((HOST, PORT))
        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")

        # Accept a connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        with client_socket:
            # Start an interactive process (e.g., msfconsole)
            process = subprocess.Popen(
                ['msfconsole'],  # Replace with any interactive tool
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                universal_newlines=True
            )

            while True:
                # Receive data from the client
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                # Send the data to the process's stdin
                process.stdin.write(data)
                process.stdin.flush()

                # Read the process's stdout and send it back to the client
                output = process.stdout.read(1024)
                client_socket.sendall(output.encode('utf-8'))

if __name__ == "__main__":
    start_server()
