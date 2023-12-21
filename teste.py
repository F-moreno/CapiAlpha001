class Copo:
    def __init__(self):
        self.capacidade = "Vazio"

    def __str__(self):
        return f"O copo esta {self.capacidade}."


class Barman:
    def __init__(self, copo: Copo):
        self.copo = copo

    def encherCopo(self):
        self.copo.capacidade = "Cheio"


class Festeiro:
    def __init__(self, copo: Copo):
        self.copo = copo

    def beber(self):
        self.copo.capacidade = "Vazio"


copo = Copo()
barman = Barman(copo)
festeiro = Festeiro(copo)

print(copo)
barman.encherCopo()
print(copo)
festeiro.beber()
print(copo)
