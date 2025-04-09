class Restaurante():
    def __init__(self):
        self.pedidos = []

        

    def listaPedidos(self, nome: str, numero: str, enviar: bool, adicionar: bool, remover: bool):
        self.nome = nome
        self.numero = numero
        self.enviar = enviar
        self.adicionar = adicionar
        self.remover = remover

        pedido = [self.nome, self.numero, self.enviar, self.adicionar, self.remover]
        self.pedidos.append(pedido)


        

        print(f"--- Pedido ---")
        print(f"Nome: {pedido[0]}")
        print(f"Número do Pedido: {pedido[1]}")
        print(f"Enviar: {pedido[2]}")
        print(f"Adicionar: {pedido[3]}")
        print(f"Remover: {pedido[4]}")
        print("--------------\n")
        return pedido

p1 = Restaurante()
p2 = Restaurante()
p1.listaPedidos(nome="Luiz", numero="123454", enviar=True, adicionar=True, remover=False)
p2.listaPedidos(nome="Chico", numero="1233454", enviar=False, adicionar=False, remover=True)


