print(ord('H'))
print(ord('\n'))
print(ord('P'))
print(ord('e'))
print()
# Prepresenting Simple Strings
# We refer to "8 bits of memory as a "byte" of memory
# Each character is repped by a number between 0 and 256 stored in 8 bits

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
mystring = data.decode()
print(mystring)
