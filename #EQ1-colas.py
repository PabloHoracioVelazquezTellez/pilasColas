from collections import deque

class BancoMultiFila:
    def __init__(self, num_cajas, capacidad_por_caja):
        self.cajas=[deque() for _ in range(num_cajas)] #Definimos una lista de listas para almacenar los datos
        self.capacidad_por_caja = capacidad_por_caja

    def insertarCliente(self, cliente, caja):
        if 0<=caja<len(self.cajas): #validamos que la cola a modificar exista
            if not self.colaLlena(caja): #validamos que la cola tenga espacio disponible
                self.cajas[caja].append(cliente) #Para agregar datos en la cola usamos la funcion append de la clase deque
                print(f"Cliente {cliente} agregado a la caja {caja}.")
            else:
                print(f"La caja {caja} ya está en su capacidad máxima.")
        else:
            print("Número de caja inválido.")

    def eliminarCliente(self, caja):
        if 0<=caja<len(self.cajas): #validamos que la cola exista
            if not self.colaVacia(caja):#validamos que haya datos que borrar en la cola
                cliente = self.cajas[caja].popleft() #la funcion popleft de la clase deque elimina el primer dato a a la izquierda de la cola
                print(f"Atendiendo a {cliente} en la caja {caja}.")
            else:
                print(f"No hay clientes en la caja {caja}.")
        else:
            print("Número de caja inválido.")

    def consultarPrimerCliente(self, caja):
        if 0<=caja<len(self.cajas):#validamos que la cola exista
            if not self.colaVacia(caja):#validamos que la cola contenga datos
                print(f"Primer cliente en la caja {caja}: {self.cajas[caja][0]}")#consultamos el primer dato de la cola "caja"_0
            else:
                print(f"La caja {caja} está vacía.")
        else:
            print("Número de caja inválido.")

    def consultarUltimoCliente(self, caja):
        if 0<=caja<len(self.cajas):#validamos que la cola exista
            if not self.colaVacia(caja):#validamos que la cola contenga datos
                print(f"Último cliente en la caja {caja}: {self.cajas[caja][-1]}")#el subindice -1 cumple una funcion similar a peek en pilas
            else:
                print(f"La caja {caja} está vacía.")
        else:
            print("Número de caja inválido.")

    def colaVacia(self, caja):
        if 0<=caja<len(self.cajas):#validamos que la cola exista
            return len(self.cajas[caja])==0#comparamos la longitud de la cola, si es 0 devuelve un valor True
        else:
            print("Número de caja inválido.")
            return True

    def colaLlena(self, caja):
        if 0<=caja< len(self.cajas):#validamos que la cola exista
            return len(self.cajas[caja])>=self.capacidad_por_caja#comparamos la longitud de la cola con la capacidad de la caja
        else:                                                   #si es igual, devolvemos un valor True
            print("Número de caja inválido.")
            return False

    def recorrerCola(self, caja):
        if 0<=caja<len(self.cajas):#validamos que la cola exista
            print(f"Caja {caja}: {' <- '.join(self.cajas[caja]) if self.cajas[caja] else 'Vacío'}")
        else:
            print("Número de caja inválido.")

    def recorrerColaDeColas(self):
        print("\nEstado de todas las cajas:")
        for i, cola in enumerate(self.cajas):#usando la clase enumerate imprimimos un iterado de cada cola y sus datos
            print(f"Caja {i}: {' <- '.join(cola) if cola else 'Vacío'}")
        print()

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Insertar cliente en una caja")
    print("2. Eliminar (atender) al primer cliente de una caja")
    print("3. Ver el estado de una caja")
    print("4. Ver el estado de todas las cajas")
    print("5. Verificar si una caja está vacía")
    print("6. Verificar si una caja está llena")
    print("7. Consultar el primer cliente de una caja")
    print("8. Consultar el último cliente de una caja")
    print("9. Salir")

def ejecutar_banco():
    banco=BancoMultiFila(num_cajas=3, capacidad_por_caja=3)
    while True:
        mostrar_menu()
        opcion=input("Selecciona una opción: ")

        if opcion=="1":
            caja=int(input("Selecciona el número de caja (0, 1, 2): "))
            cliente=input("Ingresa el nombre del cliente: ")
            banco.insertarCliente(cliente, caja)
        elif opcion=="2":
            caja=int(input("Selecciona el número de caja (0, 1, 2): "))
            banco.eliminarCliente(caja)
        elif opcion=="3":
            caja=int(input("Selecciona el número de caja (0, 1, 2): "))
            banco.recorrerCola(caja)
        elif opcion=="4":
            banco.recorrerColaDeColas()
        elif opcion=="5":
            caja=int(input("Selecciona el número de caja (0, 1, 2): "))
            print(f"¿La caja {caja} está vacía? {'Sí' if banco.colaVacia(caja) else 'No'}")
        elif opcion=="6":
            caja=int(input("Selecciona el número de caja (0, 1, 2): "))
            print(f"¿La caja {caja} está llena? {'Sí' if banco.colaLlena(caja) else 'No'}")
        elif opcion=="7":
            caja=int(input("Selecciona el número de caja (0, 1, 2): "))
            banco.consultarPrimerCliente(caja)
        elif opcion=="8":
            caja=int(input("Selecciona el número de caja (0, 1, 2): "))
            banco.consultarUltimoCliente(caja)
        elif opcion=="9":
            print("Saliendo del sistema de banco...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

ejecutar_banco()


#LO DE ABAJO ES PARA ACELERAR EL FUNCIONAMIENTO Y NO HACERLO MANUAL


"""banco = BancoMultiFila(num_cajas=3, capacidad_por_caja=3)

# Insertar clientes en diferentes cajas
banco.insertarCliente("Carlos", 0)
banco.insertarCliente("Ana", 0)
banco.insertarCliente("Luis", 1)
banco.insertarCliente("Maria", 2)
banco.insertarCliente("Jose", 1)

# Intentar agregar más clientes para probar COLA LLENA
banco.insertarCliente("Elena", 0)
banco.insertarCliente("Pedro", 0)  # Debería decir que la caja está llena

# Recorrer todas las colas
banco.recorrerColaDeColas()

# Verificar si las cajas están vacías o llenas
print(f"¿La caja 0 está vacía? {'Sí' if banco.colaVacia(0) else 'No'}")
print(f"¿La caja 0 está llena? {'Sí' if banco.colaLlena(0) else 'No'}")
print(f"¿La caja 2 está vacía? {'Sí' if banco.colaVacia(2) else 'No'}")

# Atender clientes
banco.eliminarCliente(0)
banco.eliminarCliente(1)

# Ver estado después de la atención
banco.recorrerColaDeColas()
"""