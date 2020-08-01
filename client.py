import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

HEADER_SIZE = 10
while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(8)
        if new_msg:
            print(f"new mssage len: {msg[:HEADER_SIZE]}")
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False

        full_msg += msg.decode('utf-8')

        if len(full_msg)-HEADER_SIZE == msglen:
            print("Full message received")
            print("Message:",full_msg[HEADER_SIZE:])
            full_msg = ''
            break

    print(full_msg)
    # print(msg.decode('utf-8'))

