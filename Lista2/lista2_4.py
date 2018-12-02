def pierwsza(n):

    lista_dzielnikow = []
    for i  in range(1, n):
        if n % i == 0:
            lista_dzielnikow.append(i)
    liczba_dzielnikow = len(lista_dzielnikow)

    if liczba_dzielnikow == 1:
        return True
    else:
        return False





