import base64

class Profissional:
    def __init__(self, id, nome, email, especialidade, senha, foto=None):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)
        self.set_senha(senha)
        self.set_foto(foto)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_email(self, email):
            if email == "": raise ValueError("E-mail deve ser informado")
            self.__email = email
    def set_especialidade(self, especialidade):
            if especialidade == "": raise ValueError("Especialidade deve ser informada")
            self.__especialidade = especialidade
    def set_senha(self, senha):
        if senha == "": raise ValueError("Senha deve ser informada")
        self.__senha = senha
    def set_foto(self, foto):
        if foto is not None and not isinstance(foto, (bytes, bytearray)):
            raise ValueError("Foto deve estar em formato de bytes")
        self.__foto = bytes(foto) if foto is not None else None

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_email(self) : return self.__email
    def get_especialidade(self) : return self.__especialidade
    def get_senha(self) : return self.__senha
    def get_foto(self) : return self.__foto

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__especialidade}"
   
    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "email":self.__email, "especialidade":self.__especialidade, "senha":self.__senha, "foto": base64.b64encode(self.__foto).decode('utf-8') if self.__foto is not None else None }
   
    def to_dict(self):
        return { "id":self.__id, "nome":self.__nome, "email":self.__email, "especialidade":self.__especialidade, "foto": base64.b64encode(self.__foto).decode('utf-8') if self.__foto is not None else None }
   
    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["email"], dic["especialidade"], dic["senha"], base64.b64decode(dic["foto"]) if dic.get("foto") is not None else None)