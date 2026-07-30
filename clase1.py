class Node:
    def __init__(self, valor):
        self.data = valor
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insertar al final
    def insert(self, valor):
        new_node = Node(valor)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insertar al inicio
    def insert_at_beginning(self, valor):
        new_node = Node(valor)
        new_node.next = self.head
        self.head = new_node

    # Insertar en la mitad
    def insert_at_middle(self, valor):
        contador = 0
        current = self.head
        while current:
            contador += 1
            current = current.next
        middle = contador // 2
        new_node = Node(valor)
        if self.head is None:
            self.head = new_node
            return
        if middle == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(middle - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Mostrar lista
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Eliminar en posición
    def eliminarEnPosicion(self, posicion):
        if self.head is None:
            print("La lista está vacía.")
            return
        if posicion == 0:
            self.head = self.head.next
            return
        actual = self.head
        contador = 0
        while actual.next is not None and contador < posicion - 1:
            actual = actual.next
            contador += 1
        if actual.next is None:
            print("Posición fuera de rango.")
            return
        actual.next = actual.next.next

    # Eliminar el primer nodo
    def eliminarInicio(self):
        if self.head is None:
            print("La lista está vacía.")
            return
        self.head = self.head.next

    def queHace(self):
        # Esta función elimina el último nodo de la lista (eliminar al final)
        if self.head is None:
            print("La lista está vacía.")
            return

        if self.head.next is None:
            self.head = None
            return

        actual = self.head

        while actual.next.next is not None:
            actual = actual.next

        actual.next = None

    # Determinar si la lista está vacía
    def esVacia(self):
        return self.head is None

    # Buscar un elemento dentro de la lista
    def buscar(self, valor):
        actual = self.head
        posicion = 0
        while actual:
            if actual.data == valor:
                return posicion
            actual = actual.next
            posicion += 1
        return -1


import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    lista1 = SinglyLinkedList()

    while True:
        limpiar_pantalla()
        print("\n--- MENÚ LISTA ENLAZADA ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Insertar en el medio")
        print("4. Eliminar al inicio")
        print("5. Eliminar en una posición")
        print("6. Eliminar al final")
        print("7. Verificar si la lista está vacía")
        print("8. Buscar un elemento")
        print("9. Mostrar lista")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                valor = int(input("Valor a insertar al inicio: "))
                lista1.insert_at_beginning(valor)

            case "2":
                valor = int(input("Valor a insertar al final: "))
                lista1.insert(valor)

            case "3":
                valor = int(input("Valor a insertar en el medio: "))
                lista1.insert_at_middle(valor)

            case "4":
                lista1.eliminarInicio()

            case "5":
                pos = int(input("Posición a eliminar: "))
                lista1.eliminarEnPosicion(pos)

            case "6":
                lista1.queHace()

            case "7":
                print("¿Está vacía?:", lista1.esVacia())

            case "8":
                valor = int(input("Valor a buscar: "))
                resultado = lista1.buscar(valor)
                if resultado == -1:
                    print("Elemento no encontrado.")
                else:
                    print(f"Elemento encontrado en la posición {resultado}")

            case "9":
                lista1.display()

            case "0":
                print("Saliendo...")
                break

            case _:
                print("Opción no válida.")

        input("\nPresiona ENTER para continuar...")


menu()