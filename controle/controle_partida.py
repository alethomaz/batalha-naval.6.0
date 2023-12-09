from tela.partida_interface import TelaPartida
from controle.controle_oceano import ControleOceano
from entidade.oceano import Oceano
from entidade.partida import Partida
from random import randint
from dao.partida_dao import PartidaDAO
from exception.nao_encontrado import NaoEncontrado


class ControlePartida:
    def __init__(self):
        self.__controle_oceano = ControleOceano()
        self.__tela_partida = TelaPartida()
        self.__partida_dao = PartidaDAO()
        self.__partida_atual = None
        self.__oceano_jogador = None
        self.__oceano_computador = None
        self.__lista_partidas = []
        
    def salvar_jogo(self, partida: Partida):
        jogador = self.__controlador_principal.jogador_logado
        jogador.jogos.append(partida)
        self.__partida_dao.add(partida)
        self.__controlador_principal.jogador_ctrl.salvar_jogador(jogador)
        
    def remover_jogo(self, partida: Partida):
        try:
            self.__partida_dao.remove(partida)
            self.__controlador_principal.oceano_ctrl\
                .remover_oceano(partida.oceano_jogador)
            self.__controlador_principal.oceano_ctrl\
                .remover_oceano(partida.oceano_pc)
        except NaoEncontrado as e:
            self.__tela_partida.mostra_mensagem(e)

    @property
    def jogos(self):
        return self.__jogo_dao.get_all()

    @property
    def lista_partidas(self):
        return self.__lista_partidas

    @lista_partidas.setter
    def lista_partidas(self, partida):
        self.lista_partidas.append(partida)

    @property
    def tela_partida(self):
        return self.__tela_partida

    @property
    def controle_oceano(self):
        return self.__controle_oceano

    @property
    def partida_atual(self):
        return self.__partida_atual

    @partida_atual.setter
    def partida_atual(self, jogador):
        self.__partida_atual = Partida(jogador)

    @property
    def oceano_jogador(self):
        return self.__oceano_jogador

    @oceano_jogador.setter
    def oceano_jogador(self, oceano: Oceano):
        self.__oceano_jogador = oceano

    @property
    def oceano_computador(self):
        return self.__oceano_computador

    @oceano_computador.setter
    def oceano_computador(self, oceano: Oceano):
        self.__oceano_computador = oceano

    def iniciar_partida(self, jogador):
        self.oceano_jogador, self.oceano_computador = self.controle_oceano.cria_oceano() ##### CONECTAR ESSE METODO COM O JOGO EM SI #####
        self.partida_atual = Partida(jogador)
        self.menu_opcoes()
        self.partida_atual.oceano_computador = self.oceano_computador
        self.partida_atual.oceano_jogador = self.oceano_jogador
        self.lista_partidas = self.partida_atual
        return

    def menu_opcoes(self):
        while True:
            opcao_escolhida = self.tela_partida.mostra_opcoes()
            if opcao_escolhida == 1:
                self.mostra_mapa()
            if opcao_escolhida == 2 and self.partida_atual.vencedor is None:
                while True:
                    acerto = self.tiro_humano()
                    self.verifica_vencedor()
                    if self.partida_atual.vencedor != None:
                        break
                    if acerto == False:
                        break
                while True and self.partida_atual.vencedor is None:
                    acerto = self.tiro_computador()
                    self.verifica_vencedor()
                    if self.partida_atual.vencedor != None:
                        break
                    if acerto == False:
                        break
            else:
                if opcao_escolhida == 2:
                    self.tela_partida.mostra_erro('A partida já finalizou!')
            if self.partida_atual.vencedor != None:
                return
            if opcao_escolhida == 3:
                self.ver_tiros()

    def mostra_mapa(self):
        dimensao = self.oceano_jogador.dimensao
        mapa = self.oceano_jogador.mapa
        self.tela_partida.mostra_oceano(dimensao, mapa)

    def tiro_humano(self):
        acerto = False
        dimensao = self.oceano_jogador.dimensao
        while True:
            coord_x, coord_y = self.tela_partida.dados_posicao(dimensao)
            verificador = self.verifica_repeticao(coord_x, coord_y, 'humano')
            if verificador == True:
                break
            else:
                self.tela_partida.mostra_erro('As coorddenadas inseridas já sofreram um tiro! Tente novamente')
        mapa = self.oceano_computador.mapa
        self.partida_atual.tiros_jogador = [coord_x, coord_y]
        if mapa[coord_x][coord_y] != '-':
            acerto = True
            mapa = self.atualiza_mapa(mapa, coord_x, coord_y)
            self.oceano_computador.mapa = mapa
            emb = self.altera_embarcacao(coord_x, coord_y, 'humano')
            self.partida_atual.pontuacao_jogador = 1
            verifica_naufrago = self.verifica_naufrago(emb, 'humano')
            if verifica_naufrago == True:
                self.partida_atual.pontuacao_jogador = 3
        if acerto == True:
            self.tela_partida.resultado_tiro('O seu tiro atingiu o inimigo!')
        else:
            self.tela_partida.resultado_tiro('Você não atingiu uma embarcação inimiga!')
        return acerto

    def verifica_repeticao(self, coord_x, coord_y, quem):
        if quem == 'humano':
            tiros = self.partida_atual.tiros_jogador
            for i in range(len(tiros)):
                if tiros[i] == [coord_x, coord_y]:
                    return False
            return True
        if quem == 'comp':
            tiros = self.partida_atual.tiros_computador
            for i in range(len(tiros)):
                if tiros[i] == [coord_x, coord_y]:
                    return False
            return True

    def atualiza_mapa(self, mapa, coord_x, coord_y):
        mapa[coord_x][coord_y] = 'X'
        return mapa

    def altera_embarcacao(self, coord_x, coord_y, quem):
        if quem == 'humano':
            for i in range(len(self.oceano_computador.embarcacoes)):
                for j in range(len(self.oceano_computador.embarcacoes[i].posicao)):
                    if self.oceano_computador.embarcacoes[i].posicao[j] == [coord_x, coord_y]:
                        self.oceano_computador.embarcacoes[i].posicao[j] = 'X'
                        print(self.oceano_computador.mapa)
                        indice = i
                        return indice
        if quem == 'comp':
            for c in range(len(self.oceano_jogador.embarcacoes)):
                for l in range(len(self.oceano_jogador.embarcacoes[c].posicao)):
                    if self.oceano_jogador.embarcacoes[c].posicao[l] == [coord_x, coord_y]:
                        self.oceano_jogador.embarcacoes[c].posicao[l] = 'X'
                        indice = c
                        return indice

    def verifica_naufrago(self, emb, quem):
        if emb != None:
            contador = 0
            if quem == 'humano':
                for i in range(len(self.oceano_computador.embarcacoes[emb].posicao)):
                    if self.oceano_computador.embarcacoes[emb].posicao[i] == 'X':
                        contador += 1
                if contador == len(self.oceano_computador.embarcacoes[emb].posicao):
                    self.oceano_computador.embarcacoes[emb].afundado = True
                    return True
                else:
                    return False
            if quem == 'comp':
                for i in range(len(self.oceano_jogador.embarcacoes[emb].posicao)):
                    if self.oceano_jogador.embarcacoes[emb].posicao[i] == 'X':
                        contador += 1
                if contador == len(self.oceano_jogador.embarcacoes[emb].posicao):
                    self.oceano_jogador.embarcacoes[emb].afundado = True
                    return True
                else:
                    return False

    def tiro_computador(self):
        acerto = False
        dimensao = self.oceano_jogador.dimensao
        while True:
            coord_x, coord_y = self.gera_coordenada(dimensao)
            verificador = self.verifica_repeticao(coord_x, coord_y, 'comp')
            if verificador == True:
                break
        mapa = self.oceano_jogador.mapa
        self.partida_atual.tiros_computador = [coord_x, coord_y]
        if mapa[coord_x][coord_y] != '-':
            acerto = True
            mapa = self.atualiza_mapa(mapa, coord_x, coord_y)
            self.oceano_jogador.mapa = mapa
            emb = self.altera_embarcacao(coord_x, coord_y, 'comp')
            self.partida_atual.pontuacao_computador = 1
            verifica_naufrago = self.verifica_naufrago(emb, 'comp')
            if verifica_naufrago == True:
                self.partida_atual.pontuacao_computador = 3
        if acerto == True:
            self.tela_partida.resultado_tiro('Uma de suas embarcações foi atingida!')
        else:
            self.tela_partida.resultado_tiro('Nenhuma embarcação sua foi atingida!')
        return acerto

    def gera_coordenada(self, dimensao): ###### SE DER TEMPO, PENSAR EM FORMAS DE DEIXAR A MAQUINA MAIS INTELIGENTE ######
        x = randint(1, dimensao)
        y = randint(1, dimensao)
        return x - 1, y - 1

    def verifica_vencedor(self):
        contador = 0
        for i in range(len(self.oceano_computador.embarcacoes)):
            if self.oceano_computador.embarcacoes[i].afundado == True:
                contador += 1
        if contador == 5:
            self.partida_atual.vencedor = 'Vencedor'
            self.tela_partida.mostra_resultado('Você venceu!')
            return
        contador = 0
        for i in range(len(self.oceano_jogador.embarcacoes)):
            if self.oceano_jogador.embarcacoes[i].afundado == True:
                contador += 1
        if contador == 5:
            self.partida_atual.vencedor = 'Computador'
            self.tela_partida.mostra_resultado('Você perdeu!')
        return

    def ver_tiros(self):
        tiros = self.partida_atual.tiros_jogador
        self.tela_partida.mostra_tiros(tiros)
        return
    
    def obter_jogo_id(self, id_jogo):
        for partida in self.lista_partidas:
            if partida.id == id_jogo:
                return partida
        return None
    
    def mostra_relatorio(self):
        nome = self.__tela_partida.obtem_nome()
        for partida in self.lista_partidas:
            if partida.jogador.nome == nome:
                self.__tela_partida.mostra_relatorio(partida)
                return
  