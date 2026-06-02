import socket
import time
import csv
import hashlib

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

file_path = r"C:\Users\tugba\Desktop\NetProbe\test.txt"
packet_size = 256
max_retry = 5

sent = 0
acked = 0
timeout = 0
retrans = 0

rtts = []

start = time.time()

# FILE HASH
with open(file_path, "rb") as f:
    file_data = f.read()
    file_hash = hashlib.md5(file_data).hexdigest()

# SEND HASH FIRST
sock.sendto(file_hash.encode(), (SERVER_IP, SERVER_PORT))

seq = 0

with open(file_path, "rb") as f:
    while True:
        chunk = f.read(packet_size)
        if not chunk:
            break

        packet = seq.to_bytes(4, "big") + chunk

        retry = 0
        ok = False

        while retry < max_retry and not ok:
            send_time = time.time()
            sock.sendto(packet, (SERVER_IP, SERVER_PORT))
            sent += 1

            try:
                ack, _ = sock.recvfrom(1024)
                ack_seq = int.from_bytes(ack, "big")

                if ack_seq == seq:
                    acked += 1
                    ok = True

                    # RTT
                    rtt = time.time() - send_time
                    rtts.append(rtt)

            except:
                timeout += 1
                retrans += 1
                retry += 1

        seq += 1

end = time.time()
duration = end - start

packet_loss = sent - acked
goodput = (acked * packet_size) / duration
throughput = (sent * packet_size) / duration
loss_rate = packet_loss / sent if sent > 0 else 0
avg_rtt = sum(rtts) / len(rtts) if rtts else 0

sock.sendto(b"EOF", (SERVER_IP, SERVER_PORT))

# LOG
with open("../logs/client_log.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Metric", "Value"])
    w.writerow(["Sent", sent])
    w.writerow(["ACK", acked])
    w.writerow(["Timeout", timeout])
    w.writerow(["Retransmission", retrans])
    w.writerow(["Time", duration])
    w.writerow(["Throughput", throughput])
    w.writerow(["Goodput", goodput])
    w.writerow(["PacketLossRate", loss_rate])
    w.writerow(["AvgRTT", avg_rtt])

print("[CLIENT] Done")