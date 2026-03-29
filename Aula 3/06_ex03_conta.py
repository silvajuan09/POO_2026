class ContaBancaria:
    def __init__ (self):
        self.nome = 0
        self.num = 0
        self.saldo = 0
    def calc_deposito(self):
        self.deposito = float(input('Digite o valor do depósito: '))
        self.saldo += self.deposito
    def calc_saque(self):
        self.saque = float(input('Digite o valor do saque: '))
        self.saldo -= self.saque
    
conta = ContaBancaria()
conta.nome = input('Digite o nome do titular: ')
conta.num = int(input('Digite o número da conta: '))
conta.saldo = float(input('Digite o saldo da conta: '))
deposito = conta.calc_deposito()
print(conta.saldo)
saque = conta.calc_saque()
print(conta.saldo)