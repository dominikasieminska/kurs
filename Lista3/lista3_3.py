def statystyka(nazwa_pliku):

    with open(nazwa_pliku, 'r') as fh:
        tekst = fh.read()
        liczba_znakow = len(tekst)
        liczba_wyrazow = len(tekst.split())
        liczba_zdan = len(tekst.split('.'))-1

        print(F"Liczba znaków to {liczba_znakow}")
        print(F"Liczba wyrazów to {liczba_wyrazow}")
        print(F"Liczba zdań to {liczba_zdan}")


statystyka("D:\Pulpit/test.txt")