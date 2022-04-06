class Liczba():
    def __init__(self, number: int):
        self.number = number

    def dodaj(self, inny):
        if type(inny) == Liczba:
            return self.number + inny.number
        if type(inny) == Wyraz:
            return self.number + ord(inny.word[-1])

    def odejmij(self, inny):
        if type(inny) == Liczba:
            return self.number - inny.number
        if type(inny) == Wyraz:
            return "???"

class Wyraz():
    def __init__(self, word: str):
        self.word = word

    def dodaj(self, inny):
        if type(inny) == Wyraz:
            return self.word + inny.word
        if type(inny) == Liczba:
            return ord(self.word[-1]) + inny.number

    def odejmij(self, inny):
        if type(inny) == Wyraz:
            if max(len(self.word), len(inny.word)) == len(self.word):
                return self.word
            return inny.word
        if type(inny) == Liczba:
            return "???"

liczba1 = Liczba(5)
liczba2 = Liczba(10)

wyraz1 = Wyraz("hej ")
wyraz2 = Wyraz("czesc")

print(wyraz1.odejmij(wyraz2))

