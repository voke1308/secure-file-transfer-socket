import socket
import ssl
import threading
import random
import os

HOST = "0.0.0.0"
PORT = 5000

# SSL setup
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="certs/cert.pem", keyfile="certs/key.pem")

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("🔐 Secure Server running on port", PORT)


def handle_client(conn, addr):
    print(f"\n[+] Client connected: {addr}")

    # Random file selection
    file_choice = random.choice([
        "test-files/small.bin",
        "test-files/large.bin"
    ])

    print(f"[📂] Sending {file_choice} to {addr}")

    if not os.path.exists(file_choice):
        print(f"[❌] File not found: {file_choice}")
        conn.close()
        return

    try:
        with open(file_choice, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                try:
                    conn.sendall(data)
                except Exception:
                    print(f"[⚠️] Client {addr} disconnected early")
                    break

        print(f"[✅] Transfer complete → {addr}")

    except Exception as e:
        print("[❌] Error:", e)

    finally:
        conn.close()
        print(f"[🔌] Connection closed: {addr}")


# Accept clients
while True:
    client_socket, addr = server.accept()

    try:
        secure_socket = context.wrap_socket(client_socket, server_side=True)
    except Exception as e:
        print("[SSL ERROR]", e)
        client_socket.close()
        continue

    thread = threading.Thread(target=handle_client, args=(secure_socket, addr))
    thread.start()