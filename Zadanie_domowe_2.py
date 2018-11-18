def rachunek(kwota):

    liczba_b20 = kwota//20
    suma = liczba_b20 * 20
    liczba_b10 = (kwota - suma)//10
    suma = suma + liczba_b10 * 10
    liczba_m5 = (kwota - suma)//5
    suma = suma + liczba_m5 * 5
    liczba_m2 = (kwota - suma)//2
    suma = suma + liczba_m2 * 2
    liczba_m1 = (kwota - suma)//1
    suma = suma + liczba_m1 * 1

    print(str(liczba_b20) + " - liczba banknotów 20zł")
    print(str(liczba_b10) + " - liczba banknotów 10zł")
    print(str(liczba_m5) + " - liczba monet 5zł")
    print(str(liczba_m2) + " - liczba monet 2zł")
    print(str(liczba_m1) + " - liczba monet 1zł")

rachunek(123)