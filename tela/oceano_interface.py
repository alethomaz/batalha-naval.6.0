import PySimpleGUI as sg


class TelaOceano:

    def __init__(self):
        self.__janela_opcoes = None
        self.escolha_opcoes()
        self.__janela_tamanho = None
        self.escolha_tamanho()
        self.__janela_posicao = None
        self.escolha_posicao()
        self.__janela_como_posicionar = None
        self.cria_como_posicionar()

    def escolha_opcoes(self):
        layout = [
                    [sg.Text('Escolha uma das opções')],
                    [sg.Submit(button_text = 'Ver Mapa')],
                    [sg.Submit(button_text = 'Posicionar Embarcação')],
                    [sg.Submit(button_text = 'Iniciar o combate')]
                 ]
        self.__janela_opcoes = sg.Window('Opções do usuário').Layout(layout)

    def mostra_opcoes(self):
        button, values = self.__janela_opcoes.read()
        if button == 'Ver Mapa':
            return 1
        if button == 'Posicionar Embarcação':
            return 2
        if button == 'Iniciar o combate':
            return 3

    def close_janela_opcoes(self):
        self.__janela_opcoes.Close()

    def escolha_tamanho(self):
        layout = [
                    [sg.Text('Defina o tamanho do Oceano')],
                    [sg.Text('Tamanho', size = (15,1)), sg.InputText('', key = 'Tamanho')],
                    [sg.Submit(button_text = 'Enviar'), sg.Cancel(button_text = 'Cancelar')]
                 ]
        self.__janela_tamanho = sg.Window('Tamanho do Oceano').Layout(layout)


    def tamanho_oceano(self):
        while True:
            try:
                button, values = self.__janela_tamanho.read()
                numero_inserido = int(values['Tamanho'])
                if button == 'Cancelar':
                    break
                if button == 'Gerar Aleatório':
                    return 1
                if numero_inserido not in range(8,16) or button is 'Cancelar':
                    raise ValueError
            except ValueError:
                self.mostra_erro('Entre com um número que esteja no intervalo [8,15]')
            else:
                self.__janela_tamanho.close()
                return numero_inserido

    def escolha_posicao(self):
        layout = [
                    [sg.Text('Defina as coordenadas da embarcação')],
                    [sg.Text('Coordenada X', size = (15,1)), sg.InputText('', key = 'Coordenada X')],
                    [sg.Text('Coordenada Y', size = (15,1)), sg.InputText('', key = 'Coordenada Y')],
                    [sg.Submit(button_text = 'Enviar'), sg.Cancel(button_text = 'Cancelar')]
                 ]
        self.__janela_posicao = sg.Window('Coordenadas da embarcação').Layout(layout)

    def dados_posicao(self, dimensao):
        layout = [
            [sg.Text('Coordenada X:'), sg.InputText(key='num1')],
            [sg.Text('Coordenada Y:'), sg.InputText(key='num2')],
            [sg.Button('Enviar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Inserir Números', layout)

        while True:
            try:
                event, values = window.read()
                num1 = int(values['num1'])
                num2 = int(values['num2'])
                window['num1'].update('')
                window['num2'].update('')
                if num1 not in range(1, dimensao + 1) or event is 'Cancelar' or num2 not in range(1, dimensao + 1) or event == sg.WINDOW_CLOSED:
                    raise ValueError
            except ValueError:
                self.mostra_erro(f'Entre com um número que esteja no intervalo [1,{dimensao}]')
            else:
                break
        window.close()
        return num1 - 1, num2 - 1

    def mostra_erro(self, mensagem: str):
        sg.Popup('Algo deu errado!', mensagem)

    def mostra_oceano(self, dimensao, mapa):
        headings = ['Coord'] + [str(i+1) for i in range(dimensao)]
        data = [[str(i+1)] + row for i, row in enumerate(mapa)]
        layout = [
            [sg.Text('Estado Atual do seu mapa')],
            [sg.Table(values=data, headings = headings, col_widths=[7]*dimensao, auto_size_columns=False,
                      justification='justified', display_row_numbers=False,
                      font=('Helvetica', 12), 
                      header_font=('Helvetica', 14),
                      num_rows= dimensao)],
            [sg.Button('Fechar')]
        ]
        window = sg.Window('Batalha Naval', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break
        window.close()
        return

    def cria_como_posicionar(self):
        layout = [
                    [sg.Text('Como deseja posicionar as embarcações?')],
                    [sg.Submit(button_text = 'Manualmente')],
                    [sg.Submit(button_text = 'Automaticamente')]
        ]
        self.__janela_como_posicionar = sg.Window('Posicionamento das embarcações').Layout(layout)

    def como_posicionar(self):
        button, values = self.__janela_como_posicionar.read()
        self.__janela_como_posicionar.close()
        if button == 'Manualmente':
            return 1
        if button == 'Automaticamente':
            return 2
