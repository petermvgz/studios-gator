import urllib.request
import urllib.parse
import urllib.error
# Make socket and HTTP communications better
phand = urllib.request.urlopen('http://github.com')

for x in phand:
    print(x.decode().strip())
# using urrlib in Python

fhand = urllib.request.urlopen('http://github.com')

counts = dict()
for x in fhand:
    words = x.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
# Like a File...

fhand = urllib.request.urlopen('http://github.com')
for line in fhand:
    print(line.decode().strip())
# Reading Web Pages
