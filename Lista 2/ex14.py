def MMC(x, y):
    maior = max(x, y)
    while True:
        if maior % x == 0 and maior % y == 0:
            return maior
        maior += 1
print('Digite os valores para MMMC')
a = int(input())
b = int(input())
resultado = MMC(a,b)
print(f'O MMC entre {a} e {b} é {resultado}')