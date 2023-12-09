

class Jogador:
    def __init__(self,
                 id: int,
                 nome: str,
                 usuario: str,
                 senha: str) -> None:
        
        self.__id = id
        self.__nome = nome
        self.__usuario = usuario
        self.__senha = senha 
        self.__pontuacao_total = 0
        self.__jogos = []
        
    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @property
    def usuario(self) -> str:
        return self.__usuario
    
    @property
    def jogo(self) -> list:
        return self.__jogos
    
    @usuario.setter
    def usuario(self, usuario: str):
        self.__usuario = usuario
        
    @property
    def senha(self) -> str:
        return self.__senha
    
    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha
        
    @property
    def pontuacao_total(self):
        return self.__pontuacao_total
    
    def aumenta_pontuacao(self, pontuacao: int):
        self.__pontuacao_total += pontuacao
        
        
        
        