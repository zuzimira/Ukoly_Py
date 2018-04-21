#Definice jednotlivych funkci

def hraci_pole(radky, sloupce):
    """vytvori hraci pole"""
    seznam_radku = []
    for i in range(radky):
        radek = []                          
        for j in range(sloupce):
            radek.append(".")
        seznam_radku.append(radek)
    return seznam_radku


def pohyb(seznam_tahu, seznam_ovoce, tah,radky, sloupce):
    """Prida k seznamu tahu bod dle posunu (a odebere posledni), ktery zadal hrac
       pokud tah neni realny, oznami to.
       Pokud je na policku ovoce, vola se funkce snez.
       Pokud had sni ovovce, neodebira se posledni bod."""

    x= seznam_tahu [len(seznam_tahu)-1][0]                      # [x,y]   souradnice noveho tahu
    y= seznam_tahu [len(seznam_tahu)-1][1]

    if tah == "s":                           #sever
        y -= 1
    elif tah == "j":                         #jih
        y += 1
    elif tah == "v":                         #vychod
        x += 1
    elif tah == "z":                         #zapad
        x -= 1
    else:
        print("Zadal jsi spatne pismeno." )
        return()

    if x<0 or x>sloupce-1 or y<0 or y>radky-1:                      #tah mimo pole
        print("Tah neni mozny, je mimo hraci pole. Opakuj tah.")
    elif [x,y] in seznam_tahu:                                      #jiz obsazene policko hadem
        print("Tah neni mozny, had uz na nem je. Opakuj tah.")
    elif [x,y] in seznam_ovoce:                                     #policko s ovocem, vola se funkce snez
        snez (seznam_ovoce, seznam_tahu,[x,y],radky, sloupce)
    else:
        seznam_tahu.append([x,y])                                   #tah na volne policko, prida se tah a odebere posledni bod
        seznam_tahu.pop(0)



def snez (seznam_ovoce, seznam_tahu, souradnice, radky, sloupce):
    """Had sni ovoce, pokud je seznam ovoce prazdny,
       vola se funkce na vytvoreni ovoce"""

    seznam_tahu.append(souradnice)                      #snezeni
    seznam_ovoce.pop(seznam_ovoce.index(souradnice))    #vymazani ze seznamu ovoce
    if (len(seznam_tahu)) == radky * sloupce:           #v poli jiz neni ani jedno volne policko, konec
        return()
    if seznam_ovoce == []:
        vytvor_ovoce(seznam_ovoce, seznam_tahu,radky, sloupce)      #volam funkci, ktera vytvori dalsi ovoce

def vytvor_ovoce (seznam_ovoce, seznam_tahu,radky, sloupce):
    """Vytvori novy kusu ovoce na nahodne pozici"""
    while True:
        nove_ovoce = [randrange(sloupce),randrange(radky)]
        if nove_ovoce in seznam_tahu or nove_ovoce in seznam_ovoce:
            continue
        else:
            break
    seznam_ovoce.append(nove_ovoce)

def vloz (pole, pozice, znak):
    """Vlozi na urcene pozice v zadanem poli znak pro hada nebo ovoce """
    for k in pozice:
       pole [k[1]] [k[0]]= znak

def vytvor_hru (seznam_tahu, seznam_ovoce, radky, sloupce):
    """Vrati hraci pole - hriste s pozicemi hada a ovoce"""
    hriste = hraci_pole(radky, sloupce)
    vloz(hriste,seznam_ovoce, "O")
    vloz(hriste, seznam_tahu, "X")
    return(hriste)

def tiskni_hru (hriste):
    """Vytiskne hru po tahu a vsech akcich"""
    for radek in hriste:
       for cislo in radek:
           print(cislo, end=' ')
       print()

#  HLAVNI PROGRAM
#uvodni informace
print("Pohybuj se ve smeru sever, jih, vychod, zapad pismenky s, j, v, z.")
print("Pokud chces hru ukoncit, nebo nemas moznost dalsiho tahu, zadej 0.")

#Zadani velikosti hraciho pole
hriste_radky =  int(input ("Zadej pocet radku hadiho hriste (minimalne dva): "))
hriste_sloupce =  int(input ("Zadej pocet sloupcu hadiho hriste (minimalne pet): "))

# Definice + import
from random import randrange
jedu = True
hra = []
tajemne_ovoce = 30                  #po 30-ti tazich se objevi dalsi kus ovoce
pocet_tahu=0
had = [[0,0],[1,0],[2,0]]                                                 # pocatecni pozice hada
ovoce = [[randrange(3,hriste_sloupce),randrange(hriste_radky)]]           #umisteni prvniho kusu ovoce

#Vytisteni pocatecniho stavu hry
hra = vytvor_hru (had, ovoce,hriste_radky, hriste_sloupce)
tiskni_hru(hra)


#Cyklus hry
while jedu:
    pocet_tahu += 1                 #pocitani tahu pro tajemne ovoce
    tah = input ("Zadej tah: ")
    print()
    if tah == "0":                  #ukonceni hry
        jedu = False
    else:
        pohyb(had, ovoce, tah,hriste_radky, hriste_sloupce)         #volam funkci pohyb

    if pocet_tahu == tajemne_ovoce:                                 # Vytvoreni noveho ovoce kazdych 30 tahu
        vytvor_ovoce (ovoce, had,hriste_radky, hriste_sloupce)
        pocet_tahu = 0
    hra = vytvor_hru (had, ovoce,hriste_radky, hriste_sloupce)      #vyutvoreni a vytisteni hriste
    tiskni_hru(hra)
    if len(had)== hriste_radky*hriste_sloupce:                      # Premie za vyplneni celeho pole hry
        print("Vyplnil jsi cele pole. Gratuluji!!!")
        break
    print()
 #Tisk ziskaneho poctu bodu
print("Tvuj pocet bodu je: ", len(had)-3,".")                       #vytisteni poctu bodu
