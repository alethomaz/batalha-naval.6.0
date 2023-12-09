

class Embarcacao:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__posicao = []
        self.__afundado = None

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao: list):
        if isinstance(posicao, list):
            self.__posicao = posicao

    @property
    def afundado(self):
        return self.__afundado

    @afundado.setter
    def afundado(self, afundado: bool):
        if isinstance(afundado, bool):
            self.__afundado = afundado
