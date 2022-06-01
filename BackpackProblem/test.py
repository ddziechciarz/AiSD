# def wczytaj(sciezka):
#     dane = []
#     with open(sciezka) as f:
#         danej = f.read().split('\n')[2:]
#     for i in range(len(danej)):
#         dane.append(list(map(int, danej[i].split(','))))
#     return dane

def wczytaj():
    #read data and automatically convert each field to int
    f = open("packages/packages20.txt")
    l = f.readlines()
    l = l[2:]

    products = []

    for line in l:
        new_line = []
        line = line.split(",")
        for element in line:
            new_line.append(int(element))
        products.append(new_line)
    return products
def sprawdz_miejsce(plecak, y, x, przedmiot):
    szerokosc, wysokosc = przedmiot[1], przedmiot[2]
    if x + szerokosc <= len(plecak[0]) and y + wysokosc <= len(plecak):
        suma = 0
        for i in range(y, y + wysokosc):
            for j in range(x, x + szerokosc):
                suma += plecak[i][j]
        if not suma:
            return (szerokosc, wysokosc)
    # if y + wysokosc <= len(plecak) and x + szerokosc <= len(plecak[0]):
    #     suma = 0
    #     for i in range(y, y + szerokosc):
    #         for j in range(x, x + wysokosc):
    #             suma += plecak[i][j]
    #     if not suma:
    #         return (wysokosc, szerokosc)
    return None

def wrzuc_przedmiot(plecak, y, x, szerokosc, wysokosc, id):
    for i in range(y, y+wysokosc):
        for j in range(x, x+szerokosc):
            #print(i,j)
            plecak[i][j] = id

def pokaz_plecak(plecak):
    for wiersz in plecak:
        print(wiersz)


def wsadz_przedmiot(plecak, szerokosc, wysokosc, przedmiot):
    for i in range(wysokosc):
        for j in range(szerokosc):
            wymiary = sprawdz_miejsce(plecak, i, j, przedmiot)
            # print(wymiary)
            if plecak[i][j] == 0 and wymiary is not None:  # not False -> True
                # print(f"adding item on {wymiary}")
                wrzuc_przedmiot(plecak, i, j, wymiary[0], wymiary[1], przedmiot[0])
                return przedmiot[3]

def zapelnij_plecak(przedmioty, szerokosc, wysokosc):
    plecak = [[0 for _ in range(szerokosc)] for _ in range(wysokosc)]
    wynik = 0
    for przedmiot in przedmioty:
        value = wsadz_przedmiot(plecak, szerokosc, wysokosc, przedmiot)
        if value is not None:
            wynik += value


    pokaz_plecak(plecak)

    print(wynik)


if __name__ == '__main__':
    dane = sorted(wczytaj(), key=lambda x: x[3] / (x[1] * x[2]), reverse=True)
    print(dane)
    #global wynik
    #wynik = 0
    zapelnij_plecak(dane, 20, 20)



