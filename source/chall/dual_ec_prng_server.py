#!/usr/bin/env python3

import socket
import threading
import hashlib
import time
import os
from Crypto.Cipher import AES

# CTF Challenge Parameters (Manually Chosen)
PRNG_PARAMS = """
P = (6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
Q = (69fce7770c38dca71d26f2f2c95aeb81999003322330a7b30962e0acdba23768, aec52c3d1bae7844230f438eb38b7c1af6c33025ec5aad766ec63a19aac25b49)
d = 32cc126523371d8448638652f70087ba01056ae925c192dc439aaa4093e67c3c
dQ = (6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
a = -3
b = 5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
Observed a 32-byte block of output:
128de40016ea477dff180dd4743aa080c12d5621852c3be4fe64ffae0433fd5b

Given the above, what is the internal state of this PRNG?
"""

# Precomputed correct answer (hashed for security)
CORRECT_ANSWER_HASH = hashlib.sha256(b"8f6ee7d05b633f3c8943a9e76522d612492a62ecb44da3e6d9580629").hexdigest()

# Load the AES key from an environment variable (secure)
KEY = bytes.fromhex(os.getenv("FLAG_KEY", "00000000000000000000000000000000"))  # Default to all zeros if missing

# Encrypted flag (Replace with your actual encrypted flag)
ENCRYPTED_FLAG = "7712a457635fa164e7e924a2696238ffa3706cffdcc27f7e29099bed59738455c0e820a49bf62ecb2fa38c736d7e4e7d95bd9b46aec7bb2259b081573bc0c46e"

def decrypt_flag():
    """Decrypt the flag before sending it"""
    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(ENCRYPTED_FLAG)).decode()
    return decrypted.rstrip(decrypted[-1])  # Remove padding

# Timeout in seconds
TIMEOUT = 5
HOST = "0.0.0.0"  # Bind to all available interfaces
PORT = 1337       # Example port

def handle_client(conn, addr):
    try:
        print(f"[*] Connection from {addr}")

        # Send challenge parameters
        conn.sendall(PRNG_PARAMS.encode() + b"\nEnter your answer: ")

        # Set timeout for receiving input
        conn.settimeout(TIMEOUT)

        # Receive user input
        user_input = conn.recv(1024).strip().decode()

        # Validate input
        if hashlib.sha256(user_input.encode()).hexdigest() == CORRECT_ANSWER_HASH:
            conn.sendall(f"Correct! Here is your flag: {decrypt_flag()}\n".encode())
        else:
            conn.sendall(b"Wrong answer! Try again.\n")

    except socket.timeout:
        conn.sendall(b"Timeout! You took too long.\n")
    except Exception as e:
        print(f"[!] Error handling client {addr}: {e}")
    finally:
        conn.close()

def start_server():
    """Start the TCP challenge server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
