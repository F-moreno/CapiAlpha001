"""Questao 1"""
while True:
    try:
        numero = int(input("Insira um valor inteiro:"))
        percentual = 100 / numero
        break
    except ValueError as e:
        print(f"Erro: {e}")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")

"""Questao 2"""
# Erro ZeroDivisionError ocorre quando existe uma tentativa de
# dividir por 0
# Ex.: divisao = 1 / 0

# Erro NameError ocorre quando utilizamos uma variavel que nao
# foi inicializada
# Ex.: divisao = numero/100

# Erro TypeError ocorre quando tentamos operar sobre dois
# valores de tipos diferentes
# soma = "1" + 1

"""Questao 3"""
lista = []
valor = 10


class ListaVazia(Exception):
    pass


class ValorNaoEncontrado(Exception):
    pass


class ValorImprar(Exception):
    pass


class ValorNulo(Exception):
    pass


try:
    if not len(lista):
        raise ListaVazia("Lista vazia!")
    elif valor not in lista:
        raise ValorNaoEncontrado("Valor Não Encontrado!")
    elif valor % 2 == 1:
        raise ValorImprar("Valor Impar!")
    elif valor <= 0:
        raise ValorNulo("Valor Nulo!")

except ListaVazia as e:
    print(f"Erro: {e}")
except ValorNaoEncontrado as e:
    print(f"Erro: {e}")
except ValorImprar as e:
    print(f"Erro: {e}")
except ValorNulo as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro: {e}")
