from dao_sql.dao import DAO
from models.atendimento import Atendimento
from datetime import datetime

class AtendimentoDAO(DAO):
    
    def inserir(self, obj):
        self.abrir()
        sql = """
            INSERT INTO atendimento (data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, (obj.get_data(), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario()))
        self.fechar()

    def listar(self):
        self.abrir()
        sql = "SELECT * FROM atendimento"
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = [Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario) for (id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario) in rows]
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = "SELECT * FROM atendimento WHERE id = ?"
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Atendimento(*row) if row else None
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = """
            UPDATE atendimento SET data=?, queixa_principal=?, historico_saude=?, avaliacao=?, prescricao=?, id_horario=?
            WHERE id=?
        """
        self.execute(sql, (obj.get_data(), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = "DELETE FROM atendimento WHERE id=?"
        self.execute(sql, (id,))
        self.fechar()