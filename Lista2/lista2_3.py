def dzielniki(n):

    lista_dzielnikow = []
    for i  in range(1, n):
        if n % i == 0:
            lista_dzielnikow.append(i)

    return lista_dzielnikow


print(dzielniki(6))
print(dzielniki(8))

