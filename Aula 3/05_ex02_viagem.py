class Viagem:
    def __init__(self):
        self.distancia = 0
        self.horas = 0
        self.minutos = 0
    def calc_v_media(self):
        self.tempo = self.horas + self.minutos / 60
        return self.distancia / self.tempo
    
x = Viagem()
print("Informe a distância da viagem")
x.distancia = float(input())
print("Informe o tempo (horas e minutos) da viagem")
x.horas = int(input())
x.minutos = int(input())
a = x.calc_v_media()
print(f"A velocidade média da viagem foi de {a:.2f}km/h")