class País:
    def __init__(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0
    def calc_densidade(self):
        return self.populacao / self.area

pais = País()
pais.nome = input("Digite o nome do país: ")
pais.populacao = int(input("Digite sua população: "))
pais.area = float(input("Digite a área em km2: "))
densidade = pais.calc_densidade()
print(f'A densidade demográfica de {pais.nome} é de {densidade:.2f} hab/km2')