import enum 

class Estacao(enum.Enum):
    OUTONO = 1
    INVERNO = 2
    PRIMAVERA = 3
    VERAO = 4

a = Estacao.INVERNO     # atributo
b = Estacao["OUTONO"]   #lista
c = Estacao(3)          #valor
print(a)
print(b)
print(c)
print(c.name)      # retorna apenas o nome
print(c.value)     # retorna o valor associado