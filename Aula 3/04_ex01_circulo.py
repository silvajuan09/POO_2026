import math
class Circulo:
    def __init__(self):
        self.r = 0
    def calc_area(self):
        return math.pi * self.r ** 2

x = Circulo()
print("Informe o raio do círculo" )
x.r = float(input())
a = x.calc_area()
print(f"A área do círculo é {a:.2f}")