# class Car:
#     numWheels = 4
#     def setColor(self, newColor):
#         self.color = newColor
#     def honkHorn(self):
#         print("Beep beep")
    
# chevy = Car()
# print(chevy.numWheels)

# class Vehicle:
#     numOfWheels = 4
#     def __init__(self):
#         pass

# class Truck(Vehicle):
#     def __init__(self):
#         pass

# chevy = Truck()
# print(chevy.numOfWheels)


# class Car:
#     def setColor(self, newColor):
#         self.color = newColor
#     def honkHorn(self):
#         print("Beep beep")

# chevy = Car()
# ford = Car()
# if chevy == ford:
#     print("TRUE")
# else:
#     print("FALSE")

# class Atom:
#     def __init__(self, atno, x, y, z):
#         self.atno = atno
#         self.__position = (x, y, z) #__position is private
#     def getPosition(self):
#         return self.__position
#     def setPosition(self, x, y, z):
#         self.__position = (x, y, z)
#     def translate(self, x, y, z):
#         x0, y0, z0 = self.__position
#         self.__position = (x0 + x, y0 + y, z0 + z)

# atom = Atom(14, 1, 1, 2)
# atom.translate(2, 3, 8)


class Molecule:
    def __init__(self, name = 'Generic'):
        self.name = name
        self.atomlist = []
    def addAtom(self, atom):
        self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule named %s\n' %self.name
        str = str + 'It has %d atoms\n' %len(self.atomlist)
        for atom in self.atomlist:
            str = str + 'atom' + '\n'
        return str
