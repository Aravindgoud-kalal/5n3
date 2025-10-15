import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    print("Connected to the server. Type 'exit' to end chat.\n")

    while True:
        # Send message
        msg = input("You: ")
        client_socket.send(msg.encode())

        if msg.lower() == 'exit':
            print("You ended the chat.")
            break

        # Receive reply
        reply = client_socket.recv(1024).decode()
        if reply.lower() == 'exit':
            print("Server ended the chat.")
            break

        print(f"Server: {reply}")

    client_socket.close()

if __name__ == "__main__":
    start_client()