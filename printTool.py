def deColorLen(texto):
    if texto[0] == '\x1b':
        texto = texto[5:-5]

    return len(texto)


def colorizar(texto, cor):
    cores = {'rosa': '\033[95m', 'azul': '\033[94m', 'verde': '\033[92m', 'amarelo': '\033[93m',
             'vermelho': '\033[91m',
             'clear': '\033[0m', }

    if cor not in cores:
        return texto

    return f"{cores[cor]}{texto}{cores["clear"]}"


class configCentralizar:

    def __init__(self, MX, borda):
        self.MX = MX
        self.borda = borda

    def centralizar(self, texto, ):
        tamanhoTexto = deColorLen(texto)
        fix = 0
        if tamanhoTexto % 2 != 0: fix = 1

        espacos = int((self.MX - tamanhoTexto) / 2)
        print(f"{self.borda * espacos} {texto} {self.borda * (espacos + fix)}")


class configColorizar:
    def __init__(self, cor):
        if cor not in ['rosa', 'azul', 'verde', 'amarelo', 'vermelho', 'clear']:
            raise CorInexistente

        self.cor = cor


class CorInexistente(Exception):
    pass
