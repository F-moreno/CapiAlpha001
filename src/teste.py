import os


def limpatela():
    os.system("clear" if os.name == "posix" else "cls")


limpatela()

"""
1 - a)
ValueError
while True:
    try:
        numero = int(input("Insira um valor inteiro:"))
        break
    except ValueError as e:
        print(f"Erro: {e}")

1 - b)

while True:
    try:
        numero = int(input("Insira um valor inteiro:"))
        percentual = 100 / numero
        print(percentual)
        break
    except ValueError as e:
        print(f"Erro: {e}")

    except ZeroDivisionError as e:
        print(f"Erro: {e}")
"""

"""
2 - a)
while True:
   numero = int(input("Insira um valor inteiro:")) # numero = 0
   percentual = 100/numero
   break

2 - b)

# import numpy as np
# mean = [i for i in range 10 if i % 2 == 0]
# np.mean(mean)

mean * 3

2 - c)

"mean: " + 1.0
"""

"""
3 - 

class EmptyListError(Exception):
    pass


class ValueNotFoundError(Exception):
    pass


class OddValueError(Exception):
    pass


class NullValueError(Exception):
    pass


lista = [i for i in range(10)]

while True:
    try:
        i = int(input("Digita essa mizera ai: "))

        if len(lista) == 0:
            raise EmptyListError("A lista está vazia.")

        if i not in lista:
            raise ValueNotFoundError("Valor não encontrado.")

        if not i % 2 == 0:
            raise OddValueError("O valor respectivo é impar")

        if i <= 0:
            raise NullValueError("Valor menor ou igual à 0.")

    except EmptyListError as e:
        print(f"Erro: {e}")

    except ValueNotFoundError as e:
        print(f"Erro: {e}")

    except OddValueError as e:
        print(f"Erro: {e}")

    except NullValueError as e:
        print(f"Erro: {e}")

    except Exception:
        print("Fernando mama no cano")
    
    else:
            print("show papai")
            break
            
    finally:
        print("Finally executado.")
"""

"""
-Triangulo:
    Atributos:
        lado
        base
        altura
        angulo

    Metodo:
        area
        pitagoras

- Quadrado:
    Atributos:

        base
        altura
    Métodos:

        area
        perímetro

- Poligono:
    Atributos:
        
        lado
        

    Métodos:

        perimetro do poligono

        

- Circulo:
    Atributos:
        raio

    Métodos:
        diametro
        area
        corda
        arco
        setor circular
        


- Cilindro:
    Atributos:
        raio da base
        altura
        Apótema

    Métodos:
        superficie lateral
        superficie total
        volume
        inclinação

- Veículo:
    Atributos:
        capacidade

    Métodos:
        transportar()
        acelerar()
        frear()
        vira a esquerda()
        vira a direita()

-Terrestre: Veiculo
    Atributos:
        Roda
    
    metodos:
        Andar na estrada()

-Aquatico: Veiculo
    Atributo:
        Popa
        Proa
    Metodos:
        Navegar()

-Aéreo: Veiculo
    Atributos:
        hélice
    Metodos:
        Voar()
- Veículo:
    Atributos:
        capacidade

    Métodos:
        transportar()
        acelerar()
        frear()
        vira a esquerda()
        vira a direita()

-Terrestre: Veiculo
    Atributos:
        Roda
    
    metodos:
        Andar na estrada()

-Aquatico: Veiculo
    Atributo:
        Popa
        Proa
    Metodos:
        Navegar()

-Aéreo: Veiculo
    Atributos:
        hélice
    Metodos:
        Voar()

-Aviao: Aereo, Terrestre

- Carro: Terrestre
    Atributos:
        motor
        chassi
        placa
    Métodos:
        metodos veiculos
        estacionar
        fazer drifting
        ...

-Carro Hibrido: Terrestre, Aquatico

- Moto: Terrestre
    Atributos:
        motor
        chassi
        placa

    Métodos:
        dar grau
        dar babalu

- Bicicleta:
    Atributos:
        camara de ar
        aro
        coroa
        corrente
        catraca
        celin 
        quadro

    Métodos:
        metodos moto

"""
"""
CLASSES Q2 - TRIANGULO

class Triangulo:
    def __init__(self, lado:int, base:int, altura:int, angulo:float) -> None:
        self.lado = lado
        self.base = base
        self.altura = altura
        self.angulo = angulo

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area

    def TeoremaDePitagoras(self):
        if self.angulo == 90:
            c = (self.lado**2 - self.base**2) ** 1 / 2
            return c
        else:
            print("Calculo válido apenas para triângulos retangulos.")
   
   
            
QUADRADO:

class Quadrado:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area
    def calcula_perimetro(self):
        perimetro = self.base *2 + self.altura *2
        return perimetro

POLIGONO

class Poligono:
    def __init__(self, lados) -> None:
        self.lados = lados
    
    def calcula_perimetro(self):
        perimetro = sum(self.lados)
        return perimetro

CIRCULO 

class Circulo:
    def __init__(self, raio, pi = 3.141592) -> None:
        self.pi = pi
        self.raio = raio

    def calcular_area(self):
        area = self.pi * self.raio**2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * self.pi * self.raio
        return perimetro

CILINDRO

class Cilindro:
    def __init__(self, raio, altura, pi = 3.141592) -> None:
        self.raio = raio
        self.altura = altura
        self.pi = pi

    def calcular_volume(self):
        volume = self.pi * self.raio**2 * self.altura
        return volume

    def calcular_area_superficial(self):
        area_base = self.pi * self.raio**2
        area_lateral = 2 * self.pi * self.raio * self.altura
        area_total = 2 * area_base + area_lateral
        return area_total

    def __str__(self):
        return "teu cu"

VEICULO

class Veiculo:
    def __init__(self, capacidade, velocidade:int = 0) -> None:
        self.capacidade = capacidade
        self.velocidade = velocidade

    def transportar(self):
        _embarcar = int(input("Digite quantos passageiros vao embarcar: "))
        if _embarcar > self.capacidade:
            _excedente = _embarcar - self.capacidade
            print(f"Capacidade insuficiente, {_excedente} ficarão de fora.")
        else:
            print(f"{_embarcar} embarcados.")

    def acelerar(self, aceleracao):
        self.velocidade += aceleracao
        print(f"Velocidade aumentada em {aceleracao}km/h.")
        print(f"Velocidade atual: {self.velocidade + aceleracao}km/h.")

    def freia(self, frenagem):
        self.velocidade -= frenagem
        print(f"Velocidade reduzida em {frenagem}km/h.")
        print(f"Velocidade atual: {self.velocidade}km/h.")

    def vira_esquerda(self):
        print("Veiculo virou à esquerda.")

    def vira_direita(self):
        print("Veiculo virou à direita.")


class Terrestre(Veiculo):
    def __init__(self, capacidade, velocidade, rodas) -> None:
        super().__init__(capacidade, velocidade)
        self.rodas = rodas

    def andar_na_estrada(self):
        print("Veículo terrestre está andando na estrada.")


class Aquatico(Veiculo):
    def __init__(self, popa, proa, *args, **kwargs) -> None:
        super().__init__(*args, *kwargs)
        self.popa = popa
        self.proa = proa

    def navegar(self):
        print("Veículo aquático está navegando.")


class Aereo(Veiculo):
    def __init__(self, helice, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helice = helice

    def voar(self):
        print("Veículo aéreo está voando.")

"""


