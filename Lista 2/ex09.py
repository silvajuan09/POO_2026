print('Digite uma frase:')
frase = input()
lista = frase.split()
for u in lista:
    print(u[::-1])
