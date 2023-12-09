from entidade.embarcacao import Embarcacao


class Oceano:
    def __init__(self, dimensao: int):
        self.__dimensao = dimensao
        self.__mapa = []
        self.__embarcacoes = []

    @property
    def dimensao(self):
        return self.__dimensao

    @dimensao.setter
    def dimensao(self, dimensao: int):
        if isinstance(dimensao, int):
            self.__dimensao = dimensao

    @property
    def mapa(self):
        return self.__mapa

    @mapa.setter
    def mapa(self, mapa: list):
        if isinstance(mapa, list) and mapa is not None:
            self.__mapa = mapa

    @property
    def embarcacoes(self):
        return self.__embarcacoes

    @embarcacoes.setter
    def embarcacoes(self, embarcacao):
        if isinstance(embarcacao, Embarcacao):
            self.__embarcacoes.append(embarcacao)

    def cria_mapa(self):
        linha_matriz = ["-"] * self.dimensao
        matriz = [linha_matriz[:] for _ in range(self.dimensao)]
        self.mapa = matriz

    def cria_mapa_padrao(self, dimensao):
        if dimensao == 8:
            # Mapa padrão para dimensão 8x8
            matriz_padrao = [
                ['', 'S', 'S', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', 'B', '~', '~', '~'],
                ['~', '~', 'P', '~', '~', '~', 'S', '~'],
                ['~', '~', 'P', '~', '~', '~', 'S', '~'],
                ['~', '~', 'P', '~', '~', '~', '~', '~'],
                ['~', 'B', 'P', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', 'B', '~'],
                ['~', '~', 'F', 'F', 'F', '~', '~', '~']
            ]
        elif self.dimensao == 15:
            # Mapa padrão para dimensão 15x15
            matriz_padrao = [
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'S', 'S', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', 'F', 'F', 'F', '~', '~', '~', '~', 'F', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'F', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'F', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', 'P', 'P', 'P', 'P', '~', 'S', 'S', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', 'B', '~', '~', '~', 'B', '~', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'B', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
            ]
        else:
            raise ValueError("Dimensão não suportada para o mapa padrão.")

        self.mapa = matriz_padrao
