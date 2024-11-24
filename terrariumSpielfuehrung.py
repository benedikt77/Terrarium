import terrarium
from terrarium import Organism
from terrarium import infoObject

print("Wilkommen \nin deinen Terrarium. \nDeine Aufgabe ist es dich um die Tiere und Pflanzen hier gut zu kümmern!")

stop = False
while not stop:
    choise = input('''1 - Zeig mir wer hier lebt.
    2 - Wie geht es einen bestimmten Lebewesen?
    3 - Ich möchte füttern oder gießen oder lüften?
    x - beenden''')

    if choise == '1':
        Organism.showAllNames()
    elif choise == '2':
        infoObject()
    elif choise == 'x':
        stop = True
    else:
        print("Da ging was schief!")
        break
