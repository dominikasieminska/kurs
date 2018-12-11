class NotStringError(Exception):
    pass

def klasyfikator(napis):
    if not isinstance(napis, str):
        raise NotStringError()
    for slowo in napis.split():
        if len(slowo) > 5:
            klasyfikacja = "+"
        else:
            klasyfikacja = "-"

        print("{0} {1}".format(klasyfikacja, slowo))


#klasyfikator("Lorem ipsum dolor sit amet, consecteur adipiscing elit.")
klasyfikator(2)