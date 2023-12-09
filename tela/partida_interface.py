import PySimpleGUI as sg


class TelaPartida():
    def __init__(self):
        self.__janela_opcoes = None
        self.escolha_opcoes()
        self.__janela_posicao = None
        self.escolha_posicao()

    def escolha_opcoes(self):
        layout = [
                    [sg.Text('Qual das embarcações você deseja posicionar?')],
                    [sg.Submit(button_text = 'Ver seu mapa atual')],
                    [sg.Submit(button_text = 'Atirar')],
                    [sg.Submit(button_text = 'Ver tiros realizados')],
                 ]
        self.__janela_opcoes = sg.Window('Opções do usuário').Layout(layout)

    def mostra_opcoes(self):
        button, values = self.__janela_opcoes.Read()
        if button == 'Ver seu mapa atual':
            return 1
        if button == 'Atirar':
            return 2
        if button == 'Ver tiros realizados':
            return 3

    def mostra_erro(self, mensagem: str):
        sg.Popup('Algo deu errado!', mensagem)

    def resultado_tiro(self, mensagem: str):
        sg.Popup('Resultado do seu tiro:', mensagem)

    def mostra_resultado(self, mensagem: str):
        sg.Popup('A partida terminou!', mensagem)

    def mostra_tiros(self, tiros):
        sg.Popup('Tiros realizados!', tiros)

    def escolha_posicao(self):
        layout = [
                    [sg.Text('Defina as coordenadas do tiro')],
                    [sg.Text('Coordenada X', size = (15,1)), sg.InputText('', key = 'Coordenada X')],
                    [sg.Text('Coordenada Y', size = (15,1)), sg.InputText('', key = 'Coordenada Y')],
                    [sg.Submit(button_text = 'Enviar')]
                 ]
        self.__janela_posicao = sg.Window('Coordenadas do tiro').Layout(layout)

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
