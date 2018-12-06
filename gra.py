import komputer

stan_gry = 10

gracz = 0


def ruch_gracza(stan_gry):
    print("Na stole jest {0} zapałek".format(stan_gry))
    ruch = int(input("Podaj liczbę zapałek"))
    return ruch

print("Zaczynamy. Jest {0} zapałek".format(stan_gry))
while stan_gry > 0:
    if gracz == 0:
        ruch = komputer.strategia(stan_gry)
    else:
        ruch = ruch_gracza(stan_gry)
    if ruch < 1 or ruch > 3 or ruch > stan_gry:
        print("Błąd. Ruch jest niepoprawny.")
    stan_gry = stan_gry - ruch
    print("Gracz {2} wziął {0} zapałek. Zostało {1}".format(ruch, stan_gry, gracz))
    gracz = 1 - gracz
