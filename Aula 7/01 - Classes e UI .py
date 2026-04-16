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
    
class Viagem():
    def __init__(self):
        self.__distancia = 0.0
        self.__horas = 0.0
        self.__minutos = 0.0
        self.__tempo = self.__horas + self.__minutos / 60
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()
    def set_tempo(self, t):
        if t >= 0: self.__tempo = t
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo


# Interface com o usuário
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()

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
        x.set_distancia(float(input('Distância (km): ')))
        x.set_distancia(float(input(': ')))

UI.main()