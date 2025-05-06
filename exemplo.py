class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco, telefone=None, email=None):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

cliente1 = Cliente(
    nome="João Silva",
    cpf="123456-90",
    data_nascimento="10/10/10",
    endereco = "Rua tal tal tal",
    telefone="999290192",
    email="jao@bol.com"
)

print(cliente1.cpf)