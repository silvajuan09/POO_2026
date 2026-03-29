import math
def Diagonal(b, h):
    diagsqrd = b**2 + h**2
    return math.sqrt(diagsqrd)

print('Digite os lados do retângulo:')
a = float(input())
b = float(input())
diag = Diagonal(a, b)
print(f'A diagonal do retângulo mede {diag:.2f}')