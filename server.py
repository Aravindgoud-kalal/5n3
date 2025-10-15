import socket

def start_server():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(1)

    print("Server started. Waiting for connection...")
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        # Receive message
        msg = conn.recv(1024).decode()
        if msg.lower() == 'exit':
            print("Client ended the chat.")
            break
        print(f"Client: {msg}")

        # Send message
        reply = input("You: ")
        conn.send(reply.encode())

        if reply.lower() == 'exit':
            print("You ended the chat.")
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
