import os


def limpatela():
    os.system("clear" if os.name == "posix" else "cls")


# class Livro:
#     def __init__(self, titulo, autor, ano) -> None:
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano

#     def __str__(self):
#         return f"Livro: {self.titulo}, Autor:{self.autor}, Ano de Publicação:{self.ano}"


# class Biblioteca:
#     def __init__(self) -> None:
#         self.livros = set()
#         self.index = 0

#     def adicionarLivro(self, livro: Livro) -> None:
#         self.livros.add(livro)

#     def emprestarLivro(self) -> Livro:
#         return self.livros.pop()

#     def devolverLivro(self, livro: Livro) -> Livro:
#         return self.adicionarLivro(livro)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.livros):
#             saida = list(self.livros)[self.index]
#             self.index += 1
#             return saida
#         else:
#             self.index = 0
#             raise StopIteration

#     def __str__(self) -> str:
#         if len(self.livros) == 0:
#             return f"Livraria Vazia!"
#         return f"Existem {len(self.livros)} Livros disponiveis."


# class Leitor:
#     def __init__(self):
#         self.livro = None

#     def pegarlivro(self, biblioteca: Biblioteca) -> None:
#         if self.livro == None:
#             self.livro = biblioteca.emprestarLivro()
#         else:
#             print(f"Atualmente possuo um livro, e é o maximo que consigo ler por vez.")

#     def devolverLivro(self, biblioteca: Biblioteca) -> None:
#         if self.livro == None:
#             print("Não possuo livros para devolver.")
#         else:
#             biblioteca.devolverLivro(self.livro)
#             self.livro = None

#     def __str__(self) -> None:
#         if self.livro == None:
#             return "Atualmente não estou lendo nada, me recomenda algo?"
#         else:
#             return f"Atualmente estou lendo {self.livro.titulo} de {self.livro.autor}, estou adorando e recomendo!"


# # testes
# limpatela()

# livro1 = Livro("Harry Potter e a Ordem da Fenix", "JK Rowling", 2003)
# livro2 = Livro("Harry Potter e o Enigma do Principe", "JK Rowling", 2005)
# livro3 = Livro("Harry Potter e a As Reliquias da Morte", "JK Rowling", 2007)


# print(livro1)
# print(livro2)
# print(livro3)


# biblioteca1 = Biblioteca()
# biblioteca1.adicionarLivro(livro1)
# biblioteca1.adicionarLivro(livro2)
# biblioteca1.adicionarLivro(livro3)

# print(biblioteca1)

# leitor1 = Leitor()
# leitor1.pegarlivro(biblioteca1)

# print(leitor1)
# print(biblioteca1)

# leitor1.devolverLivro(biblioteca1)
# print(biblioteca1)

# for livro in biblioteca1:
#     print(livro)
