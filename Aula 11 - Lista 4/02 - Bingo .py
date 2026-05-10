import random
class Bingo:
    def __init__(self, numBolas):
        self.set_numBolas(numBolas)
    def set_numBolas(self, numBolas):
        if numBolas <= 0: raise ValueError('O número deve ser positivo')
        self.__numBolas = numBolas
    def get_numBolas(self): return self.__numBolas

class BingoUI:
    bolas = []
    bingo = None
    @staticmethod
    def main():
        op = 0
        while op != 4:
            if op == 1: BingoUI.iniciar_jogo()
            if op == 2: BingoUI.sortear()
            if op == 3: BingoUI.sorteados()
    
    @staticmethod
    def menu():
        print('''
        1 - Iniciar Jogo
        2 - Sortear número
        3 - Verificar sorteados
        4 - Sair
        ''')    
        return int(input('Escolha uma opção: '))
    
    @classmethod
    def iniciar_jogo(cls):
        numBolas = int(input('Defina o número de bolas do jogo: '))
        cls.bingo = Bingo(numBolas)
    
    @classmethod
    def sortear(cls):
        if cls.bingo == None:
            print('Inicie um jogo primeiro')
            return
        
        if len(cls.bolas) == cls.bingo.get_numBolas():
            print('Todas as bolas já foram sorteadas')
            return

        while x in cls.bolas:
            x = random.randint(1, cls.bingo.get_numBolas())
            
        cls.bolas.append(x)
        print(f'Número sorteado: {x}')
    
    @classmethod
    def sorteados(cls):
        if cls.bingo == None:
            print('Inicie um jogo primeiro')
            return
        print(cls.bolas)
    
BingoUI.main()