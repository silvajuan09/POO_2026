class Playlist:
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

class PlaylistItem:
    def __init__(self, id, idPlaylist, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlaylist(idPlaylist)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)
    def set_id(self, id):
        if id < 0: raise ValueError('O ID deve ser positivo')
        self.__id = id
    def set_idPlaylist(self, idPlaylist):
        if idPlaylist < 0: raise ValueError('O ID da playlist deve ser positivo')
        self.__idPlaylist = idPlaylist
    def set_idMusica(self, idMusica):
        if idMusica < 0: raise ValueError('O ID da música deve ser positivo')
        self.__idMusica = idMusica
    def set_sequencia(self, sequencia):
        if sequencia < 0: raise ValueError('A ordem da música na playlist deve ser positiva')
        self.__sequencia = sequencia
    def get_id(self): return self.__id
    def get_idPlaylist(self): return self.__idPlaylist
    def get_idMusica(self): return self.__idMusica
    def get_sequencia(self): return self.__sequencia
    def __str__(self): 
        return f"{self.__id} - {self.__idPlaylist} - {self.__idMusica} - {self.__sequencia}"

class PlaylistUI:
    playlists = []
    musicas = []
    playlistItens = []
    @staticmethod
    def main():
        op = 0
        while op != 14:
            op = PlaylistUI.menu()
            if op == 1: PlaylistUI.cadastrar_playlist()
            if op == 2: PlaylistUI.abrir_playlist()
            if op == 3: PlaylistUI.cadastrar_musica()
            if op == 4: PlaylistUI.cadastrar_playlistItem()
            if op == 5: PlaylistUI.listar_playlists()
            if op == 6: PlaylistUI.listar_musicas()
            if op == 7: PlaylistUI.listar_playlistItens()
            if op == 8: PlaylistUI.atualizar_playlist()
            if op == 9: PlaylistUI.atualizar_musica()
            if op == 10: PlaylistUI.atualizar_playlistItem()
            if op == 11: PlaylistUI.excluir_playlist()
            if op == 12: PlaylistUI.excluir_musica()
            if op == 13: PlaylistUI.excluir_playlistItem()
        
    @staticmethod
    def menu():
        print('''
        1-Cadastrar playlist
        2-Abrir playlist
        3-Cadastrar música
        4-Cadastrar item em uma playlist
        5-Listar playlists 
        6-Listar músicas
        7-Listar itens de playlist 
        8-Atualizar playlist 
        9-Atualizar música 
        10-Atualizar item de playlist 
        11-Excluir playlist 
        12-Excluir música 
        13-Excluir item de playlist 
        14-Fim
        ''')
        return int(input('Escolha uma opção: '))

    @classmethod
    def cadastrar_playlist(cls):
        id = int(input('Informe o ID da playlist: '))
        nome = input('Escolha um nome para sua playlist: ')
        descricao = input('Descreva sua playlist: ')
        x = Playlist(id, nome, descricao)
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
        idPlaylist = int(input('Informe o ID da playlist a qual o item será acrescido: '))
        idMusica = int(input('Informe o ID da música que o item representa: '))
        sequencia = int(input('Informe a ordem do item na playlist: '))
        
        for item in cls.playlistItens:
            if item.get_idPlaylist() == idPlaylist and item.get_sequencia() == sequencia:
                print('Já existe uma música nessa posição da playlist')
                return
            
        x = PlaylistItem(id, idPlaylist, idMusica, sequencia)
        cls.playlistItens.append(x)

    @classmethod
    def listar_playlists(cls):
        if len(cls.playlists) == 0:
            print('Não há playlists cadastradas!')
        else:
            for pl in cls.playlists:
                print(pl)

    @classmethod
    def listar_musicas(cls):
        if len(cls.musicas) == 0: print('Não há músicas cadastradas!')
        else: 
            for msc in cls.musicas:
                print(msc)
    
    @classmethod
    def listar_playlistItens(cls):
        if len(cls.playlistItens) == 0: print('Não há itens de playlist cadastrados!')
        else:
            for plit in cls.playlistItens:
                print(plit)

    @classmethod
    def atualizar_playlist(cls):
        PlaylistUI.listar_playlists()
        id = int(input('Informe o ID da playlist a ser atualizada: '))

        pl_encontrada = None
        for i in cls.playlists:
            if i.get_id() == id:
                pl_encontrada = i
                break

        if pl_encontrada is not None:
            nome = input("Informe o novo nome: ")
            pl_encontrada.set_nome(nome)
            descricao = input("Informe a nova descrição: ")
            pl_encontrada.set_descricao(descricao)
        else:
            print("Playlist não encontrada!") 
        
    @classmethod
    def atualizar_musica(cls):
        PlaylistUI.listar_musicas()
        id = int(input('Informe o ID da música a ser atualizada: '))

        msc_encontrada = None
        for i in cls.musicas:
            if i.get_id() == id:
                msc_encontrada = i
                break

        if msc_encontrada is not None:
            titulo = input('Informe o novo título: ')
            msc_encontrada.set_titulo(titulo)

            artista = input('Informe o novo artista: ')
            msc_encontrada.set_artista(artista)

            album = input('Informe o novo nome do álbum: ')
            msc_encontrada.set_album(album)
        else: print('Música não encontrada!')
    
    @classmethod
    def atualizar_playlistItem(cls):
        PlaylistUI.listar_playlistItens()
        id = int(input('Informe o ID do item de playlist a ser atualizado: '))

        plit_encontrado = None
        for i in cls.playlistItens:
            if i.get_id() == id:
                plit_encontrado = i
                break
        
        if plit_encontrado is not None:
            idPlaylist = int(input('Informe o novo ID da playlist: '))
            plit_encontrado.set_idPlaylist(idPlaylist)

            idMusica = int(input('Informe o novo ID da música: '))
            plit_encontrado.set_idMusica(idMusica)

            sequencia = int(input('Informe a nova sequência do item: '))
            plit_encontrado.set_sequencia(sequencia)
        else: print('Item de playlist não encontrado!')

    @classmethod
    def excluir_playlist(cls):
        PlaylistUI.listar_playlists()
        id = int(input('Informe o ID da playlist a ser excluída: '))

        pl_encontrada = None
        for i in cls.playlists:
            if i.get_id() == id:
                pl_encontrada = i
                break

        if pl_encontrada is not None:
            cls.playlists.remove(pl_encontrada)
        else:
            print("Playlist não encontrada!")
    @classmethod
    def excluir_musica(cls):
        PlaylistUI.listar_musicas()
        id = int(input('Informe o ID da música a ser excluída: '))

        msc_encontrada = None
        for i in cls.musicas:
            if i.get_id() == id:
                msc_encontrada = i
                break

        if msc_encontrada is not None:
            cls.musicas.remove(msc_encontrada)
        else: print('Música não encontrada!')
    
    @classmethod
    def excluir_playlistItem(cls):
        PlaylistUI.listar_playlistItens()
        id = int(input('Informe o ID do item de playlist a ser excluído: '))

        plit_encontrado = None
        for i in cls.playlistItens:
            if i.get_id() == id:
                plit_encontrado = i
                break
        
        if plit_encontrado is not None:
            cls.playlistItens.remove(plit_encontrado)
        else: print('Item de playlist não encontrado!')

    @classmethod
    def abrir_playlist(cls):
        idPlaylist = int(input('Informe o ID da playlist que vocÊ deseja listar: '))

        itens = []

        for item in cls.playlistItens:
            if item.get_idPlaylist() == idPlaylist:
                itens.append(item)

        itens.sort(key=lambda x: x.get_sequencia())

        for item in itens:
            for musica in cls.musicas:
                if musica.get_id() == item.get_idMusica():
                    print(item.get_sequencia(), '-', musica)

PlaylistUI.main()