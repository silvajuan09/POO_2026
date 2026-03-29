print('Digite uma frase:')
frase = input()
lista = list(frase)

for i in lista:
    lista.append(lista.pop(0))
    palavra = "".join(lista)
    print(palavra)