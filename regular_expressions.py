# ^ Matches the beginning of a line
# $ Matches the end of the line
# . Matches any character
# \s Matches whitespace
# \S Matches any non-whitespace character
# * Repeats a character zero or more
# *? Repeats a character zero or more (non-greedy)
# + Repeats a character one or more times
# +? Repeats a charcter one or more times (non-greedy)
# [aeiou] Matches a single charcter in the listed set
# [^XYZ] Matches a single charcetr set in the listed set
# [a-z0-9] The set of charcters can include a range
# ( where string extraction is to start
# ) where string extraction is to end

# "import re"- before you can use regular expression,
# you must import the library using "import re"

# Use "re.search()"" to see if a string matches a regular expression
# Like using the find() method for strings

# Use "re.findall()"" to extract portions of a string
# that match your regular expression

# "re.search()" returns a T/F depending on whether the string Matches
# "re.findall()" if you want the matching strings extracted
# "[0-9]+"- One or more digits

# "stephen.marquard@uct"
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
# Matching and Extracting Data

y = re.findall('\S+@\S+', x)
print(y)
# \S+@\S+ = At least one non- whitespace character
# Found the @ sign and split the letters around it
# Fine- Tuning String extraction

# String Parsing Examples

# Extracting the host name using find and string slicing (marquard)
data = 'stephen.marquard@uct'
atpos = data.find('.')
print(atpos)
sppos = data.find('@', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

# Double Split Pattern (looking for the letter "J  ")
line = 'From peterdeyi@gmail.com Sat Jan 3:01:23 2022'
words = 'From peterdeyi@gmail.com Sat Jan 3:01:23 2022'
words = line.split()
email = words[3]
email.split('a')
print(email[0])
# Split a line one way, and then grabbed one of the pieces of the line
# and split that piece again

# Escape Character - If you want a special regular expression charcter
# to just behave normally you prefix it with "\"
