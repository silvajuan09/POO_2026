#Entidades
class Aluno:
    def __init__(self):
        self.__nome = " "                # Atributos escondidos
        self.__matricula = " "
    def set_nome(self, valor):           # Método
        if len(valor) < 3: raise ValueError("Nome deve ter pelo menos 2 letras")
        self.__nome = valor
    def get_nome(self):
        return self.__nome
    def set_matricula(self, valor):
        if len(valor) < 5: raise ValueError("Nome deve ter pelo menos 5 caracteres")
        self.__matricula = valor
    def get_matricula(self):
        return self.__matricula
    def ano_ingresso(self):
        return int(self.__matricula[:4])

class UI:
    #Programa Principal
    x = Aluno()
    #x.nome = input("Informe o nome:")
    x.set_nome = input("Informe o nome:")
    #x.matricula = input("Informe o nome:")
    x.set_matricula = input("Informe o nome:")
    ano = x.ano_ingresso()
    print(f'O aluno {x.get_nome()}, de matrícula {x.get_matricula()}')
    print(f'Entrou no IF em {ano}')
    
UI.main()