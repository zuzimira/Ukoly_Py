from math import ceil


class Vuz:                                  #definice tridy Vuz
    def __init__(self, typ, spz, kapacita):
        self.typ = typ
        self.spz = spz
        self.kapacita = kapacita

    def __str__(self):
        #return '<Vuz poznavaci znacky {} s kapacitou {}>'.format(self.spz, self.kapacita)
        return '{0:10} || {1:10} || {2:11} '.format(self.typ, self.spz, self.kapacita)

    def cena_za_cestu(self, trasa, cena_e, cena_n):     #vypocet ceny za cestu
        """Vrati cenu za km dle kapacity"""
        if self.typ == 'Elektro':
            cena = cena_e * trasa
        else:
            cena = cena_n * trasa

        if self.kapacita > 40:                          #zadana cena je 'zakladni', odvijim ji od velikosti autobusu
            cena *= 1.1                                 #jen cvicne, neni to realne
        elif self.kapacita > 20:
            cena*= 1.05
        return ceil(cena)




class Elektro(Vuz):

    dojezd = 100        #km
    def __str__(self):
        return '{0:10} || {1:10} || {2:11} '.format(self.typ, self.spz, self.kapacita)

class Hybrid(Elektro):

    def __str__(self):
        return '{0:10} || {1:10} || {2:11} '.format(self.typ, self.spz, self.kapacita)

    def cena_za_cestu(self, trasa, cena_e, cena_n):
        """Vrati cenu za km dle delky trasy"""

        if trasa > self.dojezd:                     #vypocita cenu cesty hybridu, do dojezdu za cenu el nad dojezd za cenu nafty
            cena = ((trasa - self.dojezd)*cena_n + self.dojezd * cena_e)
        else:
            cena = cena_e * trasa
        if self.kapacita > 40:
            cena *=  1.1
        elif self.kapacita > 20:
            cena *= 1.05

        return ceil(cena)

vozovy_park = [
    Elektro('Elektro','ABC 100', 10),
    Elektro('Elektro', 'KLM 145', 48),
    Elektro('Elektro', 'EFG 254', 60 ),
    Hybrid('Hybrid', 'UIO 100', 15),
    Hybrid('Hybrid', 'UFO 145', 40),
    Hybrid('Hybrid', 'AAA 254', 56 ),
    Vuz('Nafta', 'IJK 147', 22),
    Vuz('Nafta', 'XYZ 987', 70),
    Vuz('Nafta', 'PQR 589', 8),
]
def tiskni(seznam):
    print('Vitejte v nasem rezervacnim systemu!')
    vypis = '{0:10} || {1:10} || {2:11} '
    print('Vozovy park obsahuje:')
    print(vypis.format('typ', 'spz', 'kapacita'))
    print(39 *'=')
    for vuz in seznam:
        print(vuz)
    print()
    print('Celkova kapacita vozoveho parku je: {} osob.'.format(secti_celkovou_kapacitu(vozovy_park)))
    print(50*'=')
    print(50*'=')
    print()



def secti_celkovou_kapacitu(seznam_vozu):
    celkova_kapacita = 0
    for vuz in seznam_vozu:
        celkova_kapacita += vuz.kapacita
    return celkova_kapacita



def najdi_vuz(seznam_vozu, osoby, trasa):
    """Vytvori nabidku, ktera zahrnuje vsechny vozy, ktere splnuji poptavku.
    Vybere nejlevnejsi variantu. Vrati oboji ve forme slovniku"""
    nabidka = {}
    for vuz in seznam_vozu:     #vytvarim slovnik autobusu, ktere splnuji poptavku
       if vuz.kapacita >= osoby:
            if vuz.typ == 'Elektro' and trasa > vuz.dojezd:
                pass
            else:
                nabidka[vuz.spz] = {'typ': vuz.typ,'kapacita': vuz.kapacita, 'cena':vuz.cena_za_cestu(trasa, cena_elektrina, cena_nafta)}

    minimalni = trasa * 1000                    #toto by bylo treba aktualizovat, nastrelila jsem to
    vyber = {}
    for vuz, polozky in nabidka.items():        #hledam minimalni polozku
        cena = polozky['cena']
        if cena == minimalni:
            vyber[vuz] = ceil(cena)
        elif cena < minimalni:
            vyber={}
            vyber[vuz] = ceil(cena)
            minimalni = cena

    return   vyber, nabidka




#Tisk vysledku
#Vypisy jsem si udelala cvicne, urcite by slo zjednodusit.

def tiskni_nabidku(slovnik):
    if not slovnik:
        print('Vasim pozadavkum neodpovida zadny autobus.')
        print()
    vypis = '{0:10} || {1:10} || {2:10} || {3:10}'      #tisk autobusu, ktere splnuji poptavku
    print(vypis.format('autobus', 'typ', 'kapacita', 'cena Kc'))
    print(52 * '=')
    for vuz,parametry in slovnik.items():
        print(vypis.format(vuz, parametry['typ'], parametry['kapacita'], parametry['cena']))
    print(52 * '=')



def tiskni_nejlevnejsi(slovnik):
    print('Nejlevnejsi varianta: ')         #tisk nejlevnejsi varianty
    print()
    vypis = '{0:10} || {1:10}'
    print(vypis.format('autobus', 'cena Kc'))
    print(24 * '=')
    for vuz,cena in slovnik.items():
        print(vypis.format(vuz, cena))


tiskni(vozovy_park)
cena_elektrina = int(input('Zadej naklady na km pro elektro : '))     #Vstupy nejsou osetreny
cena_nafta = int(input('Zadej naklady na km pro naftu: '))

trasa = int(input('Zadej delku trasy: '))

pasazeri = int(input('Zadej pocet prepravovanych osob: '))
print()
print()
reseni = najdi_vuz(vozovy_park, pasazeri, trasa)

print('Nabidka pro prepravu {} osob na vzdalenost {} km:'.format(pasazeri, trasa))
print()
tiskni_nabidku(reseni[1])
print()

tiskni_nejlevnejsi(reseni[0])
print()
