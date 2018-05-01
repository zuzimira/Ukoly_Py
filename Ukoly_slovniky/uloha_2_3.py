def secti_znaky(retezec):
    """Vrati slovnik, kde klice jsou jednotlive znaky se zadaneho retezce
    a hodnoty je jejich cetnost"""
    slovnik_znaky = {}
    for znak in retezec:
        if znak not in slovnik_znaky:
            slovnik_znaky[znak] = retezec.count(znak)
    return(slovnik_znaky)


def secti_znaky(retezec):
    """Vrati slovnik, kde klice jsou jednotlive znaky se zadaneho retezce
    a hodnoty je jejich cetnost"""
    slovnik_znaky = {}
    for znak in retezec:
        if znak not in slovnik_znaky:
            slovnik_znaky[znak] = retezec.count(znak)
    return(slovnik_znaky)


def secti_znaky1(retezec):
    """Vrati slovnik, kde klice jsou jednotlive znaky se zadaneho retezce
    a hodnoty je jejich cetnost"""
    znaky = set(retezec)
    slovnik_znaky = {}
    for znak in znaky:
        slovnik_znaky[znak] = retezec.count(znak)
    return(slovnik_znaky)


def vypis_slovnik(slovnik):
    """Vypise polozky zadaneho slovniku, kazdou na jeden radek"""
    i = 1
    for polozka in slovnik.items():
        if polozka[0] == ' ':
            print('{}. radek: klic = {}  hodnota = {}'.format(i, 'mezera', polozka[1]))

        else:
            print('{}. radek: klic = {}       hodnota = {}'.format(i, polozka[0], polozka[1]))
        i+=1



print(vypis_slovnik(secti_znaky('!kobyla ma maly bok!')))
print(vypis_slovnik(secti_znaky1('!kobyla ma maly bok!')))
