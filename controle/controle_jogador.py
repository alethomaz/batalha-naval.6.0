from entidade.jogador import Jogador
from dao.jogador_dao import JogadorDAO
from exception.nao_encontrado import NaoEncontrado
from tela.jogador_interface import JogadorInterface
from random import randint


class ControleJogador:
    def __init__(self, controle_principal) -> None:
        self.__controlador_principal = controle_principal
        self.__jogador_tela = JogadorInterface()
        self.__jogador_dao = JogadorDAO()
        
        
    def pega_jogador_nome(self, nome: str) -> Jogador:
        try:
            return self.__jogador_dao.get(nome)
        except NaoEncontrado:
            return None
        
    def salvar_jogador(self, jogador: Jogador):
        self.__jogador_dao.add(jogador)
        
    def remover_jogador(self, jogador: Jogador):
        try:
            self.__jogador_dao.remove(jogador.nome)
            for jogo in jogador.jogo:
                self.__controlador_principal.controle_partida.lista_partidas.remove(jogo)
        except NaoEncontrado as e:
            self.__jogador_tela.mostra_mensagem(e)
        
    @property
    def jogadores(self):
        return self.__jogador_dao.get_all()
    
    @property
    def jogador_tela(self):
        return self.__jogador_tela

    def logar_jogador(self) -> Jogador:
        dicionario = self.__jogador_tela.login_jogador()
        if dicionario == None:
            self.__controlador_principal.inicia_jogo() 
        
        usuario = dicionario['username']
        senha = dicionario['password']
        
        for jogador in self.__jogador_dao.get_all():
            if usuario == jogador.usuario and \
            senha == jogador.senha:
                return jogador
                
        self.__jogador_tela.mostra_mensagem('Usuário ou senha inválidos!')
        
    def obtem_informacoes_jogador(self) -> tuple:
        id = self.__jogador_tela.ontem_informacao('ID: ')
        nome = self.__jogador_tela.ontem_informacao('Nome: ')
        usuario = self.__jogador_tela.ontem_informacao('Usuário: ')
        senha = self.__jogador_tela.ontem_informacao('Senha: ')
        return id, nome, usuario, senha
        
    def tratar_usuario(self):
        jogador_logado = self.__controlador_principal.jogador_logado
        usuarios = [jogador.usuario for jogador in self.__jogadores]
        while True:
            usuario = self.__jogador_tela.ontem_informacao('Usuário: ')
            if usuario not in usuarios or \
            usuario == jogador_logado.usuario:
                return usuario
            else:
                self.__jogador_tela.mostra_mensagem('Usuário já cadastrado!')
    
    def cadastrar_jogador(self) -> Jogador:
        dicionario = self.__jogador_tela.abrir_tela_cadastro()
        if dicionario == None:
            self.__controlador_principal.inicia_jogo()
        nome = dicionario['nome']
        usuario = dicionario['username']
        senha = dicionario['password']
        id = randint(1, 1000)
        
        novo_jogador = Jogador(id, nome, usuario, senha)
        self.salvar_jogador(novo_jogador)
        return novo_jogador
    
    def mostrar_historico_jogador(self):
        jogador = self.__controlador_principal.jogador_logado
        jogos = jogador.jogo
        print(f'Jogos:{jogos}')
        self.__jogador_tela.mostrar_historicos(jogos)
    
            
    def editar_jogador(self):
        dicionario_edicao = self.jogador_tela.obtem_informacoes_jogador()
        
        if dicionario_edicao == None:
            self.__controlador_principal.inicia_jogo()
            
        nome = dicionario_edicao['nome']
        usuario = dicionario_edicao['username']
        senha = dicionario_edicao['password']
        
        jogador_logado = self.__controlador_principal.jogador_logado
        jogador_logado.nome = nome
        jogador_logado.usuario = usuario
        jogador_logado.senha = senha
        self.salvar_jogador(jogador_logado)
        self.jogador_tela.mostra_mensagem('Jogador editado com sucesso!')
        
    def remover_jogador(self, jogador: Jogador):
        try:
            self.__jogador_dao.remove(jogador)
            #for jogo in jogador.jogo:
             #   self.__controlador_principal.jogo_ctrl.remover_jogo(jogo)
        except NaoEncontrado as e:
            self.__jogador_tela.mostra_mensagem('Jogador não encontrado')
        
    
    def excluir_jogador(self):
        confirmacao = self.__jogador_tela.confirmacao('Exclusão', 'Deseja realmente excluir o jogador?')
        if confirmacao:
            jogador_logado = self.__controlador_principal.jogador_logado
            for jogo in jogador_logado.jogo:
                self.__controlador_principal.controle_partida.lista_partidas.remove(jogo)
            self.remover_jogador(jogador_logado)
            self.__jogador_tela.mostra_mensagem('Jogador excluído com sucesso!')
            self.__controlador_principal.menu_jogador()
        
    
    def mostra_jogador_logado(self):
        jogador = self.__controlador_principal.jogador_logado
        id = jogador.id
        usuario = jogador.usuario
        pontuacao = jogador.pontuacao_total
        jogador_tela = self.__jogador_tela
        
        if jogador:
            acoes = {
                1: self.mostrar_historico_jogador,
                2: self.editar_jogador,
                3: self.excluir_jogador,
                4: self.__controlador_principal.inicia_jogo
            }
            while True:
                #jogador_tela.mostra_perfil(id,                                           id,
                #                           usuario,
                #                          pontuacao)
                opcao = jogador_tela.mostra_opcoes_jogador(id, usuario, pontuacao)
                acoes[opcao]()
                
    
    def obter_lista_jogadores(self):
        return self.__jogador_dao.get_all()
    
    