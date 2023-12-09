import PySimpleGUI as sg

class JogadorInterface:
    def __init__(self) -> None:
        self.__window = None
        
    def init_components(self):
        layout = [
            [sg.Text("Cadastro", size=(20, 1), justification='center', font=("Helvetica", 25))],
            #[sg.Text("ID:"), sg.Input(key='id')],
            [sg.Text("Nome:"), sg.Input(key='nome')],
            [sg.Text("Nome de Usuário:"), sg.Input(key='username')],
            [sg.Text("Senha:"), sg.Input(key='password', password_char='*')],
            [sg.Button("Cadastrar", key="cadastrar_button"), sg.Button("Cancelar", key="cancelar_button")],
        ]
        self.__window = sg.Window('Cadastro').Layout(layout)
    
    def abrir_tela_cadastro(self):
        self.init_components()
        button, values = self.__window.read()

        if button == "cadastrar_button":
            #user_id = values['id']
            nome = values['nome']
            username = values['username']
            password = values['password']            
            # Return the collected data as a dictionary
            self.__window.close()
            return {'nome': nome, 'username': username, 'password': password}
        if button == "cancelar_button":
            self.__window.close()
            return None

        

    def mostra_opcoes_jogador(self, id: int, usuario: str, pontos: int):
        layout = [
            [sg.Text("Jogador", size=(30, 1), justification='center', font=("Helvetica", 20))],
            [sg.Text(f"ID: {id}", justification='center', font=("Helvetica", 14))],
            [sg.Text(f"Usuário: {usuario}", justification='center', font=("Helvetica", 14))],
            [sg.Text(f"Pontos: {pontos}", justification='center', font=("Helvetica", 14))],
            [sg.Button("Mostrar Histórico", key="historico_button")],
            [sg.Button("Editar Perfil", key="editar_button")],
            [sg.Button("Excluir Conta", key="excluir_button")],
            [sg.Button("Voltar", key="sair_button")],
        ]
        self.__window = sg.Window('Opções do Jogador', layout=layout, element_justification='c')
        button, values = self.__window.read()
        
        if button == "historico_button":
            self.__window.close()
            return 1
        if button == "editar_button":
            self.__window.close()
            return 2
        if button == "excluir_button":
            self.__window.close()
            return 3
        if button == "sair_button":
            self.__window.close()
            return 4
        
    def mostrar_opcoes_jogador(self):
        self.init_components()
        button, values = self.__window.read()
        print(button, values)
        opcao = 0
        if button == 'login_button':
            opcao = 1
        if button == 'cadastro_button':
            opcao = 2
        if button == 'sair_button':
            opcao = 3

        print(opcao)
        self.__window.close()
        return opcao

    def login_jogador(self):
        layout = [
            [sg.Text("Login", size=(20, 1), justification='center', font=("Helvetica", 25))],
            [sg.Text("Nome de Usuário:"), sg.Input(key='username')],
            [sg.Text("Senha:"), sg.Input(key='password', password_char='*')],
            [sg.Button("Login", key="login_button"), sg.Button("Cancelar", key="cancelar_button")],
        ]
        self.__window = sg.Window('Login').Layout(layout)
        button, values = self.__window.read()

        if button == "login_button":
            username = values['username']
            password = values['password']
            self.__window.close()
            return {'username': username, 'password': password}
        elif button == "cancelar_button":
            self.__window.close()
            # Return a specific value (e.g., None) to indicate cancellation
            return None
            # Return the collected data as a dictionary
        
        
    def obtem_informacoes_jogador(self):
        layout = [
            [sg.Text("Editando", size=(20, 1), justification='center', font=("Helvetica", 25))],
            [sg.Text("Nome:"), sg.Input(key='nome')],
            [sg.Text("Nome de Usuário:"), sg.Input(key='username')],
            [sg.Text("Senha:"), sg.Input(key='password', password_char='*')],
            [sg.Button("Salvar", key="salvar_button"), sg.Button("Cancelar", key="cancelar_button")],            
        ]
        self.__window = sg.Window('Editar Perfil').Layout(layout)
        button, values = self.__window.read()
        if button == "salvar_button":
            nome = values['nome']
            username = values['username']
            password = values['password']
            self.__window.close()
            return {'nome': nome, 'username': username, 'password': password}
        if button == "cancelar_button":
            self.__window.close()
            return None
    
    def mostra_mensagem(self, mensagem: str):
        sg.Popup(mensagem)
        
    def confirmacao(self, titulo: str, mensagem: str):
        return sg.PopupYesNo(titulo, mensagem)
    
    def mostrar_historicos(self, jogos: list):
        layout = [
            [sg.Text("Histórico", size=(20, 1), justification='center', font=("Helvetica", 25))],
        ]

        for i, jogo in enumerate(jogos):
            pontos_text = f"Partida {i + 1} - Pontos: {jogo.pontuacao_jogador} x {jogos.pontuacao_computador},\
                            Vencedor: {jogo.vencedor}"
            layout.append([sg.Text(pontos_text)])

        layout.append([sg.Button("Voltar", key="voltar_button")])

        self.__window = sg.Window('Histórico', layout)
        button, values = self.__window.read()
        if button == "voltar_button":
            self.__window.close()
            return None
        