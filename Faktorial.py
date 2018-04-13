while True:
    cislo = input("Zadej cele cislo, vypocitam faktorial: ")
    if not cislo.isdigit():
        print('Nezadal jsi cislo, zkus to znova!')
        continue
    else:
        cislo = int(cislo)

    faktorial=1
    for i in range(2,cislo+1):
        faktorial *= i
    print(faktorial)
    break
