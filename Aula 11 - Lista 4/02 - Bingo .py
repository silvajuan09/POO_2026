class Bingo:
    def __init__(self, numBolas, bolas):
        self.__numBolas = 0
        self.__bolas = []
    def set_numBolas(self, numBolas):
        if numBolas <= 0: raise ValueError('O número deve ser positivo')
        self.__numBolas = numBolas
    def set_bolas(self, bolas):
        if isinstance(bolas, list): raise ValueError('O número deve ser positivo')
        self.__bolas = bolas