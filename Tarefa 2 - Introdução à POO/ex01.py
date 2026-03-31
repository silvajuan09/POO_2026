class Agua:
    def __init__ (self):
        self.mes = 0
        self.ano = 0
        self.consumo = 0
    def calc_conta (self):
        if self.consumo < 0:
            print('Consumo inválido!')
        elif 0 <= self.consumo <= 10:
            self.conta = 38
            return self.conta
        elif 11 <= self.consumo <= 20:
            self.conta = 38 + (self.consumo-10)*5
            return self.conta
        elif 21 <= self.consumo:
            self.conta = 38 + 10*5 + (self.consumo-20)*6
            return self.conta

conta_agua = Agua()
conta_agua.mes = 'Fevereiro'
conta_agua.ano = '1009'
conta_agua.consumo = 21
valor = conta_agua.calc_conta()
print(f'O valor da conta de água de {conta_agua.mes} de {conta_agua.ano} foi de R${valor}')