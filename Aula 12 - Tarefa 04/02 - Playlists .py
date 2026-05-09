class PlayList:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
    def set_id(self, id):
        if id < 0: raise ValueError('O ID deve ser positivo')
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError('Nome não pode ser vazio')
        self.__nome = nome
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError('A descrição não pode ser vazia')
        self.__descricao = descricao
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__descricao}"
    
class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_id(self, id):
        if id < 0: raise ValueError('O ID deve ser positivo')
        self.__id = id
    def set_titulo(self, titulo):
        if titulo == "": raise ValueError('A música precisa de um título')
        self.__titulo = titulo
    def set_artista(self, artista):
        if artista == "": raise ValueError('A música precisa pertencer a um artista')
        self.__artista = artista
    def set_album(self, album):
        if album == "": raise ValueError('A música precisa pertencer a um álbum')
        self.__album = album
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def __str__(self):
        return f"{self.__id} - {self.__titulo} - {self.__artista} - {self.__album}"

class PlayListItem:
    def __init__(self, id, idPlayList, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlayList(idPlayList)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)
    def set_id(self, id):
        if id < 0: raise ValueError('O ID deve ser positivo')
        self.__id = id
    def set_idPlayList(self, idPlayList):
        if idPlayList < 0: raise ValueError('O ID da playlist deve ser positivo')
        self.__idPlayList = idPlayList
    def set_idMusica(self, idMusica):
        if idMusica < 0: raise ValueError('O ID da música deve ser positivo')
        self.__idMusica = idMusica
    def set_sequencia(self, sequencia):
        if sequencia < 0: raise ValueError('A ordem da música na playlist deve ser positiva')
        self.__sequencia = sequencia
    def get_id(self): return self.__id
    def get_idPlayList(self): return self.__idPlayList
    def get_idMusica(self): return self.__idMusica
    def get_sequencia(self): return self.__sequencia
    def __str__(self): 
        return f"{self.__id} - {self.__idPlayList} - {self.__idMusica} - {self.__sequencia}"

class UI:
    playlists = []
    musicas = []
    playlistItens = []
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.cadastrar_playlist()
            if op == 2: UI.cadastrar_musica()
            if op == 3: UI.cadastrar_playlistItem()
        
    @staticmethod
    def menu():
        print('1-Cadastrar playlist 2-Cadastrar música 3-Cadastrar item em uma playlist 4-Fim')
        return int(input('Escolha uma opção: '))

    @classmethod
    def cadastrar_playlist(cls):
        id = int(input('Informe o ID da playlist: '))
        nome = input('Escolha um nome para sua playlist: ')
        descricao = input('Descreva sua playlist: ')
        x = PlayList(id, nome, descricao)
        cls.playlists.append(x)
    
    @classmethod
    def cadastrar_musica(cls):
        id = int(input('Informe o ID da música: '))
        titulo = input('Informe o título da música: ')
        artista = input('Informe o criador da música: ')
        album = input('Informe o álbum da música: ')
        x = Musica(id, titulo, artista, album)
        cls.musicas.append(x)
    
    @classmethod
    def cadastrar_playlistItem(cls):
        id = int(input('Informe o ID do item: '))
        idPlayList = int(input('Informe o ID da playlist a qual o item será acrescido: '))
        idMusica = int(input('Informe o ID da música que o item representa: '))
        sequencia = int(input('Informe a ordem do item na playlist: '))
        
        for item in cls.playlistItens:
            if item.get_idPlayList() == idPlayList and item.get_sequencia() == sequencia:
                print('Já existe uma música nessa posição da playlist')
                return
            
        x = PlayListItem(id, idPlayList, idMusica, sequencia)
        cls.playlistItens.append(x)

UI.main()