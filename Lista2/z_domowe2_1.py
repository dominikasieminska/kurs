def rozmien(portfel, kwota):
    suma = 0
    maxindex = len(portfel) - 1
    lista_nominalow = [0] * len(portfel)


    for index, l_nominalow in enumerate(portfel[::-1]):
        nominal = maxindex - index

        if nominal != 0 and l_nominalow != 0:
            liczba_potrzebnych_nominalow = (kwota - suma)//nominal
            if liczba_potrzebnych_nominalow > l_nominalow:
                liczba_potrzebnych_nominalow = l_nominalow
            suma = suma + liczba_potrzebnych_nominalow * nominal
        else:
            liczba_potrzebnych_nominalow = 0

        portfel[index] = l_nominalow - liczba_potrzebnych_nominalow
        lista_nominalow[nominal] = liczba_potrzebnych_nominalow
        #print ("Nominał " + str(nominal) + "zł" + " w ilości: " + str(liczba_potrzebnych_nominalow))

    while suma < kwota:
        if portfel == 0 * len(portfel):
            break
        for index, l_nominalow in enumerate(portfel[::-1]):
            nominal = maxindex - index

            if nominal != 0 and l_nominalow != 0:
                liczba_potrzebnych_nominalow = 1
                suma = suma + nominal
            else:
                liczba_potrzebnych_nominalow = 0

            portfel[index] = l_nominalow - liczba_potrzebnych_nominalow
            lista_nominalow[nominal] = lista_nominalow[nominal] + liczba_potrzebnych_nominalow


    print(suma)

    print(portfel, " - Portfel po wydaniu")
    print(lista_nominalow, " - Do wydania")



portfel = [0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 11]
rozmien(portfel, 123)