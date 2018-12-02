import lista2_4

def dzielniki_pierwsze(n):

    lista_dzielnikow = []
    for i  in range(1, n+1):
        if n % i == 0 and lista2_4.pierwsza(i) == True:
            lista_dzielnikow.append(i)

    return lista_dzielnikow

print("Test dzielniki_pierwsze:")
print("Dzielniki pierwsze liczby 6:", dzielniki_pierwsze(6))
print("Dzielniki pierwsze liczby 8:", dzielniki_pierwsze(8))


def doskonala(n):

    suma = 0
    lista_dzielnikow = []
    for i  in range(1, n):
        if n % i == 0:
            lista_dzielnikow.append(i)

    for i in lista_dzielnikow:
        suma += i

    if suma == n:
        return True
    else:
        return False

print("Test doskonala:")
print("Sprawdzenie czy liczba 12 jest doskonała:", doskonala(12))
print("Sprawdzenie czy liczba 6 jest doskonała:", doskonala(6))
print("Sprawdzenie czy liczba 28 jest doskonała:", doskonala(28))


def kolejne_doskonale(n):

        wynik = []
        i = 1
        while len(wynik) < n:
            if doskonala(i):
                wynik.append(i)
            i = i + 1
        return wynik

print("Test kolejne_doskonale:")
print("Kolejne 4 pierwsze liczby doskonałe:", kolejne_doskonale(4))

