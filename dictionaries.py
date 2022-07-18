purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
# Added "2" to 'candy' in the purse
print(purse)
# List - linear collection of values that stay in order
# Dictionary - A "bag" of values. Each with its own label (key value pairs)
# index the things in dictionary with a "lookup tag"

lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)
# {List} vs. {dictionary}

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)
# {key:value}
ooo = {}
print(ooo)
# empty Dictionary

ccc = dict()
ccc['csev'] = 1
ccc['chan'] = 1
print(ccc)
ccc['chan'] = ccc['chan'] + 1
# added 1 to 'chan'
print(ccc)
# Counting how often we see something or adding value to a key
print('csev' in ccc)
# Use the "in" operator to see if a key is in the Dictionary

counts = dict()
names = ['csev', 'chan', 'csev', 'zqian', 'ella']
for name in names:
    if 'csev' not in counts:

        counts['csev'] = 1
else:
    counts['csev'] = counts['csev'] + 1
    print(counts['csev'])
    print(counts)

# (Histogram) Added a new entry in the dict() and if the the second or later time we have seen the name
# We added one to the count in the dictionary under that name
if name in counts:

    x = counts['csev']
else:

    x = 0
x = counts.get(name, 0)
print(counts.get(name, 0))
print(counts)

# use get() to see if a key is already in dictionary, get default value if the key is not there

counts = dict()
names = ['csev', 'chan', 'csev', 'zqian', 'ella']
for name in names:

    counts[name] = counts.get(name, 0) + 1
print(counts)
# Used get() and provided a default value of zero when the key is not in the key is not yet
# in the dictionary - and then just add one (Simplified counting with 'get()')

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('counting')
for word in words:
    counts[word] = counts.get(word, 0) + 1
    print('Counts', counts)
# Split the lines into words, then loop through the words and use a dictionary
# to track the count of each word independently, then builds a Histogram
# (Counting Pattern)

counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
# for loop goes through all the keys in the dictionary and looks up the values
# run one at a time through SHELL

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())
# Retrieving list of Keys and values
# You can get a list of keys, values, or items(both) from a dictionary

for aaa, bbb in jjj.items():

    print(aaa, bbb)
# Looped through the key-value pairs ina dictionary using "two" iteration variables

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[words] = counts.get[word, 0] + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = counts
print(bigword, bigcount)
# Code for finding the biggest word in text(gives you word, and word count)
