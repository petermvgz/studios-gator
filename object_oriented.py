# A program is made up of many cooperating objects

# Instead of being the "whole program" - each object is a little "island"
# within the program and cooperatively working with other objects.

# A program is made up of one or more objects working together -
# objects make use of each ther's capabilities

# An "Object" is a bit of self contained Code and Data

# A key aspect of the Object approach is to break the problem
# into smaller understandable parts (divide and conquer)

# Objects have boundaries that allow us to ignore un-needed detail

# Definitions
# Input > (Object<>String<>Dictionary<>Object) > Output
# (Objects hide details) - they allow us to ignore the detail of the program

# {Class} - What code will each object have in it (shape/template)
# {Method or Message} - Fuction that lives inside of class (code)
# {Field or attribute} - Data items inside of class (varibles)
# {Object or Instance} - Particular instance of a class (result/actual object)

class PartyAnimal:
    # Template - Party Animals
    x = 0
# Each PartyAnimal object has a bit of data (Method)

    def party(self):

        self.x = self.x + 1
        print("So far", self.x)


# Each PartyAnimal object has a bit of code
an = PartyAnimal()
# Construct a PartyAnimalobject and store in "an"
