from threading import Thread


class Somador(Thread):

    def __init__(self, inicio, fim):
        Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        self.somatorio = 0

    def run(self):
        for i in range(self.inicio, self.fim + 1):
            self.somatorio += i


s1 = Somador(0, 10)
s1.start()
print(s1.somatorio)
