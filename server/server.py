import socket
import hashlib
import random

IP = "0.0.0.0"
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP, PORT))

print("[SERVER] Running...")

received = {}
client_hash = None

while True:
    data, addr = server_socket.recvfrom(65535)
    

    # HASH paketi (client gönderiyor)
    if len(data) < 100:
        try:
            client_hash = data.decode()
            print("[SERVER] Client hash received")
        except:
            pass
        continue

    # LOSS SIMULATION (BONUS)
    if random.random() < 0.2:
        continue

    seq = int.from_bytes(data[:4], "big")
    payload = data[4:]

    if seq not in received:
        received[seq] = payload

    # ACK
    server_socket.sendto(seq.to_bytes(4, "big"), addr)

# dosya oluşturma
with open("received_file.txt", "wb") as f:
    for i in sorted(received.keys()):
        f.write(received[i])

# checksum
with open("received_file.txt", "rb") as f:
    received_hash = hashlib.md5(f.read()).hexdigest()

print("HASH MATCH:", client_hash == received_hash)
print("[SERVER] Done")