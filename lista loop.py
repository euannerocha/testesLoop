# FOR
# lista = [2, 4, 6, 8, 9, 10, 12, 13]

# for n in lista:
#     if n % 2 != 0:
#         continue
#     elif n == 6:
#         continue
#     elif n == 8:
#         continue
#     else:
#         print(n)

# print("Deu tudo certo!")

# def calcula(x):
#     pass

#WHILE
# variavel = 1
# lista = [1, 2, 3]

# while variavel <= 10:
#     print(variavel)
#     variavel += 1
#     lista.append(variavel)

# print(lista)



# lista = [2, 4, 6, 8, 9, 10, 12, 13]
# tupla = (2, 4, 6, 8, 10, 12, 13)


# print("Hello World!")


# def maiorValor(n):
#     lista = []
#     for i in range (0, n):
#         lista.append(input("Digite um valor: "))
#     print(lista)

# maiorValor(3)

#BHASKARA


a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

pt1 = b*(-1)
delta = ((b**2) - 4*a*c)**(1/2)
div = 2*a

xLinha = (pt1 + delta)/div
xDuasLinhas = (pt1 - delta)/div

print(f"{xLinha:.4f}, {xDuasLinhas:.4f}")
print("{:.4f}, {:.4f}".format(xLinha, xDuasLinhas))

