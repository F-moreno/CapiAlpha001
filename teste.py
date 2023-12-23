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
"""
"""
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
"""

"""
2 - b)

# import numpy as np
# mean = [i for i in range 10 if i % 2 == 0]
# np.mean(mean)

mean * 3
"""

"""
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

        else:
            print("show papai")
            break

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
    def __init__(self, lado, base, altura, angulo) -> None:
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
"""


# - Poligono:
#     Atributos:
#         lado
#     Métodos:
#         perimetro do poligono