"""class Carro:
    def __init__(self, marca, modelo, ano, placa, opcionais=[]) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.opcionais = opcionais
        self.ligado = False
        self.velocidade = 0

    def __str__(self) -> str:
        print(f"Este é o {self.modelo}, da {self.marca}")

    def ligar(self):
        if not self.carro:
            self.ligado = True
            print("Carro funcionando")
        else:
            print("Carro já está ligado")

    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            print("Carro desligado")
        elif self.velocidade >= 10:
            print("Não é possivel desligar o carro em movimento")
        else:
            print("Carro ja está desligado")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f"Velocidade aumentada para {self.velocidade} km/h")

    def frear(self):
        if self.velocidade >= 10 and self.ligado:
            self.velocidade -= 10
            print(f"velocidade reduzida para {self.velocidade}")

    def liga_radio(self):
        print("Radio em funcionamento")
"""

"""
class Copo:
    def __init__(self):
        self.capacidade = "Vazio"

    def __str__(self):
        return f"o copo esta {self.capacidade}."


class Barman:
    def __init__(self):
        self.bebidas = 2

    def encherCopo(self, copo: Copo):
        if copo.capacidade == "Cheio":
            print("Seu copo ta cheio nengue ta maruco?")

        elif self.bebidas:
            copo.capacidade = "Cheio"
            self.bebidas -= 1
        else:
            pass


class Festeiro:
    def __init__(self, copo: Copo):
        self.copo = copo

    def beber(self):
        self.copo.capacidade = "Vazio"

    def comprar_birita(self, barman: Barman):
        barman.encherCopo(self.copo)

    def __str__(self):
        return f"{self.copo}."


Crie um objeto Copo, Barman e Festeiro.
Drink = Barman()
Pinga = Barman()
Refrigerante = Barman()

Marcotti = Festeiro(Copo())
Samir = Festeiro(Copo())
Deivid = Festeiro(Copo())

print(f"Marcotti {Marcotti}\n" + f"Samir {Samir}\n" + f"Deivid {Deivid}")

Marcotti.comprar_birita(Drink)
Marcotti.comprar_birita(Drink)
Samir.comprar_birita(Drink)
Deivid.comprar_birita(Drink)

print(f"Marcotti {Marcotti}\n" + f"Samir {Samir}\n" + f"Deivid {Deivid}")

Solicite a impressão do copo (print(copo)), 
Requisite a função encherCopo() e em seguida solicite novamente a impressão do copo. 
Analise e reflita sobre o que aconteceu."""
"""
Agora requisite a função beber() do objeto festeiro e após solicite novamente a impressão do copo. 
Algo similiar aconteceu, Analise e reflita sobre o ocorrido.
Reflita, porque isso acontece?"""

"""
class Caixa:
    def __init__(self) -> None:
        self.ticket = 0

    def __str__(self) -> str:
        return f"Aqui um exemplo de função str. {self.ticket}"

    def __iter__(self) -> int:
        return self

    def __next__(self) -> int:
        if self.ticket < 10:
            atual, self.ticket = self.ticket, self.ticket + 1
            return atual
        else:
            raise StopIteration


contador = Caixa()

for i in contador:  # i = [0,1,2,3,4,5,6,7,8,9] ; next(contador) = i+1
    print(i)

# variavel_qualquer = next(contador)
# print(contador)
# variavel_qualquer2 = next(contador)
# print(contador)
# variavel_qualquer3 = next(contador)
# print(contador)

"""


# class ImpressoraTicket:
#     def __init__(self, fichas) -> None:
#         self.fichas = fichas

#     def ficha_normal(self):
#         return self.ficha

#     def ficha_preferencial(self):
#         pass


# # class Chamada:
# #     def __init__(self) -> None:

# sistemaTicket = ImpressoraTicket()
# usuario1 = next(sistemaTicket.ficha_normal())
# usuario2 = next(sistemaTicket.ficha_normal())
# usuario3 = next(sistemaTicket.ficha_normal())
# usuario4 = next(sistemaTicket.ficha_normal())
