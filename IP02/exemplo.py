class Pessoa():
    def __init__(self):
        self.nome = None
        self.cpf = None

        self.infoContato = []

class Contato():
    def __init__(self):
        self.tipo = None
        self.info = None

p1 = Pessoa()
p1.nome = "Luiz"
p1.cpf = "123324345"

c1 = Contato()

c1.tipo = "Email"
c1.info = "luiz@eu.com"

