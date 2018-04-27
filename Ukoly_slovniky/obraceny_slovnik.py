narozeniny = {
    'Hanka': '20.03.',
    'Petr': '05.05.',
    'Jitka': '20.03.',
    'Adam': '15.11.',

}

# BONUS
# vytvoř ze stávajího slovníku nový "obrácený" slovník,
# kde klíčem bude vždy datum a hodnotou seznam jmen
# (tj. počítej s tím, že jich může být u jednoho data více)

narozeniny_obraceno = {}
seznam = []

for polozka in narozeniny.items():

    if polozka[1] not in narozeniny_obraceno:
        seznam.append(polozka[0])
        narozeniny_obraceno[polozka[1]] = seznam
        seznam = []
    else:
        narozeniny_obraceno[polozka[1]].append(polozka[0])


print(narozeniny_obraceno)
