#Danny Isaac Pérez Zamora
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
        if self.estaVacia():
            self.inicio = nuevo
            self.final = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo

    # Insertar un nodo al final
    def insertarFinal(self, dato):
        nuevo = Nodo(dato)
        if self.estaVacia():
            self.inicio = nuevo
            self.final = nuevo
        else:
            nuevo.anterior = self.final
            self.final.siguiente = nuevo
            self.final = nuevo

    # Insertar un nodo en una posicion determinada
    def insertarMedio(self, dato, posicion):
        if posicion == 0:
            self.insertarInicio(dato)
            return

        nuevo = Nodo(dato)
        actual = self.inicio
        contador = 0

        while actual is not None and contador < posicion:
            actual = actual.siguiente
            contador += 1

        if actual is None:
            self.insertarFinal(dato)
            return

        anterior = actual.anterior
        nuevo.anterior = anterior
        nuevo.siguiente = actual
        anterior.siguiente = nuevo
        actual.anterior = nuevo

    # Eliminar el nodo del inicio
    def eliminarInicio(self):
        if self.estaVacia():
            print("La lista esta vacia")
            return

        eliminado = self.inicio

        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            self.inicio = self.inicio.siguiente
            self.inicio.anterior = None

        print("Elemento eliminado:", eliminado.dato)

    # Eliminar un nodo de una posicion determinada
    def eliminarMedio(self, posicion):
        if self.estaVacia():
            print("La lista esta vacia")
            return

        if posicion == 0:
            self.eliminarInicio()
            return

        actual = self.inicio
        contador = 0

        while actual is not None and contador < posicion:
            actual = actual.siguiente
            contador += 1

        if actual is None:
            print("Posicion no valida")
            return

        if actual == self.final:
            self.final = actual.anterior
            self.final.siguiente = None
        else:
            anterior = actual.anterior
            siguiente = actual.siguiente
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
# PROGRAMA PRINCIPAL (demo) - solo corre si ejecutas
# este archivo directamente, NO cuando se importa
# --------------------------------------------------
if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()

    lista.insertarFinal(10)
    lista.insertarFinal(20)
    lista.insertarFinal(30)

    print("Lista inicial:")
    lista.mostrarAdelante()

    print("\nInsertar al inicio:")
    lista.insertarInicio(5)
    lista.mostrarAdelante()

    print("\nInsertar al final:")
    lista.insertarFinal(40)
    lista.mostrarAdelante()

    print("\nInsertar 15 en la posicion 2:")
    lista.insertarMedio(15, 2)
    lista.mostrarAdelante()

    print("\nRecorrer la lista hacia atras:")
    lista.mostrarAtras()

    print("\nEliminar al inicio:")
    lista.eliminarInicio()
    lista.mostrarAdelante()

    print("\nEliminar el elemento de la posicion 2:")
    lista.eliminarMedio(2)
    lista.mostrarAdelante()

    print("\nLista final hacia atras:")
    lista.mostrarAtras()

    print("\nNúmero de elementos en la lista:", lista.contarElementos())
