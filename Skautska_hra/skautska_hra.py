import random

moznosti = int(input('Kolik moznosti odpovedi na otazku budes vkladat? '))
print()

def odpovedi(pocet):
    """vrati slovnik , kde klic je otazka a hodnota je seznam ruznych odpovedi"""
    seznam_otazek = ['Jaky? ', 'Kdo? ', 'Co delal? ', 'Kde? ', 'Kdy? ', 'Proc? ']
    zasoba_slov = {}
    for otazka in seznam_otazek:
        odpoved = []
        while len(odpoved) < moznosti:
            if otazka == 'Jaky? ':
                slovo=input(otazka).title()

            elif otazka == 'Kdy? ':
                slovo = input(otazka)+','

            elif otazka == 'Proc? ':
                slovo = input(otazka)+'.'

            else:
                slovo = input(otazka)
            odpoved.append(slovo)
            zasoba_slov[otazka] = odpoved
    return zasoba_slov


def vypis_hru(slovnik):
    """Vypise 'zertovnou vetu', kazde slovo nahodne vybere z moznosti"""
    print("Nase veta zni:")
    print()
    for i in slovnik.values():
        print('{} '.format(random.choice(i)), end = '')
    print()


vypis_hru(odpovedi(moznosti))     
