import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

HEADER_SIZE = 10
while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(8)
        if new_msg:
            print(f"new mssage len: {msg[:HEADER_SIZE]}")
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADER_SIZE == msglen:
            print("Full message received")
            print("Message:",full_msg[HEADER_SIZE:])
            d = pickle.loads(full_msg[HEADER_SIZE:])
            full_msg = b''
            # break

            full_msg = b''
            new_msg = True

            print(d)

    # print(msg.decode('utf-8'))

