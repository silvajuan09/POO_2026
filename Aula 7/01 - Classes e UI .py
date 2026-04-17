import math

# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h /2

class Circulo:
    def __init__(self):
        self.__r = 0.0
    def set_raio(self, v):
        if v >= 0: self.__r = v
        else: raise ValueError()
    def get_raio(self):
        return self.__r
    def calc_area(self):
        return math.pi * self.__r ** 2
    def calc_circunferencia(self):
        return 2 * math.pi * self.__r
    
class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()
    def set_tempo(self, t):
        if t >= 0: self.__tempo = t
        else: raise ValueError()
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo
    
class Conta_Bancaria:
    def __init__(self):
        self.__nome = ""
        self.__numero = ""
        self.__saldo = 0.0
    def set_nome(self, nome):
        if nome != "": self.__nome = nome
        else: raise ValueError()
    def set_numero(self, num):
        if num >= 0: self.__numero = num
        else: raise ValueError()
    def set_saldo(self, valor):
        if valor >= 0: self.__saldo = valor
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
        else: raise ValueError()
    def saque(self, valor):
        if valor > 0:
            self.__saldo -= valor
        else: raise ValueError()

class Entrada_Cinema:
    def __init__(self):
        self.__dia = ""
        self.__horario = ""
        self.__ing_base = 0.0
        self.__ingresso = 0.0
    def set_dia(self, dia):
        match dia:
            case 'Segunda': self.__dia = dia
            case 'Terça': self.__dia = dia
            case 'Quarta': self.__dia = dia
            case 'Quinta': self.__dia = dia
            case 'Sexta': self.__dia = dia
            case 'Sábado': self.__dia = dia
            case 'Domingo': self.__dia = dia
            case _: raise NameError
    def set_horario(self, horario):
        if 0 <= horario <= 24:
            self.__horario = horario
        else: raise ValueError
    def get_dia(self):
        return self.__dia
    def get_horario(self):
        return self.__horario
    def calc_ingresso(self):
        match self.__dia:
            case 'Segunda': self.__ing_base = 16
            case 'Terça': self.__ing_base = 16
            case 'Quarta': self.__ingresso = 8
            case 'Quinta': self.__ing_base = 16
            case 'Sexta': self.__ing_base = 20
            case 'Sábado': self.__ing_base = 20
            case 'Domingo': self.__ing_base = 20
        if 17 <= self.__horario <= 24 and self.__dia != 'Quarta':
            self.__ingresso += self.__ing_base/2
        else:
            self.__ingresso = self.__ing_base
        return self.__ingresso

# Interface com o usuário
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()

    @staticmethod
    def menu():
        print("1-Triângulo, 2-Círculo, 3-Viagem, 4-Conta Bancária, 5-Ingresso, 9-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    
    @staticmethod
    def triangulo():
        print("Cálculo da área de um triângulo")
        x = Triangulo()
        x.set_base(float(input('Base: ')))
        x.set_altura(float(input('Altura: ')))
        area = x.calc_area()
        print(f'Um triângulo com a base {x.get_base()} e altura {x.get_altura()} tem área = {area}')

    @staticmethod
    def circulo():
        print('Cálculo da área de um círculo e comprimento da circunferência')
        x = Circulo()
        x.set_raio(float(input('Raio: ')))
        area = x.calc_area()
        circunferencia =  x.calc_circunferencia()
        print(f'Um círculo de raio {x.get_raio} tem área = {area} e circunferência = {circunferencia}')

    @staticmethod
    def viagem():
        print('Cálculo da velocidade média de uma viagem')
        x = Viagem()
        x.set_distancia(float(input('Digite a distância em km: ')))
        x.set_tempo(float(input('Digite o tempo em horas (1h30 = 1.5): ')))
        velocidade_media = x.velocidade_media()
        print(f'A velocidade média da viagem foi de {velocidade_media}km/h')

    @staticmethod
    def conta_bancaria():
        print('Conta bancária e operações')
        x = Conta_Bancaria()
        x.set_nome(input('Nome do titular: '))
        x.set_numero(input('Número da conta: '))
        print(f'Saldo atual: {x.get_saldo}')
        op = int(input("1 - Depositar, 2 - Sacar: "))
        if op==1:
            valor = float(input('Valor do depósito: '))
            x.deposito(valor)
        elif op==2:
            valor = float(input('Valor do saque: '))
            x.saque(valor)
        print(f'Saldo atual: {x.get_saldo}')
    
    @staticmethod
    def ing_cinema():
        print('Valor da entrada do cinema')
        x = Entrada_Cinema()
        x.set_dia(input('Dia (inicial maiúsucla): '))
        x.set_horario(int(input('Horário (0 a 24): ')))
        valor = x.calc_ingresso()
        print(f'O valor do ingresso é de R${valor}')

UI.main()