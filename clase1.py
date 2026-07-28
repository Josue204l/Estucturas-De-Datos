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
            temp = self.head
            self.head = self.head.next
            del temp
            return
        actual = self.head
        contador = 0
        while actual.next is not None and contador < posicion - 1:
            actual = actual.next
            contador += 1
        if actual.next is None:
            print("Posición fuera de rango.")
            return
        temp = actual.next
        actual.next = temp.next
        del temp

    # Eliminar el primer nodo
    def eliminarInicio(self):
        # Verificar si la lista está vacía
        if self.head is None:
            print("La lista está vacía.")
            return
        temp = self.head
        self.head = self.head.next
        del temp


    def queHace (self):

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



# ---------- PRUEBAS ----------
lista1 = SinglyLinkedList()

lista1.insert(10)
lista1.insert(20)
lista1.insert(30)
lista1.insert(40)
lista1.insert(50)
lista1.insert(60)

print("Lista original:")
lista1.display()

lista1.insert_at_beginning(1)
print("\nDespués de insertar 1 al inicio:")
lista1.display()

lista1.insert_at_middle(99)
print("\nDespués de insertar 99 en la mitad:")
lista1.display()

# ------ PRUEBAS DE ELIMINACIÓN ------
lista1.eliminarEnPosicion(2)
print("\nDespués de eliminar el nodo en la posición 2:")
lista1.display()

lista1.eliminarInicio()
print("\nDespués de eliminar el nodo del inicio:")
lista1.display()

lista1.queHace()
print("\n Ver lo que hace:")
lista1.display()    