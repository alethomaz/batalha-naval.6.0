import PySimpleGUI as sg

class RankingInterface:
    def __init__(self):
        self.__window = None
        
    def mostrar_ranking(self, ranking: list):
        layout = [
            [sg.Text('RANKING DE JOGADORES', font=('Helvetica', 16), justification='center')],
            [sg.Text('Nome', size=(20, 1), font=('Helvetica', 14), justification='center'),
             sg.Text('Pontuação', size=(15, 1), font=('Helvetica', 14), justification='center')],
        ]

        # Add rows for each player in the ranking
        for jogador in ranking:
            layout.append([sg.Text(jogador.nome, size=(20, 1), font=('Helvetica', 12), justification='center'),
                           sg.Text(str(jogador.pontuacao_total), size=(15, 1), font=('Helvetica', 12))])
            
        layout.append([sg.Button('Voltar', key='voltar_button', size=(10, 1), font=('Helvetica', 12))])
            
        self.__window = sg.Window('Ranking').Layout(layout)
        button, values = self.__window.read()
        if button == 'voltar_button':
            self.__window.close()
            return 1
