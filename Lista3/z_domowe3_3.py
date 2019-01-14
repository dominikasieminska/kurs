import csv

def wartosc_akcji(plik_csv, posiadane_akcje):

    wartosc_akcji = 0
    with open(plik_csv,'r') as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            for key in posiadane_akcje:
                if row[0] == key:
                    print(row[0])
                    print(row[1])
                    wartosc_akcji += int(row[1])*posiadane_akcje[key]


    csvFile.close()
    print(F"Wartość posiadanych akcji: {wartosc_akcji} zł")


posiadane_akcje = {
    'AB SA': 2,
    'AC SA': 1
}

plik_csv = "D:\Pulpit\moneypl-1546722249510.csv"
wartosc_akcji(plik_csv, posiadane_akcje)
