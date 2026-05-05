class Times:
    def __init__(self, id, nome, estado):
        self.set_id(id)         
        self.set_nome(nome)
        self.set_email(estado)
    def set_id(self, id):
        if id < 0: raise ValueError('ID deve ser positivo')
        self.__id = id
    def set_nome(self, nome):
        if nome == '': raise ValueError('Nome não pode ser vazio')
        self.__nome = nome
    def set_estado(self, estado): 
        if len(estado) < 2: raise ValueError('Preencha ao menos 2 caracteres')
        self.__estado = estado
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado(self): return self.__estado
    def __str__(self): return f"{self.__id} - {self.__nome} - {self.__estado}"

class TimesUI:
    times = []       # atributo de classe
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = TimesUI.menu()
            if op == 1: TimesUI.inserir()
            if op == 2: TimesUI.listar()
            if op == 3: TimesUI.atualizar()
            if op == 4: TimesUI.excluir()

    @staticmethod
    def menu():
        print('1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Fim')
        return int(input('Informe uma opção: '))
    
    @classmethod
    def inserir_time(cls):
        id = int(input('Informe o ID do time: '))
        nome = input('Informe o nome do time: ')
        estado = input('Informe o estado de origem do time: ')
        x = Times(id, nome, estado)
        cls.times.append(x)
    
    @classmethod
    def listar_times(cls):
        if len(cls.times) == 0: print('Nenhum time cadastrado')
        else:
            for x in cls.times: print(x)

    @classmethod
    def atualizar(cls):
        TimesUI.listar()
        id = int(input("Informe o id do time a ser atualizado: "))
        x = TimesUI.listar_id(id)
        if x != None:
            cls.times.remove(x)
            nome = input("Informe o novo nome: ")
            estado = input("Informe o novo estado: ")
            x = Times(id, nome, estado)
            cls.times.append(x)
        else:
            print("Esse time não existe") 