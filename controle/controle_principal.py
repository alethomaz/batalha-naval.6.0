

from controle.controle_ranking import ControleRanking
from controle.controle_jogador import ControleJogador
from controle.controle_oceano import ControleOceano
from controle.controle_partida import ControlePartida
from tela.principal_interface import PrincipalInterface


class ControlePrincipal:
    def __init__(self):
        self.__jogador_logado = None
        self.__tela_principal = PrincipalInterface()
        self.__controle_ranking = ControleRanking(self)
        self.__controle_jogador = ControleJogador(self)
        self.__controle_oceano = ControleOceano()
        self.__controle_partida = ControlePartida()
        
        
    @property
    def controle_jogador(self):
        return self.__controle_jogador
    
    @property
    def controle_oceano(self):
        return self.__controle_oceano

    @property
    def controle_ranking(self):
        return self.__controle_ranking
        
    @property
    def jogador_logado(self):
        return self.__jogador_logado
    
    @property
    def controle_partida(self):
        return self.__controle_partida
    
    def inicia_jogo(self):
        if self.__jogador_logado:
            self.menu_principal()
        else:
            self.menu_jogador()
            
    def login_jogador(self):
        self.__jogador_logado = self.__controle_jogador.logar_jogador()
        self.inicia_jogo()
        
    def cadastro_jogador(self):
        self.__jogador_logado = self.__controle_jogador.cadastrar_jogador()
        self.inicia_jogo()  
        
    def sair(self):
        exit(0)
        
    def jogar(self):
        self.__controle_partida.iniciar_partida(self.__jogador_logado)
        
    def perfil_jogador(self):
        self.__controle_jogador.mostra_jogador_logado()   
    
    def ranking(self):
        self.__controle_ranking.listar_ranking()
    
    def menu_jogador(self):
        while True:
            opcoes = {
                1: self.login_jogador,
                2: self.cadastro_jogador,
                3: self.sair
            }
            
            opcao_escolhida = self.__tela_principal.abrir_menu_principal()
            opcoes[opcao_escolhida]()
            
    def menu_principal(self):
        while True:
            opcoes = {
                1: self.jogar,
                2: self.perfil_jogador,
                3: self.ranking,
                4: self.sair
            }
            opcao_escolhida = self.__tela_principal.exibir_menu_logado()
            opcoes[opcao_escolhida]()