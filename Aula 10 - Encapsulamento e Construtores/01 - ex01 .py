class Viagem:
    def __init__(self, dest, dist, lt):
        self.set_destino(dest)
        self.set_distancia(dist)
        self.set_litros(lt)
    def set_destino(self, nome):
        if nome != "": self.__destino = nome
        else: raise ValueError()
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()
    def set_litros(self, l):
        if l > 0: self.__litros = l
        else: raise ValueError()
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia / self.__litros
    def __str__(self):
        return (f"Destino: {self.__destino}\n" 
            f"Distância: {self.__distancia} km\n"
            f"Litros: {self.__litros} L\n"
            f"Consumo: {self.consumo()} km/L")

class ViagemUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1: ViagemUI.calculo()
    @staticmethod
    def menu():
        print("1-Calcular 2-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    
    @staticmethod
    def calculo():
        print("Cálculo do consumo de combustível")
        dest = input("Informe o destino: ")
        dist = float(input("Informe a distância (km): "))
        lt = float(input("Informe a quantidade de litros: "))
        x = Viagem(dest, dist, lt)
        print(x)
ViagemUI.main()