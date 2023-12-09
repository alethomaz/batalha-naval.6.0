from tela.ranking_interface import RankingInterface

class ControleRanking:
    def __init__(self, controle_principal) -> None:
        self.__controle_principal = controle_principal
        self.__tela_ranking = RankingInterface()
        
    def listar_ranking(self):
        
        jogadores = self.__controle_principal.controle_jogador.obter_lista_jogadores()
        raking = sorted(jogadores, key=lambda jogador: jogador.pontuacao_total, reverse=True)
        opcao = self.__tela_ranking.mostrar_ranking(raking)
        if opcao == 1:
            self.__controle_principal.inicia_jogo()
        