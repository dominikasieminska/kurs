class Wyrazenie:
    pass

class Zmienna(Wyrazenie):

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def oblicz(self, stan):
        return stan[self.nazwa]



class Stala(Wyrazenie):

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def oblicz(self, stan):
        return int(self.nazwa)


class Dodawanie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " + " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) + self.prawy.oblicz(stan)

class Mnozenie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " * " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) * self.prawy.oblicz(stan)

wyrazenie = Dodawanie(Dodawanie(Zmienna("x"), Zmienna("y")), Zmienna("z"))
print(wyrazenie)
stan = {'x' : 1, 'y' : 2, 'z' : 3}
print(wyrazenie.oblicz(stan))


wyrazenie2 = Mnozenie(Mnozenie(Zmienna("x"), Zmienna("y")), Zmienna("z"))
print(wyrazenie2)
stan = {'x' : 1, 'y' : 3, 'z' : 3}
print(wyrazenie2.oblicz(stan))



wyrazenie3 = Mnozenie(Stala("4"), Stala("5"))
print(wyrazenie3)
print(wyrazenie3.oblicz(stan))