# V tomto modulu mam tri funkce, zakladni je tah hrace,
# ktera v urcitych pripadech vola nahodny tah nebo
# tah, ktery se pokousi utocit.

from random import randrange, choice

def nahodny_tah(kolo, symbol):      #vytvoren test
    """Vrati nahodny tah od tretiho do 18-teho policka, pokud to jde,
        na kraje neni takticke hrat"""
    if "-" in kolo[3:len(kolo)-3]:
    #if "-" in kolo[3:18]:
        tah = randrange(3,len(kolo)-3)
        while kolo[tah]!= "-":                   #Ve vetsine pripadu neni takticke hrat na kraje,
            tah = randrange(3,len(kolo)-3)
    else:                                       #Jen, pokud je to nutne.
        tah = choice([0,1,2, len(kolo)-3, len(kolo)-2, len(kolo)-1])
        while kolo[tah] != "-":
            tah = choice([0,1,2, len(kolo)-3, len(kolo)-2, len(kolo)-1])
    return tah



def utocim(kolo, symbol):               #vytvoren test
    """Pokus o utok, nemusi -li pocitac zrovna branit,
    pokud nema moznost utoku, hraje nahodny tah."""

    if "o---o" in kolo:                           # kombinace o-o-o je jasne,ze pocitac vyhraje,
        pozice_pocitac = kolo.index("o---o") + 2          # proto se ji snazi vybudovat
    elif "-o-" in kolo:
        pozice_pocitac = choice([kolo.index("-o-") + 2, kolo.index("-o-")]) #doleva nebo doprava
    elif "----o" in kolo:
        pozice_pocitac = kolo.index("----o")
    elif "o----" in kolo:
        pozice_pocitac = kolo.index("o----") + 4
    elif "o--" in kolo:
        pozice_pocitac = kolo.index("o--") + 2             #pokud nemuze, pokusi se o jednodussi vypad
    elif "--o" in kolo:
        pozice_pocitac = kolo.index("--o")
    elif "-----" in kolo:
            pozice_pocitac = kolo.index("-----") + 2
    else:                                           #pokud nemuze utocit, voli nahodny tah
        return nahodny_tah(kolo, symbol)

    return pozice_pocitac


def tah_pocitace (kolo,  symbol):           #vytvoren test
    """Vrati herni pole s tahem pocitace.
    Strategie pocitace -  hraje na remizu, v pripade chyby hrace utoci na vyhru (doufam :).
    """

     # Nasleduje poradi tahu dle priority.
     # V posloupnosti tahu jsou jeste chyby, nekdy by mohl hrat lepe.
     # Ale je tezke ty chyby vychytat, nejake jsem odstranila,
     # ale musim doma taky obcas neco uvarit a tak, takze moje taktika zustane nedodelana.

     # pozice_pocitac je misto v retezci, ktere se bude menit.
     # pricitane cislo mi rika, kam se vlozi pocitacuv symbol do podretezce


    while "-" in kolo:
                                                        # pokud jsou 2 o V POZICI NA VYHRU
                                                        # a pocitac je na rade, vyhraje
        if "o-o" in kolo:
            pozice_pocitac = kolo.index("o-o") + 1       #+1 doprostred
        elif "oo-" in kolo:
            pozice_pocitac = kolo.index("oo-") +2        #+2 pravy kraj
        elif "-oo" in kolo:
            pozice_pocitac = kolo.index("-oo")           # levy kraj

        elif "x-x" in kolo:                                  #pokud jsou dve x v pozici na vyhru
            pozice_pocitac = kolo.index("x-x") +1                    #pocitac tomu zabrani
        elif "xx-" in kolo:
            pozice_pocitac = kolo.index("xx-") +2
        elif "-xx" in kolo:
            pozice_pocitac = kolo.index("-xx" )
        elif "x---x-"in kolo:
            pozice_pocitac = kolo.index("x---x") +3
        elif "-x---x" in kolo:
            pozice_pocitac = kolo.index("x---x") +2
        elif "x---x" in kolo:
            pozice_pocitac = kolo.index("x---x") +2
                             #pokud by hrac dal krizek doprostred, vyhraje
                                                                     #pocitac tomu zabrani

        elif "-x-" in kolo:                                         #pokud je ve hrekombinace -x-
            pozice_pocitac = kolo.index("-x-" )                      #muze byt mene, vice nebo vubec nebezpecna
            if "o-x-o" in kolo:                                     #tento blok neni doreseny, nekdy to skripe
                pozice_pocitac=  utocim(kolo,symbol)                 #pokud to je mozne, pocitac utoci
            elif "o--x-" in kolo:
                pozice_pocitac = pozice_pocitac       #pred x
            elif "-x--o" in kolo:
                pozice_pocitac = pozice_pocitac + 2   #za x
            elif "-x-o" in kolo:
                if pozice_pocitac == 0:
                    pozice_pocitac=  utocim(kolo,symbol)
                else:
                    pozice_pocitac = pozice_pocitac
            elif "o-x-" in kolo:
                if pozice_pocitac == 17:
                    pozice_pocitac=   utocim(kolo,symbol)
                else:
                    pozice_pocitac += 2
            elif pozice_pocitac == 0:                                #kraje
                pozice_pocitac += 2
            elif pozice_pocitac == 17:
                pozice_pocitac = pozice_pocitac
            else:
                pozice_pocitac = choice([(pozice_pocitac+2), pozice_pocitac])  #je jedno, zda tahne zprava nebo zleva

        else:
            pozice_pocitac = utocim(kolo,symbol)                             #pokud si pocitac nic nevybral, pokusi se utocit


        return kolo[:pozice_pocitac] + symbol + kolo[pozice_pocitac+1:]
    # Tyto posledni 4 radky jsem pripojila cvicne jako ukol 5, i kdyz to mam (doufam) vyreseno ve funkci piskvorky1d()
    # v prubehu hry by na ne nemelo dojit
    if len(kolo) == 0:
        raise ValueError('Hraci pole nebylo vytvoreno.')
    if "-" not in kolo:
        raise ValueError('Hraci pole je plne, hra zkoncila.')
