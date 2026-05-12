import socket
import threading
import time

HOST = "localhost"
PORT = 8080
TOKEN = "TOKEN"
BUFFER = 1024

clients = []

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
server.bind((HOST, PORT))

# Listen
server.listen()

print("Server Started...")
print("Waiting for Clients...\n")


# ACCEPT CLIENTS
def accept_clients():

    while True:

        client, addr = server.accept()

        name = client.recv(BUFFER).decode()

        clients.append((client, name))

        print(f"\n[CONNECTED] {name} joined the ring")

        show_ring()


# SHOW RING
def show_ring():

    print("\nCurrent Ring:")

    for i, (_, name) in enumerate(clients):

        print(f"{i+1}. {name}")

    print()


# START TOKEN RING
def start_ring():

    if len(clients) == 0:

        print("No clients connected")

        return

    print("\nStarting Token Ring...\n")

    index = 0

    while True:

        client, name = clients[index]

        try:

            print(f"\n[TOKEN] Token transferred to {name}")

            client.send(TOKEN.encode())

            response = client.recv(BUFFER).decode()

            print(f"[DONE] {response}")

        except:

            print(f"{name} disconnected")

            clients.pop(index)

            if len(clients) == 0:
                break

            continue

        index = (index + 1) % len(clients)

        time.sleep(1)


# THREAD FOR CLIENTS
threading.Thread(target=accept_clients, daemon=True).start()


# MENU
while True:

    print("\n========= MENU =========")
    print("1. Show Ring")
    print("2. Start Token Ring")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        show_ring()

    elif choice == "2":

        start_ring()

    elif choice == "3":

        for client, name in clients:

            try:

                client.send("CLOSE".encode())

                client.close()

            except:
                pass

        server.close()

        print("Server Closed")

        break