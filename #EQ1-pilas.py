class EditorTexto:
    def __init__(self, capacidad_maxima=10):
        #AQUI DEFINIMOS UNA PILA A LA CUAL SE LE DEFINE UNA CAPACIDAD MAXIMA EN LA EJECUCION DEL PROGRAMA
        self.pila = []
        self.capacidad_maxima = capacidad_maxima

    def pushEscribir(self, texto):
        #OPERACION PUSH PARA AGREGAR TEXTO
        if not self.pilaLlena():#validamos que la pila tenga espacio
            self.pila.append(texto)#usando el metodo append, equivalente a push agregamos el dato a ala pila
            print(f"Se escribio: '{texto}'")
        else:
            print("PILA LLENA NO SE PUEDE ESCRIBIR MAS...") #SI LA PILA ESTA LLENA YA NO PODEMOS AGREGAR NADA

    def popDeshacer(self):
        #POP PARA BORRAR EL ULTIMO TEXTO ESCRITO
        if not self.pilaVacia():#validamos que la pila tenga datos para borrar
            ultima_accion=self.pila.pop()#usando el metodo pop, eliminamos el ultimo dato ingresado
            print(f"Deshacer: '{ultima_accion}'")
        else:
            print("PILA VACÍA.")

    def peekUltimaAccion(self):
        #PEEK PARA MOSTRAR NUESTRO ULTIMO TEXTO AGREGADO
        if not self.pilaVacia():#validamos que la pila tenga datos para mostrar
            print(f"Ultima accion: '{self.pila[-1]}'")#SE REVISA EL ULTIMO INDICE DE LA LISTA
        else:                                           #el indice -1 cumple la funcion peek en python
            print("PILA VACÍA.")                        #no hay definido un metodo llamada como tal peek

    def pilaVacia(self):
        #VERIFICAMOS EL ESTADO DE LA PILA
        return len(self.pila)==0#si la longitud de la pila es =0 devolvemos True

    def pilaLlena(self):
        #VERIFICAMOS SI LA PILA ESTA LLENA
        return len(self.pila)>=self.capacidad_maxima#si la lingitud de la pila es = a su capacidad, devolcemos True

    def recorrerPila(self):
        #SE MUESTRAN LOS ELEMENTOS DE LA PILA DEL ULTIMO AL PRIMERO
        print("\nHistorial de cambios:")
        if self.pila:
            for i, accion in enumerate(reversed(self.pila), 1): #con la clase reversed damos una iteracion invertida a la pila
                print(f"{i}. {accion}")                         #para mostrar los datos de esta desde el ultimo al primero
        else:
            print("No hay cambios registrados.")
        print()

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Escribir texto")
    print("2. Deshacer última acción")
    print("3. Ver última acción")
    print("4. Ver historial de cambios")
    print("5. Verificar si la pila está vacía")
    print("6. Verificar si la pila está llena")
    print("7. Salir")

# Función principal
def ejecutar_editor():
    editor = EditorTexto(capacidad_maxima=5)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            if editor.pilaLlena():
                print("La pila está llena, no puedes escribir más texto.")
            else:
                texto = input("Ingresa el texto a escribir: ")
                editor.pushEscribir(texto)
        elif opcion == "2":
            if editor.pilaVacia():
                print("La pila está vacía, no hay acciones para deshacer.")
            else:
                editor.popDeshacer()
        elif opcion == "3":
            editor.peekUltimaAccion()
        elif opcion == "4":
            editor.recorrerPila()
        elif opcion == "5":
            if editor.pilaVacia():
                print("La pila está vacía.")
            else:
                print("La pila no está vacía.")
        elif opcion == "6":
            if editor.pilaLlena():
                print("La pila está llena.")
            else:
                print("La pila no está llena.")
        elif opcion == "7":
            print("Saliendo del editor...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

ejecutar_editor()


#LO DE ABAJO ES PARA ACELERAR EL FUNCIONAMIENTO Y NO HACERLO MANUAL
"""
editor = EditorTexto(capacidad_maxima=5)

# Escribir acciones
editor.pushEscribir("Hola")
editor.pushEscribir("Mundo")
editor.pushEscribir("Esto")
editor.pushEscribir("Es")
editor.pushEscribir("Un Editor")
editor.pushEscribir("Esta no se agrega a la pila")  # PILA LLENA

# Verificar si la pila está llena
print(f"¿La pila está llena? {'Si' if editor.pilaLlena() else 'No'}")

# Recorrer pila
editor.recorrerPila()

# Peek y deshacer
editor.peekUltimaAccion()
editor.popDeshacer()

# Ver historial después de deshacer
editor.recorrerPila()
"""