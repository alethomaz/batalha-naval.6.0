import PySimpleGUI as sg

class PrincipalInterface:
    
    def __init__(self):
        sg.theme('DarkAmber')
        self.__window = None
        self.init_components()
    
    def init_components(self):
        image_path = '/home/dvdpericles/Programação/batalha-naval-4.0/download.png'
        
        layout = [
            [sg.Text("Batalha Naval", size=(20, 1), justification='center', font=("Helvetica", 25))],
            [sg.Image(filename=image_path, size=(200, 200))],
            [sg.Button("Login", key="login_button")],
            [sg.Button("Cadastro", key="cadastro_button")],
            [sg.Exit("Sair", key="sair_button")]
        ]
        window_size = (400, 400)
        self.__window = sg.Window('Inicio', layout, size=window_size, element_justification='c')

    def abrir_menu_principal(self):
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

    '''def iniciar(self):
        window = sg.Window("Batalha Naval", self.layout, element_justification='c').finalize()

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "sair_button":
                break
            elif event == "login_button":
                self.realizar_login()
            elif event == "cadastro_button":
                self.realizar_cadastro()

        window.close()'''

    def realizar_login(self):
        username = sg.popup_get_text("Digite o nome de usuário", "Login")
        if username:
            self.controle_principal.controle_jogador.login_jogador_existente(username)
            self.exibir_menu_principal()

    def realizar_cadastro(self):
        username = sg.popup_get_text("Digite o nome de usuário", "Cadastro")
        if username:
            self.controle_principal.controle_jogador.cadastrar_jogador(username)
            self.exibir_menu_principal()

    def exibir_menu_logado(self):
        image_path = '/home/dvdpericles/Programação/batalha-naval-4.0/download.png'
        layout_menu_principal = [
            [sg.Text("BATALHA NAVAL", size=(20, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Image(filename=image_path, size=(200, 200))],      
            [sg.Button("Jogar", key="jogar_button")],
            [sg.Button("Perfil", key="perfil_button")], 
            [sg.Button("Ranking", key="ranking_button")],
            [sg.Exit("Sair", key="sair_button")],
        ]
        window_size = (400, 400)
        self.__window = sg.Window("BATALHA NAVAL", layout_menu_principal, size=window_size,\
            element_justification='c')
        
        while True:
            event, values = self.__window.read()
        
            if event == sg.WINDOW_CLOSED or event == "sair_button":
                break
            elif event == "jogar_button":
                self.__window.close()
                return 1
            elif event == "perfil_button":
                self.__window.close()
                return 2
            elif event == "ranking_button":
                self.__window.close()
                return 3
            else:
                self.__window.close()
                return 4

        
        