

class NaoEncontrado(Exception):
    def __init__(self, objeto: str) -> None:
        super().__init__(f'{objeto} não foi encontrado')