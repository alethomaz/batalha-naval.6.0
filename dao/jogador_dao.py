from dao.dao import DAO
from entidade.jogador import Jogador
from exception.nao_encontrado import NaoEncontrado

class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogadores.pkl')
        
    def add(self, jogador):
        if isinstance(jogador, Jogador) and isinstance(jogador.nome, str):
            super().add(jogador.nome, jogador)
            
    def get(self, nome: str):
        try:
            if isinstance(nome, str):
                return super().get(nome)
        except KeyError:
            raise NaoEncontrado('jogador')
        
    def remove(self, jogador) -> None:
        try:
            if isinstance(jogador, Jogador) and isinstance(jogador.nome, str):
                super().remove(jogador.nome)
        except KeyError:
            raise NaoEncontrado('jogador')