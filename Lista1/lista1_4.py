def podatek(kwota):

    granica_dolna = 44490
    granica_gorna = 85528

    if kwota <= granica_dolna:
        wynik = 0.19 * kwota

    elif kwota > granica_dolna and kwota <= granica_gorna:
        wynik = 0.19 * granica_dolna + 0.3 * (kwota - granica_dolna)

    else:
        wynik = 0.19 * granica_dolna + 0.3 * (granica_gorna - granica_dolna) + 0.4 * (kwota - granica_gorna)
    return wynik

print(podatek(100000))