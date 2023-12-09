

class Partida:
    def __init__(self, jogador):
        self.__jogador = jogador
        self.__oceano_jogador = None
        self.__oceano_computador = None
        self.__pontuacao_jogador = 0
        self.__pontuacao_computador = 0
        self.__tiros_jogador = []
        self.__tiros_computador = []
        self.__vencedor = None

    @property
    def tiros_jogador(self):
        return self.__tiros_jogador

    @tiros_jogador.setter
    def tiros_jogador(self, tiro):
        self.__tiros_jogador.append(tiro)

    @property
    def pontuacao_jogador(self):
        return self.__pontuacao_jogador

    @pontuacao_jogador.setter
    def pontuacao_jogador(self, adicao):
        self.__pontuacao_jogador += adicao

    @property
    def tiros_computador(self):
        return self.__tiros_computador

    @tiros_computador.setter
    def tiros_computador(self, tiro):
        self.__tiros_computador.append(tiro)

    @property
    def pontuacao_computador(self):
        return self.__pontuacao_computador

    @pontuacao_computador.setter
    def pontuacao_computador(self, adicao):
        self.__pontuacao_computador += adicao

    @property
    def vencedor(self):
        return self.__vencedor

    @vencedor.setter
    def vencedor(self, vencedor):
        self.__vencedor = vencedor

    @property
    def oceano_jogador(self):
        return self.__oceano_jogador

    @oceano_jogador.setter
    def oceano_jogador(self, oceano):
        self.__oceano_jogador = oceano

    @property
    def oceano_computador(self):
        return self.__oceano_computador

    @oceano_computador.setter
    def oceano_computador(self, oceano):
        self.__oceano_computador = oceano

    @property
    def jogador(self):
        return self.__jogador
