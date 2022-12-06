from random import randint
from vikingClasses import *

def fight(viking, saxon):
    number_of_vikings = int(input("How many viking do you want to fight? "))
    number_of_saxons = int(input("How many saxons do you want to fight? "))
    vikings = []
    saxons = []

    for i in range(number_of_vikings):
        vikings.append(viking)
    for i in range(number_of_saxons):
        saxons.append(saxon)
    while len(vikings) > 0 and len(saxons) > 0:
        viking = vikings[randint(0, len(vikings)-1)]
        saxon = saxons[randint(0, len(saxons)-1)]
        saxon.receiveDamage(viking.attack())
        if saxon.health <=0:
            saxons.remove(saxon)
        else:
            viking.receiveDamage(saxon.attack())
            if viking.health <= 0:
                vikings.remove(viking)
    
    if len(vikings) > 0:
        print("Vikings win")
    else:
        print("Saxons win")

if __name__ == "__main__":
    viking = Viking("Harald", 100, 10)
    saxon = Saxon(200, 10)
    fight(viking, saxon)