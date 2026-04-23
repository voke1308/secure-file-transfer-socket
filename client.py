import socket
import ssl

HOST = "127.0.0.1"   # Change to server IP if needed
PORT = 5000

# Toggle SSL verification
VERIFY_SSL = False

if VERIFY_SSL:
    context = ssl.create_default_context()
else:
    context = ssl._create_unverified_context()

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = context.wrap_socket(sock, server_hostname=HOST)

secure_socket.connect((HOST, PORT))

with open("received.bin", "wb") as file:
    while True:
        data = secure_socket.recv(1024)
        if not data:
            break
        file.write(data)

secure_socket.close()

print("✅ File download complete")