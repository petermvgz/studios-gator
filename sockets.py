import socket
petersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
petersock.connect(('github.com', 80))
cmd = 'GET https://github.com/ HTTP/1.0\n\n'.encode()
petersock.send(cmd)
# An HTTP Request software from Internet in Python
while True:
    data = petersock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
petersock.close()
# How to Ask Server to receive Data
# Sending HTTP Request inside & outside Python
