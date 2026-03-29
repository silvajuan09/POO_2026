def RemoverEspacos(texto):
    return " ".join(texto.split())

print('Digite seu texto:')
texto = input()
print(RemoverEspacos(texto))