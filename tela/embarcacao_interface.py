import PySimpleGUI as sg


class TelaEmbarcacao:
    def __init__(self):
        self.__janela_opcoes = None
        self.escolha_opcoes()

    def escolha_opcoes(self):
        layout = [
                    [sg.Text('Qual das embarcações você deseja posicionar?')],
                    [sg.Submit(button_text = 'Posicionar Bote')],
                    [sg.Submit(button_text = 'Posicionar Submarino')],
                    [sg.Submit(button_text = 'Posicionar Fragata')],
                    [sg.Submit(button_text = 'Posicionar Porta Aviões')]
                 ]
        self.__janela_opcoes = sg.Window('Opções do usuário').Layout(layout)

    def mostra_opcoes(self):
        button, values = self.__janela_opcoes.read()
        if button == 'Posicionar Bote':
            return 1
        if button == 'Posicionar Submarino':
            return 2
        if button == 'Posicionar Fragata':
            return 3
        if button == 'Posicionar Porta Aviões':
            return 4

    def mostra_erro(self, mensagem: str):
        sg.Popup('Algo deu errado!', mensagem)
