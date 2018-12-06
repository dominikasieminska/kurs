import random

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):

    nowa_lista_slow = []
    lista_slow = tekst.split(" ")
    for slowo in lista_slow:
        if len(slowo) <= dl_slowa:
            nowa_lista_slow.append(slowo)

    nowa_liczba_slow = len(nowa_lista_slow)

    while liczba_slow < nowa_liczba_slow:
        index = random.randint(0, len(nowa_lista_slow)-1)
        del nowa_lista_slow[index]
        nowa_liczba_slow = len(nowa_lista_slow)

    nowy_tekst = " ".join(nowa_lista_slow)

    return nowy_tekst



tekst = "Podział peryklinalny inicjałów wrzecionowatych \
        kambium charakteryzuje się ścianą podziałową inicjowaną \
        w płaszczyźnie maksymalnej."


print(uprosc_zdanie(tekst, 10, 5))