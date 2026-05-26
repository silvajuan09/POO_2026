from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)         
        self.set_data(data)         
        self.set_distancia(distancia)         
        self.set_tempo(tempo)
    def set_id(self, id):
        if id < 0: raise ValueError('ID deve ser positivo')
        self.__id = id
    def set_data(self, data):
        if data == '': raise ValueError('Data não pode ser vazio')
        self.__data = data
    def set_distancia(self, distancia): 
        if distancia < 0: raise ValueError('Distância deve ser positiva')
        self.__distancia = distancia
    def set_tempo(self, tempo): 
        if tempo < 0: raise ValueError('Tempo deve ser positivo')
        self.__tempo = tempo
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo
    def pace(self): return self.__tempo / self.__distancia
    def __str__(self): return f"{self.__id} - {self.__data} - {self.__distancia} - {self.__tempo}"


class TreinoUI:   
    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.listar_id()
            if op == 4: TreinoUI.atualizar()
            if op == 5: TreinoUI.excluir()
            if op == 6: TreinoUI.mais_rapido()

    @staticmethod
    def menu():
        print('1-Inserir time 2-Listar times 3-Atualizar times 4-Excluir time 5-Inserir jogador 6-Listar jogadores 7-Atualizar jogador 8-Excluir jogador 9-Listar jogadores de um time 10-Transferir jogador entre times 11-Fim')
        return int(input('Informe uma opção: '))
    
    @classmethod
    def inserir_time(cls):
        id = int(input('Informe o ID do time: '))
        nome = input('Informe o nome do time: ')
        estado = input('Informe o estado de origem do time: ')
        x = Time(id, nome, estado)
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
        TimeUI.listar_times()
        id = int(input("Informe o id do time a ser atualizado: "))
        x = TimeUI.listar_id(id)
        if x is not None:   
            nome = input("Informe o novo nome: ")
            x.set_nome(nome)
            estado = input("Informe o novo estado: ")
            x.set_estado(estado)
        else:
            print("Esse time não existe") 
    
    @classmethod
    def excluir_time(cls):
        TimeUI.listar_times()
        id = int(input('Informe o id do time a ser excluído: '))
        x = TimeUI.listar_id(id)
        if x != None:
            cls.times.remove(x)
        else:
            print('Esse time não existe')

    @classmethod
    def inserir_jogador(cls):
        id = int(input('Informe o ID do jogador: '))
        idTime = int(input('Informe o ID do time do jogador: '))
        nome = input('Informe o nome do jogador: ')
        camisa = int(input('Informe a camisa do jogador: '))
        x = Jogador(id, idTime, nome, camisa)
        cls.jogadores.append(x)

    @classmethod
    def listar_id_jogador(cls, id):
        for j in cls.jogadores:
            if j.get_id() == id:
                return j
        return None
    
    @classmethod
    def listar_jogadores(cls):
        if len(cls.jogadores) == 0: print('Nenhum jogador inserido')
        else:
            for x in cls.jogadores: print(x)
    
    @classmethod
    def atualizar_jogador(cls):
        TimeUI.listar_jogadores()
        id = int(input("Informe o id do jogador a ser atualizado: "))
        j = TimeUI.listar_id_jogador(id)
        if j is not None:   
            nome = input("Informe o novo nome: ")
            idTime = int(input("Informe o novo ID do time: "))
            camisa = int(input("Informe o novo camisa: "))

            j.set_nome(nome)
            j.set_idTime(idTime)
            j.set_camisa(camisa)
        else:
            print("Jogador não encontrado") 
        
    @classmethod
    def excluir_jogador(cls):
        TimeUI.listar_jogadores()
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
        TimeUI.listar_jogadores()
        id = int(input("Informe o id do jogador a ser transferido: "))
        idTime = int(input('Informe o novo ID do time: '))

        for j in cls.jogadores:
            if j.get_id() == id:
                j.set_idTime(idTime)
                print('Jogador transferido')
                return
        print('Jogador não encontrado')

TimeUI.main()