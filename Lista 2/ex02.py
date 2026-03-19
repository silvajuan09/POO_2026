print("Informe o número do mês")
num_mes = int(input())
match num_mes:
    case 1: mes = "janeiro"
    case 2: mes = "fevereiro"
    case 3: mes = "março"
    case 4: mes = "abril"
    case 5: mes = "maio"
    case 6: mes = "junho"
    case 7: mes = "julho"
    case 8: mes = "agosto"
    case 9: mes = "setembro"
    case 10: mes = "outubro"
    case 11: mes = "novembro"
    case 12: mes = "dezembro"
    case _:
        print("Mês inválido") 
        exit()

if mes == "janeiro" or mes == "fevereiro" or mes == "março":
    trimestre = "primeiro"
elif mes == "abril" or mes == "maio" or mes == "junho":
    trimestre = "segundo"
elif mes == "julho" or mes == "agosto" or mes == "setembro":
    trimestre = "terceiro"
elif mes == "outubro" or mes == "novembro" or mes == "dezembro":
    trimestre = "quarto"

print(f'O mês de {mes} é do {trimestre} trimestre do ano')