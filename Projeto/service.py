from models.cliente import Cliente
from dao_sql.clientedao import ClienteDAO
from models.servico import Servico
from dao_sql.servicodao import ServicoDAO
from models.horario import Horario
from dao_sql.horariodao import HorarioDAO
from models.profissional import Profissional
from dao_sql.profissionaldao import ProfissionalDAO
from models.atendimento import Atendimento
from dao_sql.atendimentodao import AtendimentoDAO
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

class Service:
    @staticmethod
    def _validar_email_unico(email, id_cliente=None, id_profissional=None):
        if id_cliente is not None:
            cliente_atual = Service.cliente_listar_id(id_cliente)
            if cliente_atual != None:
                if cliente_atual.get_email() == "admin" and email != "admin":
                    raise ValueError("O e-mail do administrador não pode ser alterado")

        for cliente in Service.cliente_listar():
            if cliente.get_id() != id_cliente:
                if cliente.get_email() == email:
                    raise ValueError("E-mail já cadastrado para outro cliente")

        for profissional in Service.profissional_listar():
            if profissional.get_id() != id_profissional:
                if profissional.get_email() == email:
                    raise ValueError("E-mail já cadastrado para outro profissional")

    @staticmethod
    def cliente_inserir(nome, email, fone, senha, foto=None):
        obj = Cliente(0, nome, email, fone, senha, foto)
        Service._validar_email_unico(obj.get_email())
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        r = ClienteDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha, foto=None):
        atual = Service.cliente_listar_id(id)
        if foto is None and atual is not None:
            foto = atual.get_foto()

        obj = Cliente(id, nome, email, fone, senha, foto)
        Service._validar_email_unico(obj.get_email(), id_cliente=id)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        horarios = Service.horario_listar_cliente(id)
        if len(horarios) > 0: raise ValueError("Não é possível excluir um cliente com horário agendado")
        ClienteDAO().excluir(id)

    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin":
                return
        Service.cliente_inserir("admin", "admin", "fone", "1234")

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None


    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)

    @staticmethod
    def servico_listar():
        r = ServicoDAO().listar()
        r.sort(key = lambda obj : obj.get_descricao().casefold())
        return r

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)


    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)

        Service._validar_horario_unico(c.get_data(), c.get_id_profissional())

        HorarioDAO().inserir(c)

    @staticmethod
    def horario_listar():
        r = HorarioDAO().listar()
        r.sort(key = lambda obj : obj.get_data())

        return r

    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id)

    @staticmethod
    def _validar_horario_unico(data, id_profissional, id=None):
        if id_profissional in [None, 0]:
            return

        for horario in Service.horario_listar():
            if horario.get_id() != id:
                if horario.get_id_profissional() == id_profissional:
                    if horario.get_data() == data:
                        raise ValueError("Já existe um horário nessa data e hora para esse profissional")

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)

        Service._validar_horario_unico(c.get_data(), c.get_id_profissional(), id)

        HorarioDAO().atualizar(c)

    @staticmethod
    def horario_excluir(id):
        horario = Service.horario_listar_id(id)
        if horario != None:
            if horario.get_id_cliente() not in [None, 0]:
                raise ValueError("Não é possível excluir um horário ja agendado por um cliente.")
        HorarioDAO().excluir(id)

    @staticmethod
    def horario_abrir_agenda(inicio, fim, intervalo, id_profissional):

        agora = datetime.now(
            ZoneInfo("America/Sao_Paulo")
        ).replace(tzinfo=None)

        if inicio <= agora:
            raise ValueError("A agenda deve começar em uma data futura")

        if fim <= inicio:
            raise ValueError("O horário final deve ser maior que o inicial")

        if intervalo <= 0:
            raise ValueError("O intervalo deve ser positivo")

        existentes = Service.horario_listar_profissional(
            id_profissional
        )

        novos_horarios = []
        atual = inicio

        while atual < fim:

            for h in existentes:
                if h.get_data() == atual:
                    raise ValueError(
                        f"Já existe um horário em {atual:%d/%m/%Y %H:%M}"
                    )

            novos_horarios.append(atual)
            atual += timedelta(minutes=intervalo)

        for data in novos_horarios:
            Service.horario_inserir(
                data, False, None, None, id_profissional
            )

        return len(novos_horarios)

    # Lista os horários de hoje que já foram agendados por um cliente
    # e ainda não foram confirmados. A lista fica em ordem de horário.
    @staticmethod
    def horario_listar_nao_confirmados_hoje():
        hoje = datetime.now(
            ZoneInfo("America/Sao_Paulo")
        ).date()

        r = []

        for h in Service.horario_listar():
            if h.get_data().date() == hoje \
            and h.get_id_cliente() not in [None, 0] \
            and not h.get_confirmado():
                r.append(h)

        r.sort(key=lambda h: h.get_data())

        return r

    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []

        agora = datetime.now(
            ZoneInfo("America/Sao_Paulo")
        ).replace(tzinfo=None)

        for h in Service.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False \
            and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)

        r.sort(key = lambda h : h.get_data())

        return r

    @staticmethod
    def horario_listar_profissional(id_profissional):
        r = []

        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)

        r.sort(key = lambda h : h.get_data())

        return r

    @staticmethod
    def horario_listar_cliente(id_cliente):
        r = []

        for h in Service.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)

        r.sort(key = lambda h : h.get_data())

        return r

    @staticmethod
    def horario_listar_agendados(id_profissional):
        r = []

        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional \
            and h.get_id_cliente() not in [None, 0] \
            and h.get_confirmado() == False:
                r.append(h)

        r.sort(key = lambda h : h.get_data())

        return r

    @staticmethod
    def cliente_alterar_senha(id, senha):
        obj = Service.cliente_listar_id(id)

        if obj != None:
            Service.cliente_atualizar(
                id,
                obj.get_nome(),
                obj.get_email(),
                obj.get_fone(),
                senha
            )


    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha, foto=None):
        obj = Profissional(0, nome, email, especialidade, senha, foto)
        Service._validar_email_unico(obj.get_email())
        ProfissionalDAO().inserir(obj)

    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha, foto=None):
        atual = Service.profissional_listar_id(id)
        if foto is None and atual is not None:
            foto = atual.get_foto()

        obj = Profissional(id, nome, email, especialidade, senha, foto)
        Service._validar_email_unico(obj.get_email(), id_profissional=id)
        ProfissionalDAO().atualizar(obj)

    @staticmethod
    def profissional_excluir(id):
        horarios = Service.horario_listar_profissional(id)
        if len(horarios) > 0:raise ValueError("Não é possível excluir profissionais com horários cadastrados")
        ProfissionalDAO().excluir(id)

    @staticmethod
    def profissional_autenticar(email, senha):
        for c in Service.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    @staticmethod
    def profissional_alterar_senha(id, senha):
        obj = Service.profissional_listar_id(id)

        if obj != None:
            Service.profissional_atualizar(
                id,
                obj.get_nome(),
                obj.get_email(),
                obj.get_especialidade(),
                senha
            )



    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):

        obj = Atendimento(
            0,
            data,
            queixa_principal,
            historico_saude,
            avaliacao,
            prescricao,
            id_horario
        )

        AtendimentoDAO().inserir(obj)


    @staticmethod
    def atendimento_listar():

        r = AtendimentoDAO().listar()
        r.sort(key=lambda obj: obj.get_data())

        return r


    @staticmethod
    def atendimento_totalizar_profissionais(data_inicial, data_final):
        if data_inicial > data_final:
            raise ValueError("A data inicial deve ser anterior à data final")

        profissionais = Service.profissional_listar()
        horarios = {h.get_id(): h for h in Service.horario_listar()}

        totais = {
            p.get_id(): {
                "Profissional": p.get_nome(),
                "Atendimentos": 0
            }
            for p in profissionais
        }

        for atendimento in Service.atendimento_listar():
            data = atendimento.get_data().date()

            if data_inicial <= data <= data_final:
                horario = horarios.get(atendimento.get_id_horario())

                if horario is not None:
                    id_profissional = horario.get_id_profissional()
                    if id_profissional in totais:
                        totais[id_profissional]["Atendimentos"] += 1

        return list(totais.values())

    
    @staticmethod
    def atendimento_totalizar_servicos_profissional(id_profissional, data_inicial, data_final):
        if data_inicial > data_final:
            raise ValueError("A data inicial deve ser anterior à data final")

        servicos = Service.servico_listar()
        horarios = {h.get_id(): h for h in Service.horario_listar()}

        totais = {
            s.get_id(): {
                "Serviço": s.get_descricao(),
                "Quantidade": 0
            }
            for s in servicos
        }

        for atendimento in Service.atendimento_listar():
            data = atendimento.get_data().date()

            if data_inicial <= data <= data_final:
                horario = horarios.get(atendimento.get_id_horario())

                if horario is not None:
                    if horario.get_id_profissional() == id_profissional:
                        id_servico = horario.get_id_servico()
                        if id_servico in totais:
                            totais[id_servico]["Quantidade"] += 1

        return list(totais.values())


    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)

    @staticmethod
    def horario_listar_para_registrar_atendimento(id_profissional):
        horarios = Service.horario_listar_profissional(id_profissional)
        atendimentos = Service.atendimento_listar()
        ids_atendidos = {a.get_id_horario() for a in atendimentos}
        agora = datetime.now()
        resultado = []

        for h in horarios:
            if h.get_confirmado() \
            and h.get_id_cliente() not in [None, 0] \
            and h.get_data() <= agora \
            and h.get_id() not in ids_atendidos:
                resultado.append(h)
        return resultado


    @staticmethod
    def atendimento_registrar(
        id_horario,
        id_profissional,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao
    ):

        horario = Service.horario_listar_id(id_horario)

        if horario is None:
            raise ValueError("Horário não encontrado")

        if horario.get_id_profissional() != id_profissional:
            raise ValueError("Este horário não pertence a você")

        if not horario.get_confirmado():
            raise ValueError("O horário precisa estar confirmado")

        if horario.get_id_cliente() in [None, 0]:
            raise ValueError("Este horário não possui cliente")

        # Impede registrar duas vezes o mesmo atendimento.
        for atendimento in Service.atendimento_listar():

            if atendimento.get_id_horario() == id_horario:
                raise ValueError("Este atendimento já foi registrado")

        Service.atendimento_inserir(
            horario.get_data(),
            queixa_principal,
            historico_saude,
            avaliacao,
            prescricao,
            id_horario
        )


    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):

        obj = Atendimento(
            id,
            data,
            queixa_principal,
            historico_saude,
            avaliacao,
            prescricao,
            id_horario
        )

        AtendimentoDAO().atualizar(obj)


    @staticmethod
    def atendimento_excluir(id):

        AtendimentoDAO().excluir(id)