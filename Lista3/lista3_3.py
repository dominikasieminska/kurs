def statystyka(nazwa_pliku):

    znaki_konca_zdania = ['.', '!', '?']
    liczba_zdan = 0

    with open(nazwa_pliku, 'r') as fh:
        tekst = fh.read()

    liczba_znakow = len(tekst)
    liczba_wyrazow = len(tekst.split())
    for znak in znaki_konca_zdania:
        liczba_zdan += len(tekst.split(znak))-1

    print(F"Liczba znaków to {liczba_znakow}")
    print(F"Liczba wyrazów to {liczba_wyrazow}")
    print(F"Liczba zdań to {liczba_zdan}")


statystyka("D:\Pulpit/test.txt")