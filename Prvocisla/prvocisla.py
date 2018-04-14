#Chtela jsem vymyslet neco jineho nez delit vsemi cisly.
#Doslo mi, ze cyklus nemusim projizdet cely.
#Kdyz delim tremi, staci dojet do tretiny hodnoty zadaneho cisla.
#Kdyz delit peti, do petiny, sedmi do sedminy atd.
#Z toho jsem sestavila podminku v poslednim else

#Na zacetku vyloucim sude cislo (prijde mi zbytecne delit v cyklu sudymi cisly)
#a zvlast osetrim 1, 2 a 3.

cislo = int(input("Zadej cislo: "))
print()
if cislo in [2, 3] :              #vymysleny postup nefunguje (kvuli mezim v cyklu) pro prvocisla mensi nez 5,
    print("Je prvocislo.")                          #proto jsem je take vyclenila, prijde mi to lepsi, nez udelat zbytek slozitejsi

elif cislo == 1 or cislo % 2 == 0:                     #  vyloucim suda cisla a 1
    print("Neni prvocislo.")

else:
    for i in range(3, cislo, 2):            #projidim pouze licha cisla
        if cislo % i == 0:                   #pokud je nulovy zbytek, neni prvocislo
            print("Neni prvocislo.")
            break
        else:
            if i > cislo/i:                  #pokud toto plati, dalsi delitel neni mozny
                print("Je prvocislo")
                break

print()
#Vygeneruje vsechny prvocisla do zadaneho cisla a rekne, zda cislo je prvocislo

zadane_cislo = int(input("Zadej cislo: "))
print()
seznam_prvocisel = [2,3]
for cislo in range (5,cislo+1,2):

    for delitel in range(3, cislo+1, 2):
        if cislo % delitel == 0:
            break
        else:
            if delitel > cislo/delitel:
                seznam_prvocisel.append(cislo)
                break

print(seznam_prvocisel)


vypis = 'Zadane cislo {} {} prvocislo.'
print(vypis.format(zadane_cislo, 'je')) if (zadane_cislo in seznam_prvocisel) else print(vypis.format(zadane_cislo, 'neni'))
