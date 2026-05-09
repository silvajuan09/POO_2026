class Times:
    def __init__(self, id, nome, estado):
        self.set_id(id)         
        self.set_nome(nome)
        self.set_estado(estado)
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

class Jogadores:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id)         
        self.set_idTime(idTime)         
        self.set_nome(nome)
        self.set_camisa(camisa)
    def set_id(self, id):
        if id < 0: raise ValueError('ID deve ser positivo')
        self.__id = id
    def set_idTime(self, idTime):
        if idTime < 0: raise ValueError('O ID do time deve ser positivo')
        self.__idTime = idTime
    def set_nome(self, nome):
        if nome == '': raise ValueError('Nome não pode ser vazio')
        self.__nome = nome
    def set_camisa(self, camisa): 
        if len(camisa) < 2: raise ValueError('Preencha ao menos 2 caracteres')
        self.__camisa = camisa
    def get_id(self): return self.__id
    def get_idTime(self): return self.__idTime
    def get_nome(self): return self.__nome
    def get_camisa(self): return self.__camisa
    def __str__(self): return f"{self.__id} - {self.__idTime}- {self.__nome} - {self.__camisa}"


class TimesUI:
    times = []   
    jogadores = []    
    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = TimesUI.menu()
            if op == 1: TimesUI.inserir_time()
            if op == 2: TimesUI.listar_times()
            if op == 3: TimesUI.atualizar_time()
            if op == 4: TimesUI.excluir_time()
            if op == 5: TimesUI.inserir_jogador()
            if op == 6: TimesUI.listar_jogadores()
            if op == 7: TimesUI.atualizar_jogador()
            if op == 8: TimesUI.excluir_jogador()
            if op == 9: TimesUI.listar_jogadores_do_time()
            if op == 10: TimesUI.transferir_jogador()

    @staticmethod
    def menu():
        print('1-Inserir time 2-Listar times 3-Atualizar times 4-Excluir time 5-Inserir jogador 6-Listar jogadores 7-Atualizar jogador 8-Excluir jogador 9-Listar jogadores de um time 10-Transferir jogador entre times 11-Fim')
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
    def listar_id(cls, id):      
        for x in cls.times:
            if x.get_id() == id: return x
        return None 

    @classmethod
    def atualizar_time(cls):
        TimesUI.listar_times()
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
    
    @classmethod
    def excluir_time(cls):
        TimesUI.listar_times()
        id = int(input('Informe o id do time a ser excluído: '))
        x = TimesUI.listar_id(id)
        if x != None:
            cls.times.remove(x)
        else:
            print('Esse time não existe')

    @classmethod
    def inserir_jogador(cls):
        id = int(input('Informe o ID do jogador: '))
        idTime = int(input('Informe o ID do time do jogador: '))
        nome = input('Informe o nome do jogador: ')
        camisa = input('Informe a camisa do jogador: ')
        x = Jogadores(id, idTime, nome, camisa)
        cls.jogadores.append(x)

    @classmethod
    def listar_jogadores(cls):
        if len(cls.jogadores) == 0: print('Nenhum jogador inserido')
        else:
            for x in cls.jogadores: print(x)
    
    @classmethod
    def atualizar_jogador(cls):
        TimesUI.listar_jogadores()
        id = int(input("Informe o id do jogador a ser atualizado: "))

        for j in cls.jogadores:
            if j.get_id() == id:
                cls.jogadores.remove(j)
                nome = input("Informe o novo nome: ")
                idTime = int(input("Informe o novo ID do time: "))
                camisa = input("Informe o novo camisa: ")
                x = Jogadores(id, idTime, nome, camisa)
                cls.jogadores.append(x)
                return
        print("Jogador não encontrado")
        
    @classmethod
    def excluir_jogador(cls):
        TimesUI.listar_jogadores()
        id = int(input('Informe o id do jogador a ser excluído: '))

        for j in cls.jogadores:
            if j.get_id() == id:
                cls.jogadores.remove(j)
                print('Jogador excluído')
                return
        print('Esse jogador não existe')

    @classmethod
    def listar_jogadores_do_time(cls):
        idTime = int(input('Informe o ID do time: '))
        for j in cls.jogadores:
            if j.get_idTime() == idTime:
                print(j)
    
    @classmethod
    def transferir_jogador(cls):
        TimesUI.listar_jogadores()
        id = int(input("Informe o id do jogador a ser transferido: "))
        idTime = int(input('Informe o novo ID do time: '))

        for j in cls.jogadores:
            if j.get_id() == id:
                j.set_idTime(idTime)
                print('Jogador transferido')
                return
        print('Jogador não encontrado')