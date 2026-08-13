from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, fone, nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_fone(fone)
        self.set_nascimento(nascimento)
    def set_nome(self, nome):
        if nome == "": raise ValueError('Nome deve ser preenchido')
        self.__nome = nome
    def set_cpf(self, cpf):
        if len(cpf) != 11: raise ValueError('Preencha os 11 dígitos de CPF (apenas algarismos)')
        self.__cpf = cpf
    def set_fone(self, fone):
        if fone == "": raise ValueError('O telefone deve ser informado')
        self.__fone = fone
    def set_nascimento(self, nascimento):
        nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
        if nascimento > datetime.now(): raise ValueError('A data não pode estar no futuro')
        self.__nascimento = nascimento
    def get_nome(self): return self.__nome 
    def get_cpf(self): return self.__cpf
    def get_fone(self): return self.__fone
    def get_nascimento(self): return self.__nascimento
    def __str__(self): return f"{self.__nome} - {self.__cpf} - {self.__fone} - {self.__nascimento.strftime('%d/%m/%Y')}"
    def idade(self):
        hoje = datetime.now() - self.__nascimento
        dias = hoje.days
        anos = dias // 365
        meses = dias % 365 // 30
        return f"{anos} ano(s) e {meses} mes(es)"