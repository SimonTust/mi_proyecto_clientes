# -*- coding: utf-8 -*-


import json
from clientes import Cliente

# Cargar datos de clientes desde clientes.json
def cargar_clientes():
    with open("clientes.json", "r") as archivo:
        clientes = json.load(archivo)
    return clientes

# Guardar datos de clientes en clientes.json
def guardar_clientes(clientes):
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo, indent=4)

if __name__ == "__main__":
    clientes = cargar_clientes()

    for cliente_data in clientes:
        cliente = Cliente(cliente_data["nombre"], cliente_data["apellido"], cliente_data["edad"], cliente_data["saldo"])
        print(cliente)

        # Ejemplo de compra (dentro del bucle)
        resultado = cliente.comprar(50)
        print(resultado)
    
        # Guardar los datos actualizados de los clientes (también dentro del bucle)
        guardar_clientes(clientes)

