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

VEICULO

class Veiculo:
    def __init__(self, capacidade, velocidade) -> None:
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
        print(f"Velocidade atual: {self.velocidade - frenagem}km/h.")

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
