def zbuduj_zdania(lista):

    wynik = ""
    for zdanie in lista:
        for slowo in zdanie:
            if zdanie.index(slowo) == 0:
                wynik += slowo.capitalize() + " "
            elif zdanie.index(slowo) == len(zdanie) - 1:
                wynik += slowo + ". "
            else:
                wynik += slowo + " "

    return wynik


lista = [ ["łódź", "się", "obudziła"],
              ["ogary", "poszły", "w", "las"] ]

print(zbuduj_zdania(lista))

