

class Cliente:
    def __init__(self, nombre, apellido, edad, saldo=0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.saldo = saldo
        
    def comprar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad 
            return f"Compra realizada por {cantidad} unidades"
        else:
            return "Saldo insuficiente"  
        
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Edad: {self.edad}, Saldo: {self.saldo}"
           