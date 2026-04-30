class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)         # atributo de instância
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self, id):
        if id < 0: raise ValueError('ID deve ser positivo')
        self.__id = id
    def set_nome(self, nome):
        if nome == '': raise ValueError('Nome não pode ser vazio')
        self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self): return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ContatoUI:
    contatos = []       # atributo de classe
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()

    @staticmethod
    def menu():
        print('1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Pesquisar 6-Fim')
        return int(input('Informe uma opção: '))
    
    @classmethod
    def inserir(cls):
        id = int(input('Informe o ID do contato: '))
        nome = input('Informe o nome: ')
        email = input('Informe o email: ')
        fone = input('Informe o telefone: ')
        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)
    
    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0: print('Nenhum contato cadastrado')
        else:
            for x in cls.contatos: print(x)
    
    @classmethod
    def atualizar(cls):
        id = int(input('Informe o ID do contato: '))
        if id in cls.contatos:
            i = 0
            for id in cls.contatos:
                nome = input('Informe o nome: ')
                email = input('Informe o email: ')
                fone = input('Informe o telefone: ')
                x = Contato(id, nome, email, fone)
                cls.contatos[i] = x
                i += 1
        else: print('Contato inexistente')

    @classmethod
    def excluir(cls):
        if len(cls.contatos) == 0: print('Nenhum contato cadastrado')
        else:
            for x in cls.contatos: print(x)

        id = int(input('Informe o ID do contato: '))
        if id in cls.contatos:
            i = 0
            for id in cls.contatos:
                del cls.contatos[i]
                i += 1
        else: print('Contato inexistente')

    @classmethod
    def pesquisar(cls):
        id = int(input('Informe o ID do contato: '))
        if id in cls.contatos:
            i = 0
            for id in cls.contatos:
                print(cls.contatos[i])
                i += 1
        else: print('Contato inexistente')

    
ContatoUI.main()