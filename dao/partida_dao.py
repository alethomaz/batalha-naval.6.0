from dao.dao import DAO
from entidade.partida import Partida
from exception.nao_encontrado import NaoEncontrado

class PartidaDAO(DAO):
    def __init__(self):
        super().__init__('partidas.pkl')

    def add(self, partida: Partida):
        if isinstance(partida, Partida) and isinstance(partida.jogador, str):
            super().add(partida.jogador, partida)

    def get(self, jogador: str):
        try:
            if isinstance(jogador, str):
                return super().get(jogador)
        except KeyError:
            raise NaoEncontrado('partida')

    def remove(self, partida: Partida):
        try:
            if isinstance(partida, Partida) and isinstance(partida.jogador, str):
                super().remove(partida.jogador)
        except KeyError:
            raise NaoEncontrado('partida')