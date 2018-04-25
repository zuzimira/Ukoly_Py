
#ukoly z lekce 6, 9.-14.
#snad nevadi vse v jednom

def tabulka(pocet_sloupcu, symbol):                 #ukol 9
    """Vykresli zadanou tabulku"""
    for i in range(pocet_sloupcu):
        tiskni_radek(symbol, pocet_sloupcu)

def tabulka_trojuhelnik(pocet_sloupcu, symbol):     #ukol 11
    """Vykresli trojuhelnikovou tabulku"""
    for i in range(pocet_radku):
        tiskni_radek("X", i+1)

def obrys_tabulky(pocet_sloupcu, symbol):           #ukol 13
    """Vypise obrys tabulky"""
    for i in range(pocet_radku):
        tiskni_znak(pocet_sloupcu, i)

def nasobilka(pocet_sloupcu):                       #ukol 10
    """Vykresli tabulku s nasobky"""
    for i in range(pocet_sloupcu):
        tiskni_nasobek(pocet_sloupcu, i)

# funkce pouzivane ve funkcich vyse
def tiskni_radek(symbol, pocet_sloupcu):
    """Vytiskne radek c danym symbolem"""
    for j in range(pocet_sloupcu):
        print(symbol,' ', end='')
    print()

def tiskni_nasobek(pocet_sloupcu, i):           # i je cislo i-teho radku
    """Vytiskne nasobky"""
    for j in range(pocet_sloupcu):
        print(i*j,' ', end='')
    print()

def tiskni_znak(pocet_sloupcu, i):
    """Vytiskne znak dle polohy v tabulce"""
    for j in range(pocet_radku):
        if i*j==0 or i==pocet_radku-1 or j==pocet_radku-1:  #krajni polohy, tisk symbolu
            print("X", " ",sep='', end="")
        else:
            print("  ",end="")                              #jinak tisk mezery
    print()

#hlavni program

while True:                                                 #ukol 14
    pocet_radku = input("Zadej pocet radku tabulky: ")      #zadani poctu radku tabulky
    if not pocet_radku.isdigit():                           #stejne by sel zadat i pocet sloupcu pro obdelnikovou tabulku
        print('Nezadal jsi cislo, zkus to znova!')
        continue
    else:
        pocet_radku = int(pocet_radku)
        break

tabulka(pocet_radku, 'X')                               #ukol 9
print()
nasobilka(pocet_radku)                                  #ukol 10
print()
tabulka_trojuhelnik(pocet_radku, 'X')                   #ukol 11
print()
obrys_tabulky(pocet_radku, 'X')                         #ukol 13

#Rekne, zda je radek prvni
for i in range(pocet_radku):                            #ukol 12
    print("prvni radek ") if i == 0 else print("neni prvni ")
print()
