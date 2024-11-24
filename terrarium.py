class Organism:
    allOrganisms = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.size = 1
        self.hunger = 1
        Organism.allOrganisms.append(self)

    def grow(self):
        self.size += 1
        print(f"{self.name} ist ein bisschen gewachsen!")
    def hunger(self):
        self.hunger += 1
    @classmethod
    def showAllNames(cls):
        for org in cls.allOrganisms:
            print(org.name)


#erzeugt Objekt Ratte mit Namen Ratte
ratte = Organism("Ratte")
#Wirft alle Atribute des Organismus Ratte aus.
for atr, values in vars(ratte).items():
    print(f"{atr}: {values}")

#erzeugt ein Objekt mit Namen Baum
baum = Organism("Baum")


def infoObject():
    print("Welcher Organismus interessiert dich?")
    for i, org in enumerate(Organism.allOrganisms, 1):
        print(f"{i} - {org.name}")

    while True:
        try:
            choice = int(input("Wähle eine Nummer: "))
            if 1 <= choice <= len(Organism.allOrganisms):
                return Organism.allOrganisms[choice - 1]
            else:
                print("Ungültige Auswahl. Bitte wähle eine gültige Nummer.")
        except ValueError:
            print("Bitte gib eine Zahl ein.")


infoObject()
