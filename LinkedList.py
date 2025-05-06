class No:
    def __init__(self, num):
        self.num = num
        self.next = None

class Fila:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, num): 
        novo_no = No(num)
        if self.head == None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no
    def show(self):
        aux = self.head
        while aux != None:
            print(aux.num)
            aux = aux.next

fila = Fila()
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(4)
fila.show()