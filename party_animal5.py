class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


s = PartyAnimal('Sally')
j = PartyAnimal('Jim')
# Two independent instances
s.party()
j.party()
s.party()
# Constructuctors can have additional parameters. These can be used to set up
# instance varibles for the particular instance of the class.
