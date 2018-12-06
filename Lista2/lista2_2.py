def odsetki(oproc, czas, kwota):

    wynik = kwota * (oproc/100) * (czas/12)
    return wynik


print(odsetki(3, 12, 1000))


def odsetki_odn(oproc, czas, kwota, odn):

    kwota_pierwotna = kwota

    for i in range(odn+1):
        kwota = odsetki(3, 3, kwota) + kwota

    print(kwota - kwota_pierwotna)


odsetki_odn(3, 3, 1000, 3)

