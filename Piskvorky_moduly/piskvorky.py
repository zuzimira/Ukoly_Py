
import textwrap
from ai import tah_pocitace


def vyhodnot(kolo): #vytvoren test
    """Vrati jednoznakovy retezec dle stavu hry"""
    if "xxx" in kolo:           #vyhral hrac
        a="x"
    elif "ooo" in kolo:         #vyhral tah_pocitace
        a = "o"
    elif "-" in kolo:           #hra jeste neskoncila
        a = "-"
    else:                       #hra skoncila remizou
        a = "!"
    return(a)

def tah_hrace (kolo, symbol):  #osetren vstup od hrace, vyvolani a vychytani vyjimek
    "Vrati herni pole s danym symbolem na danou pozici"
    if "-" in kolo:
        while True:
            try:
                pozice_hrac =int(input("Zadej pozici na kterou chces vlozit symbol, ja nasledne vlozim svuj symbol: "))
                if pozice_hrac >20 or pozice_hrac < 1:
                    raise IndexError('Policko {} není v poli! Policka maji cisla 1 az 20.'.format(pozice_hrac))
                elif kolo[pozice_hrac-1] != "-":
                    print('Policko {} je jiz obsazeno! '.format(pozice_hrac))
                else:
                    return kolo[:pozice_hrac-1] + symbol + kolo[pozice_hrac:]

            except ValueError:
                print('Nezadal jsi cislo, zkus to znova!')
            except IndexError:
                print('Policko {} není v poli! Policka maji cisla 1 az 20.'.format(pozice_hrac))
            print(kolo)




def piskvorky1d(): # nevim, jak napsat test k teto funkci
    "Vrati viteze hry"
    print(textwrap.dedent('''
    Hrajeme piskvorky, mas x. Zacni!
    Nez zacnes, zvetsi si velikost pisma v cernem okne.'''))

    pole = 20 * "-"                         #tady by sla menit velikost pole
    print()
    print (pole)

    symbol_hrac = "x"                        #a tady vyber symbolu
    symbol_pocitac = "o"

    while vyhodnot(pole) == "-":            #pokud nikdo nevyhral a jsou volna policka,
                                            #stridave se vola hrac a pocitac k tahu
        pole = tah_hrace(pole, symbol_hrac)
        if vyhodnot(pole) == symbol_hrac:
            print(pole)
            return ("Vyhral jsi.")
        print()
        pole=tah_pocitace(pole,symbol_pocitac)
        print(pole)

    if vyhodnot(pole) == symbol_pocitac:
            return ("Vyhral jsem.")
    else:
        return ("Remiza!")
