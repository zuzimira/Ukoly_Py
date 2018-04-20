#I=1                #Hodnoty jednotlivych cisel
#V=5
#X=10
#L=50
#C=100
#D=500
#M=1000

                    #Povolene odecitani:
#IV = 4
#IX = 9
#XL = 40
#XC = 90
#CD = 400
#CM = 900

#nepovolene kombinace
nepovolene_kombinace = ["IIV", "IIX", "XXL", "XXC", "CCD", "CCM","IXIX","XLXL", "XCXC","CDCD","CMCM","IVIV","VV","LL","DD","IL" , "IC" , "ID" , "IM" , "XD", "XM" , "VX" , "VL" , "VC" , "VD" , "LC", "LD" , "LM" , "DM" ]

rimske_cislice = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabske_cislice = []        #seznam arabskych cislic, jak jdou v cisle za sebou
seznam_chyb = []            #seznam spatnych kombinaci znaku v zadanem cisle


rimske_cislo = input("Zadej rimske cislo:  ")    # Zadani rimskeho cisla
rimske_cislo = rimske_cislo.upper()



def over_vstup(uzivatel_vstup):
    """Overi, zda zadany retezec je rimske cislo ve spravnem formatu
    Pokud neni vraci False a tiskne seznam chyb, pokud ano, vraci True"""

    for i in rimske_cislice:            #kontrola poctu jednotlivych znaku bezprostredne za sebou
        if 4*i in uzivatel_vstup:
            print('Rimske cislo nesmi obsahovat ctyri stejne znaky za sebou.')
            return False


    for i in uzivatel_vstup:            #kontrola jednotlivych znaku
        if i not in rimske_cislice:
            print('Zadany znak {} neni soucasti sady pismen pro rimska cisla.'.format(i))
            return False

    for k in nepovolene_kombinace:      #kontrola nepovolenych kombinaci
        if k in uzivatel_vstup:
            seznam_chyb.append(k)
    if seznam_chyb:                    #Vypis nepovolenych kombinaci a ukonceni programu
        print("Byla zadana nedovolena kombinace znaku, chyba je v techto sekvencich: ")
        print(seznam_chyb)
        return False

    return True                         #Pokud je vse v poradku, vraci True

def preved(uzivatel_vstup):
    """Prevede jednotliva pismena na arabske cislice """

    for i in range (len(uzivatel_vstup)):      #prevod zadaneho retezce na pole cisel

        if rimske_cislo[i] =="I":
            arabske_cislice.append(1)

        elif rimske_cislo[i] =="V":
            arabske_cislice.append(5)

        elif rimske_cislo[i] =="X":
            arabske_cislice.append(10)

        elif rimske_cislo[i] =="L":
            arabske_cislice.append(50)

        elif rimske_cislo[i] =="C":
            arabske_cislice.append(100)

        elif rimske_cislo[i] =="D":
            arabske_cislice.append(500)

        elif rimske_cislo[i] =="M":
            arabske_cislice.append(1000)

    return arabske_cislice



def prepocitej(uzivatel_vstup):
    """Vrati arabske cislo"""
    preved(uzivatel_vstup)
    arabske_cislo = 0

    for i in range (len(uzivatel_vstup)-1):     #pricitani nebo odecitani hodnot do celkoveho souctu, mimo posledni cislici

        if arabske_cislice[i] >= arabske_cislice[i+1]:
            arabske_cislo += arabske_cislice[i]

        elif arabske_cislice[i] < arabske_cislice[i+1]:
            arabske_cislo -= arabske_cislice[i]

    if arabske_cislo > 3999:                    #omezeni velikosti rimskych cisel
        return print ("Rimska cisla jsou pouze do 3999, tvoje cislo je prilis velke.")

    else:
        return ('Zadane cislo {} ma hodnotu {}.'.format(uzivatel_vstup, arabske_cislo + arabske_cislice[len(uzivatel_vstup)-1]))     #posledni cislice se vzdy pricita


#hlavni program                              
if over_vstup(rimske_cislo):            # Pokud je spravny vstup, zacina prepoct
    print(prepocitej(rimske_cislo))     # Tisk vysledneho cisla
