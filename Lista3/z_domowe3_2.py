import urllib.request


def statystyka(plik):
    statystyka_slow = {}
    if plik is None:
        return None
    with urllib.request.urlopen(plik) as response:
        html = response.read()
    tekst = html.decode("utf8")

    slowa = tekst.split()
    for slowo in slowa:
        if slowo in statystyka_slow:
            statystyka_slow[slowo] += 1
        else:
            statystyka_slow[slowo] = 1

    return statystyka_slow

statystyka("https://wolnelektury.pl/katalog/lektura/rodzina-polanieckich.html")


def porownanie_statystyk(plik1, plik2):

    lista_slow_tylko_w_1 = []
    lista_slow_tylko_w_2 = []
    statystyka_1 = statystyka(plik1)
    statystyka_2 = statystyka(plik2)

    for slowo in statystyka_1:
        if slowo not in statystyka_2:
            lista_slow_tylko_w_1.append(slowo)

    for slowo in statystyka_2:
        if slowo not in statystyka_1:
            lista_slow_tylko_w_2.append(slowo)

    print("Lista słów tylko w pliku 1: ", lista_slow_tylko_w_1)
    print("Lista słów tylko w pliku 2: ", lista_slow_tylko_w_2)


porownanie_statystyk("https://wolnelektury.pl/katalog/lektura/rodzina-polanieckich.html", "https://wolnelektury.pl/katalog/lektura/pan-tadeusz.html")