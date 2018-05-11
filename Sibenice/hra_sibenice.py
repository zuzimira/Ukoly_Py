from sibenice import sibenice


while True:                                                #dokud hrac chce hrat, hraje se
    dalsi_hra = input("Chces hadat slovo? (ano/ne)  ")
    try:                                                    #osetreni spatne odpovedi
        if dalsi_hra == 'ne':
            break
        elif dalsi_hra != 'ano':
            raise ValueError('Spatna odpoved.')
    except ValueError:
            print('Zadal jsi spatnou odpoved! Mozne je pouze ano nebo ne. ')
            continue

    print(sibenice())               #volani hry
