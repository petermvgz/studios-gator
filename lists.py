x = 2
x = 4
print(x)
# NOTE: Not a "collection"(Varibles only have one value)

friends = ['Dylan', 'Alyssa', 'Sally']
# NOTE: Collection

print([1, 2, 3])
print(['red', 'yellow', 'green'])
print([4, [7, 9], 6])
print([])
# NOTE: list constants

for i in [1, 2, 3, 3, 4]:
    print(i)
print('Annoying')
# NOTE: list using "for" & "in"

friends = ['Dylan', 'Alyssa' 'Sally']
for friend in friends:
    print('Happy New Year', friend)
print('Hoe!')
z = ['Dylan', 'Alyssa', 'Sally']
for x in z:
    print('Happy You Came:', x)
print('Done')
# NOTE: list using "for" & "in" definite loops

friends = ['Dylan', 'Alyssa', 'Sally']
print(friends[1])
# NOTE: Dylan = 0, Alyssa = 1, Sally = 2
# NOTE: looking inside a list

fruit = 'Apple'
x = fruit.lower()
print(x)
# NOTE: make a string lower case

lotto = [2, 14, 5, 40, 46]
print(lotto)
lotto[2] = 31
print(lotto)
# NOTE: List are "mutable" -we can change an element of a list using the index operator "[]"
# NOTE: Changed the 5 in the list into a 31

greet = 'Hello peter'
print(len(greet))
x = [1, 6, 'peter', 100]
print(len(x))
# len() tells us the number of elements of any set or sequence
# len() takes a list as a parameter and returns the number of elements in the list


friends = ['Dylan', 'Alyssa', 'Sally']
print(len(friends))
print(range(len(friends)))
# range function returns a list of numbers that range from zero ro one les than the parameter
# can construct an index loop using for and an intger iterator

for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
# these two loops do the same thing

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
# we can create a new list by adding two existing list together (concatenate)
t = [9, 41, 12, 3, 74, 15]
print(t)
print(t[1:3])
print(t[:4])
print(t[2:])
print(t[:])
print(c + t)
# Lists can be sliced using ":"
# Just like in strings, the second number is "up to but not including"
# [0, 1, 2, 3, 4, 5]

x = list()
type(x)
dir(x)
# ['append' , 'count', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# append() - Adds an element at the end of the list
# count() - Returns the number of elements with the specified value
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop() - Removes the element at the specified position
# remove() - Removes the item with the specified value
# reverse() - Reverses the order of the list
# sort() - Sorts the List

stuff = list()
stuff.append('book')
stuff.append(100)
print(stuff)
# Building a list from scratch

some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(10 not in some)
# Is something in a List?
# These are suppose to be logical operators that return True or False

friends.sort()
print(friends)
print(friends[2])
# [0, 1, 2]
# Changed the order of the Sort

nums = [3, 41, 12, 9, 74, 15]

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
# Built-in Functions and Lists

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
value = float(inp)
total = total + value
count = count + 1
average = total / count
print('Average:', average)
# Bulit-in Functions and Lists (alternate)

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

print(stuff)
for w in stuff:
    print(w)
# split breaks into parts and produces a list of strings. Access a particular word or loop
# Strings and Lists

line = 'A lot'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
# If you don't specify a delimiter, multiple spaces are treated like one delimiter
thing = line.split(';')
print(thing)
['first', 'second', 'third']
print(len(thing))
# You can specify what delimiter character to use in the splittng

"From stephan.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
words = line.split()
email = words[1]
'stephen.marquard@uct.ac.za'
pieces = email.split('@')
['stephen.marquard', 'uct.ac.za']
# The Double Split Pattern
