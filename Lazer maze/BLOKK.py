class Blokk:
    def __init__(self, fajta, irany):
        self.fajta = fajta
        self.irany = irany
    def __eq__(self, rhs):
        ''' mivel egyenlőséget csupán átlósan szimmetrikus cellák összehasonlításához van felhasználva, ezért
        egyező fajtájú cellák esetén a cellák elforgatási irányainak paritását kell összehasonlítani.'''
        return self.fajta == rhs.fajta and self.irany%2 == rhs.irany%2
    def __ne__(self, rhs):
        return not self == rhs