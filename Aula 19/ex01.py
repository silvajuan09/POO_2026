class Funcionario:
    def __init__(self, nome, salario_base):
        self.__nome = nome
        self.__salario_base = salario_base
    def get_nome(self):
        return self.__nome
    def get_salario(self):
        return self.__salario_base
    def __str__(self):
        return f"Nome: {self.__nome}, Salário Base: {self.__salario_base}"

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, gratificacao):
        super().__init__(nome, salario_base)
        self.__gratificacao = gratificacao
    def get_salario(self):
        return super().get_salario() + self.__gratificacao
    def __str__(self):
        return f"Nome: {self.get_nome()}, Salário Total: {self.get_salario()}"

x = Funcionario("João", 5000)
print(x.get_nome())
print(x.get_salario())
print(x.__str__())

y = Gerente("Maria", 6000, 2000)
print(y.get_nome())
print(y.get_salario())
print(y.__str__())