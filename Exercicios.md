<!--Python-->
# Exercicios

### Try-Except
>**1-** Altere os seguinte algoritmos com um bloco try-except para tratar os devidos erros, modo que os sistemas a seguir possam ser executados sem "quebrar".
>
>**a-)****ValueError
>```py
>
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    break
>
>```
>
>**b-)**ValueError / ZeroDivisionError
>
>```py
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    percentual = 100/numero
>    break
>```
>
>**c-)**ValueError / ZeroDivisionError
>```py
>while True:
>    numero = int(input("Insira um valor inteiro:"))
>    percentual = 100/numero
>    break
>```
>**2-** Utilizando try-except, crie um sistema que realize a busca de um valor em uma lista:
>
>**a-)** Caso a lista esteja vazia lance uma exceção ListaVazia.
>**b-)** Caso nao exista o valor na lista lance uma exceção ValueNaoEncontrado.
>**c-)** Encontrando o valor, caso ele seja impar lance uma exceção ValorImpar.
>**d-)** Encontrando o valor, caso ele seja zero ou menor lance uma exceção ValorNulo.
>**e-)** Caso não haja exceções imprima esta informação.
>**f-)** Independente de existir exceção escreve o valou que foi buscado.

