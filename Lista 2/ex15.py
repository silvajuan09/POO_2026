def Primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1

num = int(input())
if Primo(num):
    print("É primo")
else:
    print("Não é primo")