print('Digite uma frase:')
frase = input()
lista = frase.split()
while lista:
    print(" ".join(lista))
    lista.pop(0)
    