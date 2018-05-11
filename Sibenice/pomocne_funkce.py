import random

def tiskni_sibenici(cislo_obrazku):
    """Vrati prislusny obrazek sibenice dle poctu neuspesnych pokusu."""
    obrazek = 'obrazky{}.txt'.format(cislo_obrazku)
    with open(obrazek, encoding='utf-8') as soubor:         #podle poctu chyb se otevre prislusny soubor
        obrazek = soubor.read()
        return obrazek




def ukazuji_slovo (pismeno, slovo, retezec):                #doresit ten vstup z n-tice
    """Vrati retezec s uhodnutymi pismeny a slovo bez uhodnutych pismen."""

    while pismeno in slovo:
        pozice = slovo.index(pismeno)
        retezec = retezec[:2*pozice]+pismeno + retezec[2*pozice+1:]     #ty dvojky tam jsou kvuli mezeram, ktere oddeluji - ve slove
        slovo = slovo[:pozice]+ "*" + slovo[pozice+1:]                  #uhodnute pismeno se vymeni za mezeru

    return(retezec, slovo)



def vyhodnot(retezec, pocet_chyb):
    ("Vyhodnoti stav hry")

    if pocet_chyb == 10:
        a = 'prohra'       #prohra hrace
    elif "_" in retezec:
        a = 'pokracujeme'              #hra pokracuje
    else:
        a = 'vyhra'       #vyhra hrace
    return(a)

def kontrola_vstupu(pismeno):
    return pismeno.isalpha() and len(pismeno) == 1


def vyber_slova(seznam):
    return random.choice(seznam)
