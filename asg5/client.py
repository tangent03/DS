import socket
import time

HOST = "localhost"
PORT = 8080
BUFFER = 1024

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((HOST, PORT))

# Client name
name = input("Enter Client Name: ")

client.send(name.encode())

print(f"{name} Connected")

while True:

    msg = client.recv(BUFFER).decode()

    # TOKEN RECEIVED
    if msg == "TOKEN":

        print(f"\n{name} received TOKEN")

        seconds = int(input("Enter processing time in seconds: "))

        print("Processing...")

        time.sleep(seconds)

        result = f"{name} processed for {seconds} seconds"

        client.send(result.encode())

        print("TOKEN Released\n")

    # CLOSE CONNECTION
    elif msg == "CLOSE":

        print("Server Closed")

        break

client.close()