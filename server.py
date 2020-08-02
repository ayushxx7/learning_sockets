import socket, time, pickle

### What is a socket?
# It is an endpoint that receives data. socket sends and receives data. 
# socket itself is not the communication, it's just an endpoint that receives that communication.
# the endpoint sits at an IP & and a PORT.


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

HEADER_SIZE = 10
while True: #listen forever.
    clieentsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    # msg = 'Welcome to the server!'

    d = {1: "hey", 2: "there"}
    msg = pickle.dumps(d)
    print(msg)

    msg = bytes(f'{len(msg):<{HEADER_SIZE}}', "utf-8")+msg

    clieentsocket.send(msg)

#     while True:
#         time.sleep(3)
#         msg = f"The current time is: {time.time()}"
#         msg = f'{len(msg):<{HEADER_SIZE}}'+msg
#         clieentsocket.send(bytes(msg, "utf-8"))

