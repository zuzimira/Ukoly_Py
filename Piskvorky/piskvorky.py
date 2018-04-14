#Pokusila jsem se vytvorit taktiku hry pro pocitac, ale
#jeste to neni idealni.
#Na to hraci pole by asi bylo lepsi neco, co se da jednoduse menit.
#Taky si nejsem jista, zda jsem zvolila dobrou taktiku pro stavbu programu
#Jestli by treba nebylo lepsi pocitat mezery kolem tahu hrace a urcit prvni symbol a
#podle to ho volit tah pocitace.

#Varuji predem, z to je to dlouhe a asi i neprehledne.

from random import randrange, choice
import textwrap


def vyhodnot(kolo):
    """Vrati jednoznakovy retezec dle stavu hry"""
    if "xxx" in kolo:           #vyhral pocitac
        a="x"
    elif "ooo" in kolo:         #vyhral hrac
        a = "o"
    elif "-" in kolo:           #hra jeste neskoncila
        a = "-"
    else:                       #hra skoncila remizou
        a = "!"
    return(a)

def tah_hrace (kolo, symbol):
    "Vrati herni pole s danym symbolem na danou pozici"

    jedu=True
    if "-" in kolo:
        while jedu:
            poziceHrac = int(input("Zadej pozici na kterou chces vlozit symbol, ja nasledne vlozim svuj symbol: "))
            print()
            if poziceHrac >20 or poziceHrac < 1:
                print("Zadal jsi spatnou pozici policka.")
            elif kolo[poziceHrac-1] != "-":
                print("Toto policko je jiz obsazene.")
            else:
                kolo = kolo[:poziceHrac-1] + symbol + kolo[poziceHrac:]
                jedu=False

    return (kolo)

def nahodny_tah(kolo, symbol):
    """Vrati nahodny tah od tretiho do 18-teho policka
        na kraje neni takticke hrat"""
    tah = randrange(3,17)                   #Ve vetsine pripadu neni takticke hrat na kraje,
    while kolo[tah -1] != "-":              #proto jsem vyber omezila
        tah = randrange(3,17)
    else:                               #Musi byt else? myslim, ze ne
        print("nahodny")
        return tah-1

def utocim(kolo, symbol):
    """Pokus o utok, nemusi -li pocitac zrovna branit,
    pokud nema moznost utoku, hraje nahodny tah."""

    if "o---o" in kolo:                           # kombinace o-o-o je jasne,ze pocitac vyhraje,
        pozicePocitac = kolo.index("o---o") + 2          # proto se ji snazi vybudovat
    elif "----o" in kolo:
        pozicePocitac = kolo.index("----o")
    elif "o----" in kolo:
        pozicePocitac = kolo.index("o----") + 4
    elif "o--" in kolo:
        pozicePocitac = kolo.index("o--") + 2             #pokud nemuze, pokusi se o jednodussi vypad
    elif "--o" in kolo:
        pozicePocitac = kolo.index("--o")
    elif "-----" in kolo:
            pozicePocitac = kolo.index("-----")
    else:                                           #pokud nemuze utocit, voli nahodny tah
        return nahodny_tah(kolo, symbol)

    return pozicePocitac


def tah_pocitace (kolo,  symbol):
    """Vrati herni pole s tahem pocitace.
    Strategie pocitace -  hraje na remizu, v pripade chyby hrace utoci na vyhru (doufam :).
    """

     # Nasleduje poradi tahu dle priority.
     # V posloupnosti tahu jsou jeste chyby, nekdy by mohl hrat lepe.
     # pozicePocitac je misto v retezci, ktere se bude menit.
     # pricitane cislo rika, kam se vlozi pocitacuv symbol do podretezce


    while "-" in kolo:
                                                        # pokud jsou 2 o V POZICI NA VYHRU
                                                        # a pocitac je na rade, vyhraje
        if "o-o" in kolo:
            pozicePocitac = kolo.index("o-o") + 1       #+1 doprostred
        elif "oo-" in kolo:
            pozicePocitac = kolo.index("oo-") +2        #+2 pravy kraj
        elif "-oo" in kolo:
            pozicePocitac = kolo.index("-oo")           # levy kraj

        elif "x-x" in kolo:                                  #pokud jsou dve x v pozici na vyhru
            pozicePocitac = kolo.index("x-x") +1                    #pocitac tomu zabrani
        elif "xx-" in kolo:
            pozicePocitac = kolo.index("xx-") +2
        elif "-xx" in kolo:
            pozicePocitac = kolo.index("-xx" )
        elif "x---x" in kolo:
            pozicePocitac = kolo.index("x---x") +2                  #pokud by hrac dal krizek doprostred, vyhraje
                                                                     #pocitac tomu zabrani

        elif "-x-" in kolo:                                         #pokud je ve hrekombinace -x-
            pozicePocitac = kolo.index("-x-" )                      #muze byt mene, vice nebo vubec nebezpecna
            if "o-x-o" in kolo:                                     #tento blok neni doreseny, nekdy to skripe
                pozicePocitac=  utocim(kolo,symbol)                 #pokud to je mozne, pocitac utoci
            elif "o--x-" in kolo:
                pozicePocitac = pozicePocitac       #pred x
            elif "-x--o" in kolo:
                pozicePocitac = pozicePocitac + 2   #za x
            elif "-x-o" in kolo:
                if pozicePocitac == 0:
                    pozicePocitac=  utocim(kolo,symbol)
                else:
                    pozicePocitac = pozicePocitac
            elif "o-x-" in kolo:
                if pozicePocitac == 17:
                    pozicePocitac=   utocim(kolo,symbol)
                else:
                    pozicePocitac += 2
            elif pozicePocitac == 0:                                #kraje
                pozicePocitac += 2
            elif pozicePocitac == 17:
                pozicePocitac = pozicePocitac
            else:
                pozicePocitac = choice([(pozicePocitac+2), pozicePocitac])  #je jedno, zda tahne zprava nebo zleva

        else:
            pozicePocitac = utocim(kolo,symbol)                             #pokud si pocitac nic nevybral, pokusi se utocit

        p=kolo[:pozicePocitac] + symbol + kolo[pozicePocitac+1:]
        return p


def piskvorky1d():
    "Vrati viteze hry"
    print(textwrap.dedent('''
    Hrajeme piskvorky, mas x. Zacni!
    Nez zacnes, zvetsi si velikost pisma v cernem okne.'''))

    pole = 20 * "-"                         #tady by sla menit velikost pole
    print()
    print (pole)

    symbolHrac = "x"                        #a tady vyber symbolu
    symbolPocitac = "o"

    while vyhodnot(pole) == "-":            #pokud nikdo nevyhral a jsou volna policka,
                                            #stridave se vola hrac a pocitac k tahu
        pole = tah_hrace(pole, symbolHrac)
        if vyhodnot(pole) == symbolHrac:
            print("Vyhral jsi")
            print(pole)
            return
        print()
        pole=tah_pocitace(pole,symbolPocitac)
        print(pole)

    if vyhodnot(pole) == symbolPocitac:
            print("Vyhral jsem")
    else:
        print("Remiza!")



# hlavni program

piskvorky1d()
