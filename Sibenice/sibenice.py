from pomocne_funkce import ukazuji_slovo, vyhodnot, tiskni_sibenici, kontrola_vstupu, vyber_slova

slova = ["PARAPSYCHOLOGIE", "HROMDOPOLICE", "POSTAVA", "BRADAVICE", "BRONTOSAURUS", "KONIKLEC"]
def sibenice():    # Prubeh hry
    "Vrati konecny stav hry"
    hadane_slovo = vyber_slova(slova)         #nahodny vyber slova + tisk hraciho pole
    pole_hra = "_ " * len(hadane_slovo)
    print (pole_hra)
    neuspesne_pokusy = 0
    kontrola = 'pokracujeme'
    while kontrola =='pokracujeme':        #hra bezi do vyhry nebo prohry hrace
        zadane_pismeno = input("Zadej pismeno, o kterem si myslis, ze je ve slove:  ")
        try:
            if not kontrola_vstupu(zadane_pismeno):                    #osetreni spatneho vstupu
                raise ValueError('Nebylo zadano pismeno.')
        except ValueError:
            print('Nezadal jsi pismeno! Zkus to znova. ')
            continue

        zadane_pismeno = zadane_pismeno.upper()

        if zadane_pismeno not in hadane_slovo:                  #pokud hadane pismeno neni ve slove, nacte se neuspesny pokus a vytiskne prislusna sibenice
            neuspesne_pokusy += 1
            print(tiskni_sibenici(neuspesne_pokusy))
        pole_hra, hadane_slovo = ukazuji_slovo (zadane_pismeno, hadane_slovo,pole_hra) #tady se trochu divim,ze o funguje
        print(pole_hra)

                   #vytiskne stav hraciho pole po hadani pismene
        kontrola = vyhodnot(pole_hra, neuspesne_pokusy)



    if kontrola == 'prohra':        #vyhodnoceni, zda nedoslo k vyhre nebo prohre
        return "Prohral jsi. "
        print()

    elif kontrola == 'vyhra':
        return "Vyhral jsi."
        print()
