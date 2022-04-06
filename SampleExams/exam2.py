class Czytelnik:
    def otworz(self, file_name):
        self.file = open(f"{file_name}")

    def czytam(self):
        i = 1
        self.lines = []
        for line in self.file.readlines():
            if i % 2 == 0:
                self.lines.append(line)
            i += 1
    def szukam(self, combination):
        for line in self.lines:
            if combination in line:
                return True
        return False
    def licz(self, litera):
        amount = 0
        for line in self.lines:
            amount += line.count(litera)
        return amount
    def zamykam(self):
        self.file.close()

czytelnik = Czytelnik()
czytelnik.otworz("MyFile.txt")
czytelnik.czytam()
print(czytelnik.licz('b'))
czytelnik.zamykam()
