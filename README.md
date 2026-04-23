# 🔐 Secure File Transfer System (Socket Programming)

## 📌 Overview

This project implements a secure client-server file transfer system using Python sockets with SSL/TLS encryption. It supports encrypted communication, multi-client handling, and efficient file streaming for large files.

---

## 🚀 Features

* Secure communication using SSL/TLS encryption
* Multi-threaded server to handle multiple clients concurrently
* File transfer in chunks for efficient large file handling
* Dynamic file selection (small and large test files)
* Basic protocol with filename and filesize transmission
* Progress tracking during file download
* Error handling for connection drops

---

## 🛠️ Tech Stack

* Python
* Socket Programming (TCP)
* SSL/TLS Encryption
* Multithreading

---

## ⚙️ How It Works

### Server:

* Listens for incoming client connections
* Wraps socket with SSL for secure communication
* Handles each client in a separate thread
* Sends file metadata (name + size) followed by file data

### Client:

* Establishes secure connection to server
* Receives file metadata
* Downloads file in chunks and displays progress

---

## ▶️ How to Run

### 1. Generate test files

```bash
python generate_files.py
```

### 2. Run server

```bash
python server.py
```

### 3. Run client

```bash
python client.py
```

---

## 🔐 SSL Note

This project uses self-signed certificates for demonstration purposes.

To generate your own certificates:

```bash
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
```

---

## 🧠 Architecture

Client → SSL Socket → Multi-threaded Server → File System

---

## ⚠️ Limitations

* Uses self-signed certificates (not production secure)
* No user authentication implemented
* Fixed chunk size (1024 bytes)

---

## 🚀 Future Improvements

* Add authentication system
* Support file uploads from client
* Resume interrupted downloads
* Add GUI interface

---

## 📊 Learning Outcomes

* Understanding of TCP socket programming
* Secure communication using SSL/TLS
* Handling concurrency with threads
* Efficient file transfer techniques

---

## 👨‍💻 Author

Prajin R
