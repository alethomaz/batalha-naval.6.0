from abc import ABC, abstractmethod


class TelaAbstrata(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    def mostra_mensagem(self, mensagem: str):
        print(mensagem)     
    
    def mostra_titulo(self, titulo: str):
        print('-='*15)
        print(titulo.upper())
        print('-='*15)
    
    def mostra_opcoes(self, opcoes: list):
        for indice, opcao in enumerate(opcoes, start=1):
            print(f'{indice}: {opcao}')
            
    def pega_opcao(self, mensagem: str, opcoes_validas: list = None) -> int:
        while True:
            try:
                opcao_escolhida = int(input(mensagem))
                if opcao_escolhida not in opcoes_validas:
                    raise ValueError
                return opcao_escolhida
            except ValueError:
                print('Selecione uma opção válida!')
                if opcoes_validas:
                    print('Opções válidas:', opcoes_validas)
                    
    def ontem_informacao(self, mensagem: str) -> str:
        return input(mensagem)
    
    def confirmacao(self, mensagem: str) -> bool:
        confirmacao = input(f'{mensagem} [S/N]')
        return confirmacao.lower() != 'n'