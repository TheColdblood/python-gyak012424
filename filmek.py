import FilmekO

def beolvas():
    beFile = open("film.txt", "r", encoding="utf-8")
    beFile.readline()
    sorok = beFile.readlines()
    beFile.close()
    filmek = []

    for i in range(len(sorok)):
        sor = sorok[i].strip()
        darabolt = sor.split(";")
        cim = darabolt[0]
        rendezo = darabolt[1]
        foszereplo = darabolt[2]
        ev = int(darabolt[3])
        perc = int(darabolt[4])

        film = FilmekO.Filmek(cim, rendezo, foszereplo, ev, perc)
        filmek.append(film)

    return filmek

def sorai(lista):
    print(f"\nAz adatok sorainak hossza: {len(lista)}")

def legrovidebb(lista):
    # print(f"\nA lergrövidebb film címe: {}")
    pass
