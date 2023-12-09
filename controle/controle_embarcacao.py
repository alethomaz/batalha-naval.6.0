from tela.embarcacao_interface import TelaEmbarcacao
from entidade.embarcacao import Embarcacao
from entidade.bote import Bote
from entidade.submarino import Submarino
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAvioes


class ControleEmbarcacao:
    def __init__(self):
        self.__tela_embarcacao = TelaEmbarcacao()
        self.__contador_bote = 0
        self.__contador_submarino = 0
        self.__contador_fragata = 0
        self.__contador_porta_avioes = 0

    @property
    def tela_embarcacao(self):
        return self.__tela_embarcacao

    @property
    def contador_bote(self):
        return self.__contador_bote

    @contador_bote.setter
    def contador_bote(self, adicao):
        if adicao != 0:
            self.__contador_bote += adicao
        else:
            self.__contador_bote = 0

    @property
    def contador_submarino(self):
        return self.__contador_submarino

    @contador_submarino.setter
    def contador_submarino(self, adicao):
        if adicao != 0:
            self.__contador_submarino += adicao
        else:
            self.__contador_submarino = 0

    @property
    def contador_fragata(self):
        return self.__contador_fragata

    @contador_fragata.setter
    def contador_fragata(self, adicao):
        if adicao != 0:
            self.__contador_fragata += adicao
        else:
            self.__contador_fragata = 0

    @property
    def contador_porta_avioes(self):
        return self.__contador_porta_avioes

    @contador_porta_avioes.setter
    def contador_porta_avioes(self, adicao):
        if adicao != 0:
            self.__contador_porta_avioes += adicao
        else:
            self.__contador_porta_avioes = 0

    def mostra_opcoes(self):
        while True:
            embarcacao_escolhida = self.tela_embarcacao.mostra_opcoes()
            if embarcacao_escolhida == 1:
                if self.contador_bote < 3:
                    self.contador_bote = 1
                    self.resetador()
                    return 1, Bote()
                else:
                    self.tela_embarcacao.mostra_erro('Todos os botes já foram posicionados!')
            if embarcacao_escolhida == 2:
                if self.contador_submarino < 2:
                    self.contador_submarino = 1
                    self.resetador()
                    return 2, Submarino()
                else:
                    self.tela_embarcacao.mostra_erro('Todos os submarinos já foram posicionados!')
            if embarcacao_escolhida == 3:
                if self.contador_fragata < 2:
                    self.contador_fragata = 1
                    self.resetador()
                    return 3, Fragata()
                else:
                    self.tela_embarcacao.mostra_erro('Todas as fragatas já foram posicionadas!')
            if embarcacao_escolhida == 4:
                if self.contador_porta_avioes < 1:
                    self.contador_porta_avioes = 1
                    self.resetador()
                    return 4, PortaAvioes()
                else:
                    self.tela_embarcacao.mostra_erro('Todos os porta aviões já foram posicionados!')

    def resetador(self):
        if (self.contador_bote + self.contador_submarino +
            self.contador_fragata + self.contador_porta_avioes == 8):
            self.contador_bote = 0
            self.contador_submarino = 0
            self.contador_fragata = 0
            self.contador_porta_avioes = 0
        return
