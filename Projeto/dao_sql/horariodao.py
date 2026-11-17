from dao_sql.dao import DAO
from models.horario import Horario
from datetime import datetime

class HorarioDAO(DAO):
    
    def inserir(self, obj):
        self.abrir()
        sql = """
            INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional)
            VALUES (?, ?, ?, ?, ?)
        """
        self.execute(sql, (obj.get_data().isoformat(sep=" "), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional()))
        self.fechar()

    def _converter_linha(self, row):
        id, data, confirmado, id_cliente, id_servico, id_profissional = row

        obj = Horario(id, datetime.fromisoformat(data))

        obj.set_confirmado(bool(confirmado))
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)

        return obj


    def listar(self):
        self.abrir()
        sql = "SELECT * FROM horario"
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = [
            self._converter_linha(row)
            for row in rows
        ]
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = "SELECT * FROM horario WHERE id = ?"
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = self._converter_linha(row) if row else None
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = """
            UPDATE horario SET data=?, confirmado=?, id_cliente=?, id_servico=?, id_profissional=?
            WHERE id=?
        """
        self.execute(sql, (obj.get_data().isoformat(sep=" "), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = "DELETE FROM horario WHERE id=?"
        self.execute(sql, (id,))
        self.fechar()