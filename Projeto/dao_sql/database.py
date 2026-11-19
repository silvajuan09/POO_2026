import sqlite3
from pathlib import Path

class Database:
    conn = None
    nome_bd = str(Path(__file__).resolve().parent.parent / "agenda.db")

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def executar(cls, sql, params=None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()

    @classmethod
    def inicializar(cls):
        cls.abrir()
        try:
            cls.criar_tabelas()
        finally:
            cls.fechar()

    @classmethod
    def criar_tabelas(cls):
        # --------------------- Tabela Cliente ---------------------
        cls.executar("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL,
                foto BLOB
            );
        """)

        # --------------------- Tabela Profissional ---------------------
        cls.executar("""
            CREATE TABLE IF NOT EXISTS profissional (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                especialidade TEXT NULL,
                senha TEXT NOT NULL,
                foto BLOB
            );
        """)

        # --------------------- Tabela Servico ---------------------
        cls.executar("""
            CREATE TABLE IF NOT EXISTS servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL
            );
        """)

        # --------------------- Tabela Horario ---------------------
        cls.executar("""
            CREATE TABLE IF NOT EXISTS horario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                confirmado INTEGER DEFAULT 0,
                id_cliente INTEGER,
                id_servico INTEGER,
                id_profissional INTEGER,

                FOREIGN KEY (id_cliente) REFERENCES cliente(id) ON DELETE CASCADE,
                FOREIGN KEY (id_servico) REFERENCES servico(id) ON DELETE CASCADE,
                FOREIGN KEY (id_profissional) REFERENCES profissional(id) ON DELETE CASCADE
            );
        """)

        # --------------------- Tabela Atendimento ---------------------
        cls.executar("""
            CREATE TABLE IF NOT EXISTS atendimento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                queixa_principal TEXT NULL,
                historico_saude TEXT NULL,
                avaliacao TEXT NULL,
                prescricao TEXT NULL,
                id_horario INTEGER,

                FOREIGN KEY (id_horario) REFERENCES horario(id) ON DELETE CASCADE
            );
        """)

        cls.adicionar_coluna_caso_nao_exista("cliente", "foto", "BLOB")
        cls.adicionar_coluna_caso_nao_exista("profissional", "foto", "BLOB")

    @classmethod
    def adicionar_coluna_caso_nao_exista(cls, tabela, coluna, tipo):
        cursor = cls.conn.cursor()

        cursor.execute(f"PRAGMA table_info({tabela})")
        colunas = [linha[1] for linha in cursor.fetchall()]

        if coluna not in colunas:
            cls.executar(
                f"ALTER TABLE {tabela} ADD COLUMN {coluna} {tipo}"
            )