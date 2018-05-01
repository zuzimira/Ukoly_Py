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


for jmeno, datum in narozeniny.items():

    if datum not in narozeniny_obraceno:

        narozeniny_obraceno[datum] = [jmeno]        #vytvorim seznam
        
    else:
        narozeniny_obraceno[datum].append(jmeno)


print(narozeniny_obraceno)
