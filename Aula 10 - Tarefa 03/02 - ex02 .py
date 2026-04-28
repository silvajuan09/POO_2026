class Pais:
    def __init__(self, n, p, a):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)
    def set_nome(self, nome):
        if nome != "": self.__nome = nome
        else: raise ValueError()
    def set_populacao(self, v):
        if v >= 0: self.__populacao = v
        else: raise ValueError()
    def set_area(self, v):
        if v > 0: self.__area = v
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__populacao / self.__area
    def __str__(self):
        return (f"Nome: {self.__nome}\n" 
            f"População: {self.__populacao}\n"
            f"Área: {self.__area} km²\n"
            f"Densidade demográfica: {self.densidade():.2f} hab/km²")

class PaisUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = PaisUI.menu()
            if op == 1: PaisUI.calculo()
    @staticmethod
    def menu():
        print("1-Calcular 2-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    
    @staticmethod
    def calculo():
        print("Cálculo da densidade demográfica")
        n = input("Informe o nome do país: ")
        p = int(input("Informe a população: "))
        a = float(input("Informe a área (km²): "))
        x = Pais(n, p, a)
        print(x)
PaisUI.main()