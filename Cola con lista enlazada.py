class Pedido:
    def __init__(self, cantidad, cliente):
        self.cliente = cliente 
        self.cantidad = cantidad 

    def imprimir(self):
        print(f"     Cliente: {self.obtener_cliente()}")
        print(f"     Cantidad: {self.obtener_cantidad()}")
        print("     ------------")

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_cliente(self):
        return self.cliente
