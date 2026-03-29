def MenorInteiro(x):
    int = x // 1 + 1
    if x.is_integer():
        int -= 1
    return int
print('Digite o número real desejado')
a = float(input())
calc = MenorInteiro(a)
print(f'O menor inteiro maior ou igual ao seu número real é igual a {calc}')