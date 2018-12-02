def porzadek_imion(imiona):

    imiona_posortowane = imiona.sort()
    return imiona_posortowane


def liczba_imion(imiona):

    i = 0
    for imie in imiona:
        if imie[-1] == "a":
            i = i + 1
    return i


imiona = ["Aneta", "Barbara", "Filip", "Mariusz", "Ignacy", "Adam", "Maria", "Paulina"]


print(porzadek_imion(imiona))
print("Liczba imion w liście: ", liczba_imion(imiona))
