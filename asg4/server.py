import socket
import time
import json

SERVER_IP = "127.0.0.1"
PORT = 5000


def get_local_time():
    return int(time.time() * 1000)


def format_time(ms):
    return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(ms / 1000))


def main():

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind IP and port
    server_socket.bind((SERVER_IP, PORT))

    # Listen for clients
    server_socket.listen(5)

    print(f"Server started at {SERVER_IP}:{PORT}")

    # Server local time
    server_time = get_local_time()

    print(f"Server Time : {format_time(server_time)}")

    clients = []

    # Accept clients
    while True:

        client_socket, address = server_socket.accept()

        print(f"\nConnected with {address}")

        clients.append(client_socket)

        choice = input("Add more clients? (y/n): ")

        if choice.lower() == 'n':
            break

    client_times = []

    # Request time from clients
    for client_socket in clients:

        request = {
            "operation": "time_req"
        }

        client_socket.send(json.dumps(request).encode())

        response = json.loads(client_socket.recv(1024).decode())

        client_time = int(response["client_time"])

        client_times.append(client_time)

        print(f"Client Time : {format_time(client_time)}")

    # Calculate synchronized time
    avg_time = (server_time + sum(client_times)) // (len(client_times) + 1)

    print(f"\nSynchronized Time : {format_time(avg_time)}")

    # Send adjustment
    for i, client_socket in enumerate(clients):

        adjustment = avg_time - client_times[i]

        message = {
            "operation": "time_adj",
            "adjusted_time": adjustment
        }

        client_socket.send(json.dumps(message).encode())

        print(f"Adjustment sent : {adjustment} ms")

        client_socket.close()

    server_socket.close()


if __name__ == "__main__":
    main()