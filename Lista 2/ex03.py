print('Digite quatro valores inteiros diferentes')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==b or a==c or a==d or b==c or b==d or c==d:
    print("Os valores devem ser diferentes")
    exit()
else:
    if a>b and a>c and a>d:
        maior = a
        print(f'Maior valor: {maior}')
    elif b>a and b>c and b>d:
        maior = b
        print(f'Maior valor: {maior}')
    elif c>a and c>b and c>d:
        maior = c
        print(f'Maior valor: {maior}')
    else:
        maior = d
        print(f'Maior valor: {maior}')

    if a<b and a<c and a<d:
        menor = a
        print(f'Menor valor: {menor}')
    elif b<a and b<c and b<d:
        menor = b
        print(f'Menor valor: {menor}')
    elif c<a and c<b and c<d:
        menor = c
        print(f'Menor valor: {menor}')
    else:
        menor = d
        print(f'Menor valor: {menor}')

    if a == maior and b == menor or a == menor and b == maior:
        print(f'A soma do segundo maior valor com o segundo menor = {c+d}')
    elif a == maior and c == menor or a == menor and c == maior:
        print(f'A soma do segundo maior valor com o segundo menor = {b+d}')
    elif a == maior and d == menor or a == menor and d == maior:
        print(f'A soma do segundo maior valor com o segundo menor = {b+c}')
    elif b == maior and c == menor or c == maior and b == menor:
        print(f'A soma do segundo maior valor com o segundo menor = {a+d}')
    elif b == maior and d == menor or d == maior and b == menor:
        print(f'A soma do segundo maior valor com o segundo menor = {a+c}')
    elif c == maior and d == menor or d == maior and c == menor:
        print(f'A soma do segundo maior valor com o segundo menor = {a+b}')
        