from dao_sql.dao import DAO
from models.horario import Horario
from datetime import datetime

class HorarioDAO(DAO):
    
    def inserir(self, obj):
        self.abrir()
        sql = """
            INSERT INTO horario (data, hora, confirmado, id_cliente, id_servico, id_profissional)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, (obj.get_data(), obj.get_hora(), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional()))
        self.fechar()


    def listar(self):
        self.abrir()
        sql = "SELECT * FROM horario"
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = [Horario(id, data, hora, confirmado, id_cliente, id_servico, id_profissional) for (id, data, hora, confirmado, id_cliente, id_servico, id_profissional) in rows]
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = "SELECT * FROM horario WHERE id = ?"
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Horario(*row) if row else None
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = """
            UPDATE horario SET data=?, hora=?, confirmado=?, id_cliente=?, id_servico=?, id_profissional=?
            WHERE id=?
        """
        self.execute(sql, (obj.get_data(), obj.get_hora(), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = "DELETE FROM horario WHERE id=?"
        self.execute(sql, (id,))
        self.fechar()