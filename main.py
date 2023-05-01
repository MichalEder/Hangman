from random import choice
import os
from slova import hadana_slova
from grafika import obesenec


# TODO promenne¨
print("-----------------------")
print("VÍTEJ VE HŘE OBĚŠENEC!!")
print("-----------------------")


zivoty = 7
hadane_slovo = choice(hadana_slova)
tajenka = ["_"]*len(hadane_slovo)
hra_bezi = True



while hra_bezi and zivoty > 0:
    
    print(f"Tajenka: {''.join(tajenka)}")
    print(obesenec[7 - zivoty])
    print(f"Zbývající počet životů: {zivoty}")
    
    pokus = input("Hádej písmeno nebo celé slovo: ")
    os.system("cls")
    if pokus == hadane_slovo:
        hra_bezi = False
        
    elif pokus in hadane_slovo and len(pokus) == 1:
        for index, symbol in enumerate(hadane_slovo): 
            if symbol == pokus:
                tajenka[index] = pokus
                print("Uhadl jsi pismeno!! Jen tak dál!")
        if "_" not in tajenka:
            hra_bezi = False    
    else:
        print(f"Toto písmeno není v tajence. Škoda...Zkus to znova, máš ještě {zivoty} životů")
        zivoty -= 1
else: 
    if hra_bezi == False:
        print("Vyhrál jsi! Gratuluji!")
    else:
        print(f"Prohrál jsi! Slovo bylo {hadane_slovo} ")
