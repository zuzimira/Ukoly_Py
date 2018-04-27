def slovnik_mocniny(cislo):
    """Vrati slovnik, kde klice jsou cisla od nuly do zadaneho cisla
    a hodnoty jsou jeho druh0 mocniny"""
    druhe_mocniny = {}
    for i in range(cislo +1):
        druhe_mocniny[i] = i**2
    return(druhe_mocniny)

def secti(slovnik):
    """Vrati sumu vsech klicu a sumu vsech hodnot"""
    suma_klicu = 0
    suma_hodnot = 0
    for dvojice in slovnik.items():
        suma_klicu += dvojice[0]
        suma_hodnot += dvojice[1]
    return suma_klicu, suma_hodnot

print(slovnik_mocniny(7))
print(secti(slovnik_mocniny(7)))
