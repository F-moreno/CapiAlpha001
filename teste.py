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

        tama
        nho dos lados
        altura
        angulo

    Metodo:
        área
        hipotenusa
        soma_AI

- Quadrado:
    Atributos:

        ângulo reto
        diagonais iguais
        simetrias
        relação trigonométrica
    Métodos:

        area
        perímetro

- Poligono:
    Atributos:
        
        lado
        angulo interno
        vertice

    Métodos:

        perimetro do poligono
        area de um poligono
        

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
        roda
        pneu
        porta
        espelhos
        motor
        ...

    Métodos:
        acelerar
        frenar
        virar à direita
        virar à esquera


- Carro:
    Atributos:
        atributos veiculo
    Métodos:
        metodos veiculos
        estacionar
        fazer drifting
        ...


- Moto:
    Atributos:
        atributos veiculo
        

    Métodos:
        metodos veiculos
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


# class Triangulo:
#     def __init__(self, area, pitagoras, somaAngulosInternos) -> None:
#         self.area = area
#         self.pitagoras = pitagoras
#         self.somaAngulosInternos = somaAngulosInternos
# class Triangulo:
#     def __init__(self, area, pitagoras, somaAngulosInternos) -> None:
#         self.area = area
#         self.pitagoras = pitagoras
#         self.somaAngulosInternos = somaAngulosInternos
