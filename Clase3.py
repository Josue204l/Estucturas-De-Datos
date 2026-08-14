# Clase Nodo
# Cada nodo guarda un dato y dos referencias:
# anterior -> apunta al nodo anterior
# siguiente -> apunta al nodo siguiente

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


# Clase ListaDoblementeEnlazada
# Se encarga de manejar todos los nodos de la lista

class ListaDoblementeEnlazada:
    def __init__(self):
        self.inicio = None
        self.final = None

    # Verifica si la lista esta vacia
    def estaVacia(self):
        return self.inicio is None

    # Insertar un nodo al inicio
    def insertarInicio(self, dato):
        nuevo = Nodo(dato)

        # Si la lista esta vacia, el nuevo nodo
        # sera tanto el inicio como el final
        if self.estaVacia():
            self.inicio = nuevo
            self.final = nuevo
        else:
            # El nuevo nodo apunta al inicio actual
            nuevo.siguiente = self.inicio

            # El inicio actual apunta hacia atras
            # al nuevo nodo
            self.inicio.anterior = nuevo

            # Ahora el nuevo nodo es el inicio
            self.inicio = nuevo

    # Insertar un nodo al final
    def insertarFinal(self, dato):
        nuevo = Nodo(dato)

        # Si la lista esta vacia
        if self.estaVacia():
            self.inicio = nuevo
            self.final = nuevo
        else:
            # El nuevo nodo apunta hacia atras
            # al nodo que actualmente es el final
            nuevo.anterior = self.final

            # El nodo final apunta hacia adelante
            # al nuevo nodo
            self.final.siguiente = nuevo

            # Ahora el nuevo nodo es el final
            self.final = nuevo

    # Insertar un nodo en una posicion determinada
    def insertarMedio(self, dato, posicion):
        # Si la posicion es 0, insertamos al inicio
        if posicion == 0:
            self.insertarInicio(dato)
            return

        nuevo = Nodo(dato)
        actual = self.inicio
        contador = 0

        # Avanzamos hasta llegar a la posicion
        # donde queremos insertar
        while actual is not None and contador < posicion:
            actual = actual.siguiente
            contador += 1

        # Si llegamos al final, insertamos al final
        if actual is None:
            self.insertarFinal(dato)
            return

        # Guardamos el nodo anterior al actual
        anterior = actual.anterior

        # Conectamos el nuevo nodo con los nodos vecinos
        nuevo.anterior = anterior
        nuevo.siguiente = actual

        # Actualizamos las conexiones de los nodos vecinos
        anterior.siguiente = nuevo
        actual.anterior = nuevo

    # Eliminar el nodo del inicio
    def eliminarInicio(self):
        if self.estaVacia():
            print("La lista esta vacia")
            return

        # Guardamos temporalmente el nodo que vamos a eliminar
        eliminado = self.inicio

        # Si solo existe un nodo
        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            # El segundo nodo pasa a ser el inicio
            self.inicio = self.inicio.siguiente

            # El nuevo inicio ya no tiene nodo anterior
            self.inicio.anterior = None

        print("Elemento eliminado:", eliminado.dato)

    # Eliminar un nodo de una posicion determinada
    def eliminarMedio(self, posicion):
        if self.estaVacia():
            print("La lista esta vacia")
            return

        # Si queremos eliminar el primero
        if posicion == 0:
            self.eliminarInicio()
            return

        actual = self.inicio
        contador = 0

        # Buscamos el nodo de la posicion indicada
        while actual is not None and contador < posicion:
            actual = actual.siguiente
            contador += 1

        # Si no encontramos el nodo
        if actual is None:
            print("Posicion no valida")
            return

        # Si el nodo es el final
        if actual == self.final:
            self.final = actual.anterior
            self.final.siguiente = None
        else:
            # Guardamos los nodos vecinos
            anterior = actual.anterior
            siguiente = actual.siguiente

            # Saltamos el nodo que queremos eliminar
            anterior.siguiente = siguiente
            siguiente.anterior = anterior

        print("Elemento eliminado:", actual.dato)

    # Mostrar la lista desde el inicio hasta el final
    def mostrarAdelante(self):
        actual = self.inicio

        print("Lista hacia adelante:")

        while actual is not None:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente

        print("None")

    # Mostrar la lista desde el final hasta el inicio
    def mostrarAtras(self):
        actual = self.final

        print("Lista hacia atras:")

        while actual is not None:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior

        print("None")
    # Contar el número de elementos en la lista
    def contarElementos(self):
        actual = self.inicio
        contador = 0

        while actual is not None:
            contador += 1
            actual = actual.siguiente

        return contador

# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

lista = ListaDoblementeEnlazada()

# Insertamos algunos elementos
lista.insertarFinal(10)
lista.insertarFinal(20)
lista.insertarFinal(30)

print("Lista inicial:")
lista.mostrarAdelante()

# Insertar al inicio
print("\nInsertar al inicio:")
lista.insertarInicio(5)
lista.mostrarAdelante()

# Insertar al final
print("\nInsertar al final:")
lista.insertarFinal(40)
lista.mostrarAdelante()

# Insertar al medio
print("\nInsertar 15 en la posicion 2:")
lista.insertarMedio(15, 2)
lista.mostrarAdelante()

# Mostrar hacia atras
print("\nRecorrer la lista hacia atras:")
lista.mostrarAtras()

# Eliminar al inicio
print("\nEliminar al inicio:")
lista.eliminarInicio()
lista.mostrarAdelante()

# Eliminar al medio
print("\nEliminar el elemento de la posicion 2:")
lista.eliminarMedio(2)
lista.mostrarAdelante()

# Mostrar nuevamente hacia atras
print("\nLista final hacia atras:")
lista.mostrarAtras()

# Contar elementos
print("\nNúmero de elementos en la lista:", lista.contarElementos())
