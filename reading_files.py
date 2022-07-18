handle = open(filename, mode)
# NOTE: Opeing a file format

fhand = open()
# NOTE: Using open() function to get into a File\n
count = 0
for line in fhand:
    count = count + 1
    print('Line Count:', count)
    # NOTE: Counting Lines in a File
fhand = open()
inp = fhand.read()
print(len(inp))
# NOTE: Reading the *Whole* File\n

fhand = open()
for line in fhand:
    line = line.rstrip()
    if line.startswith():
        print(line)
        # NOTE: Searching Through a File (strip right-hand whitespace

fhand = open()
for line in fhand:
    line = line.rstrip()
    if not line.startswith():
        continue
    print(line)
    # NOTE: Searching Through a File with continue (strip right-hand whitespace)\n

fhand = open()
for line in fhand:
    line = line.rstrip()
    if line not in line:
        continue
    print(line)
    # NOTE: Using "in" to to select any line in a File\n

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith(''):
        count = count + 1
print('', count, '', fname)

# NOTE: Count the lines in a File that have a certain word('')\n

fname = input('Enter the File name: ')
try:
    fhand = open(fname)
except:

    print('File cannot be opened: ', fname)
    quit()
# NOTE: If a File isnt defined use 'try'&'except'Statements\n
