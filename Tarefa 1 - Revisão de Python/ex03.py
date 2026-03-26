print('Digite uma frase')
frase = input()
lista = []
for num in frase:
    match num:
        case '0': lista.append(int(num))
        case '1': lista.append(int(num))
        case '2': lista.append(int(num))
        case '3': lista.append(int(num))
        case '4': lista.append(int(num))
        case '5': lista.append(int(num))
        case '6': lista.append(int(num))
        case '7': lista.append(int(num))
        case '8': lista.append(int(num))
        case '9': lista.append(int(num))
total = sum(lista)
print(total)