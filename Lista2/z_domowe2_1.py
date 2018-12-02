def rozmien(portfel, kwota):
    suma = 0
    maxindex = len(portfel) - 1

    for index, elem in enumerate(portfel[::-1]):
        nominal = maxindex - index

        if nominal != 0 and elem != 0:
            liczba = (kwota - suma)//nominal
            if liczba > elem:
                liczba = elem
            suma = suma + liczba * nominal
        else:
            liczba = 0

        portfel[index] = elem-liczba
        print ("Nominał " + str(nominal) + "zł" + " w ilości: " + str(liczba))

    # print (portfel[::-1])
    # print (suma)


portfel = [0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 10]
rozmien(portfel, 123)