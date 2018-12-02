from Lista1 import lista1_5


def zakupy(cennik, lista):

    rachunek_netto = 0
    kwoty_zakupow = []

    for produkt in lista:
        kwota = lista[produkt] * cennik[produkt]
        rachunek_netto += kwota
        kwoty_zakupow.append(kwota)

    kwota_vat = lista1_5.vat_paragon(kwoty_zakupow)
    rachunek_brutto = rachunek_netto + kwota_vat

    return rachunek_brutto


cennik = {
    'kawa': 14.99,
    'pomarańcze': 3.49,
    'olej': 4.99
    }
lista = {'olej': 2, 'kawa': 1}
print(zakupy(cennik, lista))


