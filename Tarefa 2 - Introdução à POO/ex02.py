class País:
    def __init__(self):
        self.nome = input("Digite o nome do país: ")
        self.populacao =  int(input("Digite sua população: "))
        self.area = float(input("Digite a área em km2: "))
    def calc_densidade(self):
        return self.populacao / self.area

pais1 = País()
d1 = pais1.calc_densidade()

pais2 = País()
d2 = pais2.calc_densidade()

pais3 = País()
d3 = pais3.calc_densidade()

pais4 = País()
d4 = pais4.calc_densidade()

pais5 = País()
d5 = pais5.calc_densidade()

pais6 = País()
d6 = pais6.calc_densidade()

pais7 = País()
d7 = pais7.calc_densidade()

pais8 = País()
d8 = pais8.calc_densidade()

pais9 = País()
d9 = pais9.calc_densidade()

pais10 = País()
d10 = pais10.calc_densidade()

maior = max(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)
if maior == d1:
    maior_pais = pais1.nome
if maior == d2:
    maior_pais = pais2.nome
if maior == d3:
    maior_pais = pais3.nome
if maior == d4:
    maior_pais = pais4.nome
if maior == d5:
    maior_pais = pais5.nome
if maior == d6:
    maior_pais = pais6.nome
if maior == d7:
    maior_pais = pais7.nome
if maior == d8:
    maior_pais = pais8.nome
if maior == d9:
    maior_pais = pais9.nome
if maior == d10:
    maior_pais = pais10.nome
    
print(f'O país com maior densidade demográfica é {maior_pais}')
