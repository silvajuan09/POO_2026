print('Digite uma sequência de números separados por vírgula')
txt = input()
valores = txt.split(',')
i = 0
for num in valores:
    valores[i] = int(num)
    i = i + 1
total = sum(valores)
print(f'Soma = {total}')
