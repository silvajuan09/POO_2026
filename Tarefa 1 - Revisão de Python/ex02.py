print('Digite dois valores inteiros separados por um operador +, -, * ou /')
txt = input()
operadores = "+-*/"
for op in operadores:
    if op in txt:
        partes = txt.split(op)
        valor1 = int(partes[0])
        valor2 = int(partes[1])
        operador = op
        break
if operador == '+':
    resultado = valor1 + valor2
elif operador == '-':
    resultado = valor1 - valor2
elif operador == '*':
    resultado = valor1 * valor2
else:
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        resultado = 'Divisão inválida'

print(f'Resultado: {resultado}')
