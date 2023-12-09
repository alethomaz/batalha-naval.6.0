from entidade.oceano import Oceano
from tela.oceano_interface import TelaOceano
from controle.controle_embarcacao import ControleEmbarcacao
from entidade.bote import Bote
from entidade.submarino import Submarino
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAvioes
from random import randint


class ControleOceano:
    def __init__(self):
        self.__controle_embarcacao = ControleEmbarcacao()
        self.__tela_oceano = TelaOceano()
        self.__lista_oceanos = []
        self.__oceano_atual = None
        self.__oceano_computador = None

    @property
    def oceano_computador(self):
        return self.__oceano_computador

    @oceano_computador.setter
    def oceano_computador(self, oceano: Oceano):
        if isinstance(oceano, Oceano):
            self.__oceano_computador = oceano

    @property
    def controle_embarcacao(self):
        return self.__controle_embarcacao

    @property
    def tela_oceano(self):
        return self.__tela_oceano

    @property
    def oceano_atual(self):
        return self.__oceano_atual

    @oceano_atual.setter
    def oceano_atual(self, oceano: Oceano):
        if isinstance(oceano, Oceano) and oceano is not None:
            self.__oceano_atual = oceano

    @property
    def lista_oceanos(self):
        return self.__lista_oceanos

    @lista_oceanos.setter
    def lista_oceanos(self, oceano: Oceano):
        if isinstance(oceano, Oceano) and oceano is not None:
            self.lista_oceanos.append(oceano)

    def cria_oceano(self):
        dimensoes = self.tela_oceano.tamanho_oceano()
        self.oceano_atual = Oceano(dimensoes)
        self.oceano_atual.cria_mapa()
        self.oceano_computador = Oceano(dimensoes)
        self.oceano_computador.cria_mapa()
        self.menu_opcoes()
        return self.oceano_atual, self.oceano_computador

    def menu_opcoes(self):
        embarcacoes_posicionadas = 0
        while True:
            opcao_escolhida = self.tela_oceano.mostra_opcoes()
            if opcao_escolhida == 1:
                self.ver_mapa_atual()
            if opcao_escolhida == 2 and embarcacoes_posicionadas < 8:
                como_posicionar = 1
                if embarcacoes_posicionadas == 0:
                    como_posicionar = self.tela_oceano.como_posicionar()
                if como_posicionar == 1:
                    embarcacoes_posicionadas += 1
                    dimensao = self.oceano_atual.dimensao
                    mapa = self.oceano_atual.mapa
                    opcao_barco, barco = self.controle_embarcacao.mostra_opcoes()
                    self.aloca_embarcacao(dimensao, mapa, opcao_barco, barco)
                    if embarcacoes_posicionadas == 8:
                        mapa = self.oceano_computador.mapa
                        self.aloca_embarcacao_computador(dimensao, mapa, 'comp')
                if como_posicionar == 2:
                    dimensao = self.oceano_atual.dimensao
                    embarcacoes_posicionadas = 8
                    mapa = self.oceano_atual.mapa
                    self.aloca_embarcacao_computador(dimensao, mapa, 'humano')
                    mapa = self.oceano_computador.mapa
                    self.aloca_embarcacao_computador(dimensao, mapa, 'comp')
            else:
                if embarcacoes_posicionadas == 8 and como_posicionar == 1:
                    self.tela_oceano.mostra_erro('Todas as embarcações já foram posicionadas!')
            if opcao_escolhida == 3 and embarcacoes_posicionadas == 8:
                return
            else:
                if opcao_escolhida == 3:
                    self.tela_oceano.mostra_erro('Para iniciar o combate, primeiro posicione todas as embarcações!')

    def ver_mapa_atual(self):
        dimensao = self.oceano_atual.dimensao
        mapa = self.oceano_atual.mapa
        self.tela_oceano.mostra_oceano(dimensao, mapa)

    def aloca_embarcacao(self, dimensao, mapa, opcao_barco, barco):
        if opcao_barco == 1:
            self.posiciona_bote(dimensao, mapa, barco)
        if opcao_barco == 2:
            self.posiciona_submarino(dimensao, mapa, barco)
        if opcao_barco == 3:
            self.posiciona_fragata(dimensao, mapa, barco)
        if opcao_barco == 4:
            self.posiciona_porta_avioes(dimensao, mapa, barco)

    def posiciona_bote(self, dimensao: int, mapa: list, barco: Bote):
        while True:
            x1, y1 = self.tela_oceano.dados_posicao(dimensao)
            if mapa[x1][y1] == '-':
                mapa[x1][y1] = 'B'
                barco.posicao = [x1, y1]
                self.oceano_atual.embarcacoes = barco
                self.oceano_atual.mapa = mapa
                return
            else:
                self.tela_oceano.mostra_erro('Já existe uma embarcação nessas coordenadas!')

    def posiciona_submarino(self, dimensao: int, mapa: list, barco: Submarino):
        while True:
            x1, y1 = self.tela_oceano.dados_posicao(dimensao)
            x2, y2 = self.tela_oceano.dados_posicao(dimensao)
            linearidade = self.verifica_linearidade(x1, y1, x2, y2)
            if linearidade == True:
                tamanho = self.verifica_tamanho(2, x1, y1, x2, y2)
                if tamanho == True:
                    if mapa[x1][y1] == '-' and mapa[x2][y2] == '-':
                        mapa[x1][y1] = 'S'
                        mapa[x2][y2] = 'S'
                        barco.posicao = [[x1, y1], [x2, y2]]
                        self.oceano_atual.embarcacoes = barco
                        self.oceano_atual.mapa = mapa
                        return
            self.tela_oceano.mostra_erro('Algo não está certo no posicionamento do Submarino, tente novamente!')

    def posiciona_fragata(self, dimensao: int, mapa: list, barco: Fragata()):
        while True:
            x1, y1 = self.tela_oceano.dados_posicao(dimensao)
            x2, y2 = self.tela_oceano.dados_posicao(dimensao)
            linearidade = self.verifica_linearidade(x1, y1, x2, y2)
            if linearidade == True:
                tamanho = self.verifica_tamanho(3, x1, y1, x2, y2)
                if tamanho == True:
                    verificador, direcao, coord_3 = self.verifica_existencia(mapa, 3, x1, y1, x2, y2)
                    if verificador == True:
                        mapa[x1][y1] = 'F'
                        mapa[x2][y2] = 'F'
                        if direcao == 'H':
                            mapa[x1][coord_3] = 'F'
                            barco.posicao = [[x1, y1], [x1, coord_3], [x2, y2]]
                            self.oceano_atual.embarcacoes = barco
                            self.oceano_atual.mapa = mapa
                        if direcao == 'V':
                            mapa[coord_3][y1] = 'F'
                            barco.posicao = [[x1, y1], [coord_3, y1], [x2, y2]]
                            self.oceano_atual.embarcacoes = barco
                            self.oceano_atual.mapa = mapa
                        return
            self.tela_oceano.mostra_erro('Algo não está certo no posicionamento da Fragata, tente novamente!')

    def posiciona_porta_avioes(self, dimensao: int, mapa: list, barco: PortaAvioes):
        while True:
            x1, y1 = self.tela_oceano.dados_posicao(dimensao)
            x2, y2 = self.tela_oceano.dados_posicao(dimensao)
            linearidade = self.verifica_linearidade(x1, y1, x2, y2)
            if linearidade == True:
                tamanho = self.verifica_tamanho(4, x1, y1, x2, y2)
                if tamanho == True:
                    verificador, direcao, coord_3, coord_4 = self.verifica_existencia(mapa, 4, x1, y1, x2, y2)
                    if verificador == True:
                        mapa[x1][y1] = 'P'
                        mapa[x2][y2] = 'P'
                        if direcao == 'H':
                            mapa[x1][coord_3] = 'P'
                            mapa[x1][coord_4] = 'P'
                            barco.posicao = [[x1, y1], [x1, coord_3], [x1, coord_4], [x2, y2]]
                            self.oceano_atual.embarcacoes = barco
                            self.oceano_atual.mapa = mapa
                        if direcao == 'V':
                            mapa[coord_3][y1] = 'P'
                            mapa[coord_4][y1] = 'P'
                            barco.posicao = [[x1, y1], [coord_3, y1], [coord_4, y1], [x2, y2]]
                            self.oceano_atual.embarcacoes = barco
                            self.oceano_atual.mapa = mapa
                        return
            self.tela_oceano.mostra_erro('Algo não está certo no posicionamento da Fragata, tente novamente!')

    def verifica_linearidade(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            if x1 == x2 and y1 == y2:
                return False
            else:
                return True
        return False

    def verifica_tamanho(self, tamanho, x1, y1, x2, y2):
        if x1 == x2:
            verificador_tamanho = abs(y1 - y2)
            if tamanho == verificador_tamanho + 1:
                return True
            else:
                return False
        if y1 == y2:
            verificador_tamanho = abs(x1 - x2)
            if tamanho == verificador_tamanho + 1:
                return True
            else:
                return False

    def verifica_existencia(self, mapa, tamanho, x1, y1, x2, y2):
        if tamanho == 3:
            if x1 == x2:
                if y1 > y2:
                    y3 = y2 + 1
                if y2 > y1:
                    y3 = y2 - 1
                if mapa[x1][y3] == '-' and mapa[x1][y1] == '-' and mapa[x2][y2] == '-':
                    return True, 'H', y3
                else:
                    return False, 'F', y3
            if y1 == y2:
                if x1 > x2:
                    x3 = x2 + 1
                if x2 > x1:
                    x3 = x2 - 1
                if mapa[x3][y1] == '-' and mapa[x1][y1] == '-' and mapa[x2][y2] == '-':
                    return True, 'V', x3
                else:
                    return False, 'F', x3
        if tamanho == 4:
            if x1 == x2:
                if y1 > y2:
                    y3 = y2 + 1
                    y4 = y2 + 2
                if y2 > y1:
                    y3 = y2 - 1
                    y4 = y2 - 2
                if mapa[x1][y3] == '-' and mapa[x1][y1] == '-' and mapa[x2][y2] == '-' and mapa[x1][y4] == '-':
                    return True, 'H', y3, y4
                else:
                    return False, 'F', y3, y4
            if y1 == y2:
                if x1 > x2:
                    x3 = x2 + 1
                    x4 = x2 + 2
                if x2 > x1:
                    x3 = x2 - 1
                    x4 = x2 - 2
                if mapa[x3][y1] == '-' and mapa[x1][y1] == '-' and mapa[x2][y2] == '-' and mapa[x4][y1] == '-':
                    return True, 'V', x3, x4
                else:
                    return False, 'F', x3, x4

    def aloca_embarcacao_computador(self, dimensao, mapa, jogador):
        for i in range(3):
            mapa = self.posiciona_bote_computador(dimensao, mapa, Bote(), jogador)
        for i in range(2):
            mapa = self.posiciona_submarino_computador(dimensao, mapa, Submarino(), jogador)
        for i in range(2):
            mapa = self.posiciona_fragata_computador(dimensao, mapa, Fragata(), jogador)
        for i in range(1):
            mapa = self.posiciona_porta_avioes_computador(dimensao, mapa, PortaAvioes(), jogador)
        if jogador == 'comp':
            self.oceano_computador.mapa = mapa
        if jogador == 'humano':
            self.oceano_atual.mapa = mapa
        return

    def gera_coordenada(self, dimensao, letra):
        if letra == 'B':
            x1 = randint(1, dimensao)
            y1 = randint(1, dimensao)
            return x1 - 1, y1 - 1
        if letra == 'S':
            while True:
                x1 = randint(1, dimensao)
                y1 = randint(1, dimensao)
                x2 = randint(x1 - 1, x1 + 1)
                y2 = randint(y1 - 1, y1 + 1)
                if x2 in range(1, dimensao + 1) and y2 in range(1, dimensao + 1):
                    return x1 - 1, y1 - 1, x2 - 1, y2 - 1
        if letra == 'F':
            while True:
                x1 = randint(1, dimensao)
                y1 = randint(1, dimensao)
                x2 = randint(x1 - 2, x1 + 2)
                y2 = randint(y1 - 2, y1 + 2)
                if x2 in range(1, dimensao + 1) and y2 in range(1, dimensao + 1):
                    return x1 - 1, y1 - 1, x2 - 1, y2 - 1
        if letra == 'P':
            while True:
                x1 = randint(1, dimensao)
                y1 = randint(1, dimensao)
                x2 = randint(x1 - 3, x1 + 3)
                y2 = randint(y1 - 3, y1 + 3)
                if x2 in range(1, dimensao + 1) and y2 in range(1, dimensao + 1):
                    return x1 - 1, y1 - 1, x2 - 1, y2 - 1

    def posiciona_bote_computador(self, dimensao: int, mapa: list, barco: Bote, quem):
        while True:
            x1, y1 = self.gera_coordenada(dimensao, 'B')
            if mapa[x1][y1] == '-':
                mapa[x1][y1] = 'B'
                barco.posicao = [x1, y1]
                if quem == 'comp':
                    self.oceano_computador.embarcacoes = barco
                if quem == 'humano':
                    self.oceano_atual.embarcacoes = barco
                return mapa

    def posiciona_submarino_computador(self, dimensao: int, mapa: list, barco: Submarino, quem):
        while True:
            x1, y1, x2, y2 = self.gera_coordenada(dimensao, 'S')
            linearidade = self.verifica_linearidade(x1, y1, x2, y2)
            if linearidade == True:
                tamanho = self.verifica_tamanho(2, x1, y1, x2, y2)
                if tamanho == True:
                    if mapa[x1][y1] == '-' and mapa[x2][y2] == '-':
                        mapa[x1][y1] = 'S'
                        mapa[x2][y2] = 'S'
                        barco.posicao = [[x1, y1], [x2, y2]]
                        if quem == 'comp':
                            self.oceano_computador.embarcacoes = barco
                        if quem == 'humano':
                            self.oceano_atual.embarcacoes = barco
                        return mapa

    def posiciona_fragata_computador(self, dimensao: int, mapa: list, barco: Fragata, quem):
        while True:
            x1, y1, x2, y2 = self.gera_coordenada(dimensao, 'F')
            linearidade = self.verifica_linearidade(x1, y1, x2, y2)
            if linearidade == True:
                tamanho = self.verifica_tamanho(3, x1, y1, x2, y2)
                if tamanho == True:
                    verificador, direcao, coord_3 = self.verifica_existencia(mapa, 3, x1, y1, x2, y2)
                    if verificador == True:
                        mapa[x1][y1] = 'F'
                        mapa[x2][y2] = 'F'
                        if direcao == 'H':
                            mapa[x1][coord_3] = 'F'
                            barco.posicao = [[x1, y1], [x1, coord_3], [x2, y2]]
                            if quem == 'comp':
                                self.oceano_computador.embarcacoes = barco
                            if quem == 'humano':
                                self.oceano_atual.embarcacoes = barco
                        if direcao == 'V':
                            mapa[coord_3][y1] = 'F'
                            barco.posicao = [[x1, y1], [coord_3, y1], [x2, y2]]
                            if quem == 'comp':
                                self.oceano_computador.embarcacoes = barco
                            if quem == 'humano':
                                self.oceano_atual.embarcacoes = barco
                        return mapa

    def posiciona_porta_avioes_computador(self, dimensao: int, mapa: list, barco: PortaAvioes, quem):
        while True:
            x1, y1, x2, y2 = self.gera_coordenada(dimensao, 'P')
            linearidade = self.verifica_linearidade(x1, y1, x2, y2)
            if linearidade == True:
                tamanho = self.verifica_tamanho(4, x1, y1, x2, y2)
                if tamanho == True:
                    verificador, direcao, coord_3, coord_4 = self.verifica_existencia(mapa, 4, x1, y1, x2, y2)
                    if verificador == True:
                        mapa[x1][y1] = 'P'
                        mapa[x2][y2] = 'P'
                        if direcao == 'H':
                            mapa[x1][coord_3] = 'P'
                            mapa[x1][coord_4] = 'P'
                            barco.posicao = [[x1, y1], [x1, coord_3], [x1, coord_4], [x2, y2]]
                            if quem == 'comp':
                                self.oceano_computador.embarcacoes = barco
                            if quem == 'humano':
                                self.oceano_atual.embarcacoes = barco
                        if direcao == 'V':
                            mapa[coord_3][y1] = 'P'
                            mapa[coord_4][y1] = 'P'
                            barco.posicao = [[x1, y1], [coord_3, y1], [coord_4, y1], [x2, y2]]
                            if quem == 'comp':
                                self.oceano_computador.embarcacoes = barco
                            if quem == 'humano':
                                self.oceano_atual.embarcacoes = barco
                        return mapa
