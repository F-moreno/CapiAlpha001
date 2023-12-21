<!--Python-->
# Exercicios

### Try-Except
>1- Altere os seguinte algoritmos com um bloco try-except para tratar os devidos erros, modo que os sistemas a seguir possam ser executados sem "quebrar".
>
>a-)ValueError
>```py
>
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    break
>
>```
>
>b-)ValueError / ZeroDivisionError
>
>```py
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    percentual = 100/numero
>    break
>```
>
>c-)ValueError / ZeroDivisionError
>```py
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    percentual = 100/numero
>    break
>```
>2- Utilizando try-except, crie um sistema que realize a busca de um valor em uma lista:
>
>- Caso a lista esteja vazia lance uma exceção ListaVazia.
>- Caso nao exista o valor na lista lance uma exceção ValueNaoEncontrado.
>- Encontrando o valor, caso ele seja impar lance uma exceção ValorImpar.
>- Encontrando o valor, caso ele seja zero ou menor lance uma exceção ValorNulo.
>- Caso não haja exceções imprima esta informação.
>- Independente de existir exceção escreve o valou que foi buscado.

## Classes
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
>
>2- Codifique cada uma das classes identificadas no exercicio 1.
>
>3- Analise o código, e responda a seguir:
>
>```py
>class Copo:
>    def __init__(self):
>        self.capacidade = "Vazio"
>
>    def __str__(self):
>        return f"O copo esta {self.capacidade}."
>
>
>class Barman:
>    def __init__(self, copo: Copo):
>        self.copo = copo
>
>    def encherCopo(self):
>        self.copo.capacidade = "Cheio"
>
>
>class Festeiro:
>    def __init__(self, copo: Copo):
>        self.copo = copo
>
>    def beber(self):
>        self.copo.capacidade = "Vazio"
>```
>
>
>

crie uma classe carro e uma classe motorista
o motorista deve alterar os atributos do carro como acelerar e freiar