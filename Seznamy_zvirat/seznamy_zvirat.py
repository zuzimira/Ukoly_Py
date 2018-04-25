#Domaci projekty sedma lekce
#Ulohy 1. - 6.


seznam_zvirat1 = ["holubicka","prasatko","koza", "kun", "pes", "husa", "kocka", "kralik", "had", "kruta", "andulka"]
seznam_zvirat2 = ["vul","koza", "pes", "husa", "kralik", "had", "kruta", "krava", "slepice","kachna", "osel"]


def kratka_slova (seznam):
    "Vraci slova kratsi nez 5 pismen"

    kratsi = []
    for zvire in seznam:
        if len(zvire)<5:
            kratsi.append(zvire)

    return kratsi

def prvni_k (seznam):
    "Vraci slova zacinajici na K"
    na_k = []
    for zvire in seznam:

        if zvire.startswith("k"):
            na_k.append(zvire)

    return na_k

def over (seznam, slovo):
    "Vrati, zda je zadane slovo v seznamu"
    return slovo in seznam

def porovnej (seznam1, seznam2):
#    """Porovna dva seznamy a vrati tri.
#    V prvnim jsou slova, kter8 jsou v obou seznamech,
#    ve druhem ta, co jsou pouze v prvnim seznamu
#    a ve tretim ta, co jsou pouze ve druhem seznamu."""

    seznam_oba = []
    seznam_jen1 = []
    seznam_jen2 = []
    vysledek = []

    for zvire in seznam1:
        if zvire in seznam2:
            seznam_oba.append(zvire)
        else:
            seznam_jen1.append(zvire)

    for zvire in seznam2:
        if zvire not in seznam_zvirat1:
            seznam_jen2.append(zvire)

    return(seznam_oba, seznam_jen1, seznam_jen2 )

def serad(seznam):
    """Seradi prvky seznamu podle abecedy"""
    seznam.sort()
    return seznam

def serad2(seznam):
    """Seradi seznam dle druheho pismene"""

    seznam_dvojic = []                 #Radi podle druheho pismena, jsou li stejna, nasleduje prvni
    for zvire in seznam:
        seznam_dvojic.append((zvire[1],zvire))      #vytvori dvojice a seradi podle klice, klic je druhe pismeno
    seznam_dvojic.sort()

    seznam_klic = []
    for dvojice in seznam_dvojic:          #vytvori novy seznam zvirat, serazeny dle klice
        seznam_klic.append(seznam_dvojic[seznam_dvojic.index(dvojice)][1])
    return seznam_klic



#volani funkci

print(kratka_slova (seznam_zvirat1))
print()

print(prvni_k (seznam_zvirat1))
print()

slovo = input("Zadej zvire:")
print(over (seznam_zvirat1, slovo))
print()

print(porovnej (seznam_zvirat1, seznam_zvirat2))
print()

print(serad(seznam_zvirat1))
print()

print(serad2(seznam_zvirat1))
print()
