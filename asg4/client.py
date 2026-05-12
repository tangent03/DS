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
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client_socket.connect((SERVER_IP, PORT))

    print(f"Connected to {SERVER_IP}:{PORT}")

    # Client local time
    client_time = get_local_time()

    print(f"\nInitial Client Time : {format_time(client_time)}")

    while True:

        server_response = json.loads(client_socket.recv(1024).decode())

        # Send local time
        if server_response["operation"] == "time_req":

            data = {
                "client_time": client_time
            }

            client_socket.send(json.dumps(data).encode())

        # Receive adjustment
        elif server_response["operation"] == "time_adj":

            adjustment = int(server_response["adjusted_time"])

            print(f"\nAdjustment Received : {adjustment} ms")

            client_time += adjustment

            print(f"Adjusted Time : {format_time(client_time)}")

            break

    client_socket.close()


if __name__ == "__main__":
    main()