from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_listar_nome()
            if op == 4: UI.cliente_atualizar()
            if op == 5: UI.cliente_excluir()
            if op == 6: UI.servico_inserir()
            if op == 7: UI.servico_listar()
            if op == 8: UI.servico_listar_descricao()
            if op == 9: UI.servico_atualizar()
            if op == 10: UI.servico_excluir()

    @staticmethod
    def menu():
        print("\n----- MENU -----")
        print("1-Inserir Cliente")
        print("2-Listar Clientes")
        print("3-Pesquisar Cliente por Nome")
        print("4-Atualizar Cliente")
        print("5-Excluir Cliente")
        print("6-Inserir Serviço")
        print("7-Listar Serviços")
        print("8-Pesquisar Serviço por Descrição")
        print("9-Atualizar Serviço")
        print("10-Excluir Serviço")
        print("0-Sair")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(0, nome, email, fone)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar():
            print(obj)

    @staticmethod
    def cliente_listar_nome():
        iniciais = input("Informe as iniciais do nome: ")
        resultado = Service.cliente_listar_nome(iniciais)
        if resultado:
            for obj in resultado:
                print(obj)
        else:
            print("Nenhum cliente encontrado.")

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar():
            print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar():
            print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    

    @staticmethod
    def servico_inserir():
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(0, descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar():
            print(obj)

    @staticmethod
    def servico_listar_descricao():
        iniciais = input("Informe as iniciais da descrição: ")
        resultado = Service.servico_listar_descricao(iniciais)
        if resultado:
            for obj in resultado:
                print(obj)
        else:
            print("Nenhum serviço encontrado.")

    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar():
            print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor: "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar():
            print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

UI.main()