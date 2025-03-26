class Package:
    def __init__(self, width, height, length, mass):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    def volume(self):
        return self.width * self.height * self.length

    def is_bulky(self):
        return self.volume() >= 1000000 or self.width >= 150 or self.height >= 150 or self.length >= 150

    def is_heavy(self):
        return self.mass >= 20

    def designated_stack(self):
        bulky = self.is_bulky()
        heavy = self.is_heavy()
        return "REJECTED" if bulky and heavy else ("SPECIAL" if bulky or heavy else "STANDARD")


if __name__ == '__main__':
    pkg1 = Package(50, 50, 50, 10)
    print("For a package with dimensions (50, 50, 50) and mass 10kg, the designated stack is:", pkg1.designated_stack())

    pkg2 = Package(100, 100, 150, 10)
    print("For a package with dimensions (100, 100, 150) and mass 10kg, the designated stack is:", pkg2.designated_stack())

    pkg3 = Package(200, 50, 50, 25)
    print("For a package with dimensions (200, 50, 50) and mass 25kg, the designated stack is:", pkg3.designated_stack())

    pkg4 = Package(30, 30, 30, 21)
    print("For a package with dimensions (30, 30, 30) and mass 21kg, the designated stack is:", pkg4.designated_stack())

    pkg5 = Package(100, 100, 110, 15)
    print("For a package with dimensions (100, 100, 110) and mass 15kg, the designated stack is:", pkg5.designated_stack())
