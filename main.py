from random import choice
import os
from slova import hadana_slova
from grafika import obesenec


def main():
    
    zivoty = 7
    hra_bezi = True
    hra(hra_bezi, zivoty)
    pass


def hra(hra_bezi, zivoty):

    hadane_slovo = choice(hadana_slova)
    tajenka = vytvor_tajenku(hadane_slovo, "_")
    
    while hra_bezi and zivoty > 0:
        zobraz_stav_hry(tajenka, obesenec, zivoty)
        pokus = ziskej_pokus()
        if pokus == hadane_slovo:
            hra_bezi = False
        elif pokus in hadane_slovo and len(pokus) == 1:
            indexy = je_pismeno_ve_slove(hadane_slovo, pokus)
            if indexy:
               tajenka =  prepis_pismeno(indexy, tajenka, pokus)
            hra_bezi = uhadnuti_tajenky(tajenka)
        else:
            print(f"Toto písmeno není v tajence. Škoda...Zkus to znova, máš ještě {zivoty} životů")
            zivoty -= 1
    konec_hry(hra_bezi, hadane_slovo) 




def zobraz_stav_hry(tajenka, obesenec, zivoty):
    os.system("cls")
    print(f"Tajenka: {''.join(tajenka)}")
    print(obesenec[7 - zivoty])
    print(f"Zbývající počet životů: {zivoty}")


def vytvor_tajenku(slovo, znak):
    return [znak] * len(slovo)


def ziskej_pokus():
    return input("Hádej písmeno nebo celé slovo: ")



def je_pismeno_ve_slove(hadane_slovo, pokus):
    return [index for index, symbol in enumerate(hadane_slovo) if pokus in symbol]


def prepis_pismeno(indexy, tajenka, pokus):
    for index in indexy:
        tajenka[index] = pokus
        return tajenka


def uhadnuti_tajenky(tajenka):
    return False if "_" not in tajenka else True


def konec_hry(hra_bezi, hadane_slovo):      
    if hra_bezi == False:
        print("Vyhrál jsi! Gratuluji!")
    else:
        print(f"Prohrál jsi! Slovo bylo {hadane_slovo}")

main()