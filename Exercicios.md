# Exercicios
### Try-Except
>1- Altere os seguinte algoritmos com um bloco try-except para tratar os devidos erros, de modo que os sistemas a seguir possam ser executados sem "quebrar".
>
>- ValueError
>```py
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    break
>```
>- ValueError / ZeroDivisionError
>```py
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    percentual = 100/numero
>    break
>```
>- ValueError / ZeroDivisionError
>```py
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    percentual = 100/numero
>    break
>```
>---
>2- Os seguinte error apareceram no meu terminal, identifique cada um deles e descreva um exemplo para que eles tenham ocorrido:
>
>```
>---------------------------------------------------------------------------
>ZeroDivisionError                         Traceback (most >recent call last)
><ipython-input-1-bc757c3fda29> in <module>
>----> 1 1 / 0
>
>ZeroDivisionError: division by zero
>```
>
>```
>---------------------------------------------------------------------------
>NameError                                 Traceback (most recent call last)
><ipython-input-2-5221628d77d0> in <module>
>----> 1 mean * 3
>
>NameError: name 'mean' is not defined
>```
>```
>---------------------------------------------------------------------------
>TypeError                                 Traceback (most recent call last)
><ipython-input-3-29af19065ab3> in <module>
>----> 1 'mean: ' + 1.
>
>TypeError: can only concatenate str (not "float") to str
>```
>
>3- Utilizando try-except, crie um sistema que realize a busca de um valor em uma lista:
>
>- Caso a lista esteja vazia lance uma exceção ListaVazia.
>- Caso nao exista o valor na lista lance uma exceção ValorNaoEncontrado.
>- Encontrando o valor, caso ele seja impar lance uma exceção ValorImpar.
>- Encontrando o valor, caso ele seja zero ou menor lance uma exceção ValorNulo.
>- Caso não haja exceções imprima esta informação.
>- Independente de existir exceção escreve o valou que foi buscado.
>---
### Classes
>1- Identifique possiveis caracteristicas e ações para os seguinte objetos:
>
>- Triângulo.
>- Quadrado.
>- Poligono.
>- Circulo.
>- Cilindro.
>- Veículo.
>- Carro.
>- Moto.
>- Biclicleta.
>---
>2- Codifique cada uma das classes identificadas no exercicio 1.
>
>---
>---
>3- Crie as classes a seguir:
>- Carro.
>```
>Atributos:
>- Marca
>- Modelo
>- Ano
>- Placa
>- Opcionais (lista)
>Métodos:
>- Ligar
>- Desligar
>- Acelerar
>- Frear
>- Ligar rádio
>```
>- Distribuição Normal
>```
> Atributos:
>- Média
>- Variância
> Métodos:
>- Calcular fdp
>- Gerar amostra
>- Calcular função de distribuição acumulada
>```
>- Regressão Linear
>```
> Atributos:
>- Coeficientes
>- Intercepto
> Métodos:
>- Ajustar a uma amostra
>- Estimar valores para nova amostra
>- Calcular R2
>- Realizar testes de hipótese
>```
>---
>4- Analise o código, realize os testes propostos e responda a seguir:
>```py
>class Copo:
>    def __init__(self):
>        self.capacidade = "Vazio"
>
>    def __str__(self):
>        return f"O copo esta {self.capacidade}."
>
>class Barman:
>    def __init__(self, copo: Copo):
>        self.copo = copo
>
>    def encherCopo(self):
>        self.copo.capacidade = "Cheio"
>
>class Festeiro:
>    def __init__(self, copo: Copo):
>        self.copo = copo
>
>    def beber(self):
>        self.copo.capacidade = "Vazio"
>```
>- Crie um objeto Copo, em seguida crie um objeto Barman e Festeiro passando o copo criado como parametro.
>- Solicite a impressão do copo (```print(copo)```), Requisite a função ```encherCopo()``` e em seguida solicite novamente a impressão do copo. Analise e reflita sobre o que aconteceu.
>- Agora requisite a função ```beber()``` do objeto festeiro e após solicite novamente a impressão do copo. Algo similiar aconteceu, Analise e reflita sobre o ocorrido.
>- Reflita, porque isso acontece?
>---
>5- Crie uma classe carro e uma classe motorista o motorista deve alterar os atributos do carro como acelerar e freiar.
>
>---
### Iterator
>1- Conserte o seguinte programa em Python para que a classe.
>
>---
### Herança
>1-Implemente o seguinte diagrama:
>           
>- Atleta
>```
> Atributos:
>- Aposentado: bool
>- Peso: float
> Métodos:
>- Aposentar
>- Aquecer
>```
>- Corredor: Atleta
>```
> Atributos:
>- 
> Métodos:
>- Correr
>```
>- Nadador: Atleta
>```
> Atributos:
>- 
> Métodos:
>- Nadar
>```
>- Ciclista: Atleta
>```
> Atributos:
>- 
> Métodos:
>- Pedalar
>```
>- TriAtleta: Corredor,Nadador,Ciclista
>```
> Atributos:
>- 
> Métodos:
>- Pedalar
>```