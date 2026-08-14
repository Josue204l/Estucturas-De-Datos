class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None
 
 
class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0
 
    # ---------- #1 -----------
 
    def esta_vacia(self):
        return self.cabeza is None
 
    def cantidadDeelementos(self):
        return self.tamaño
 
    # ---------- inserciones ----------
 
    def agregara_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamaño += 1
 
    def insertard_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamaño += 1
 
    def insertar_medio(self, valor, posicion):
        if posicion < 0 or posicion > self.tamaño:
            print("Posición inválida.")
            return
        if posicion == 0:
            self.agregara_al_inicio(valor)
            return
        if posicion == self.tamaño:
            self.insertard_final(valor)
            return
 
        nuevo_nodo = Nodo(valor)
        actual = self.cabeza
        for _ in range(posicion - 1):
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        nuevo_nodo.anterior = actual
        actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo
        self.tamaño += 1
 
    # ---------- eliminaciones ----------
 
    def eliminar_inicio(self):
        if self.esta_vacia():
            print("No se puede eliminar, la lista está vacía.")
            return None
 
        valor_eliminado = self.cabeza.valor
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self.tamaño -= 1
        return valor_eliminado
 
    def EliminmarFinal(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return None
 
        valor_eliminado = self.cola.valor
        if self.cabeza != self.cola:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        else:
            self.cabeza = None
            self.cola = None
        self.tamaño -= 1
        return valor_eliminado
 
    def eliminar_medio(self, posicion):
        if self.esta_vacia():
            print("No se puede eliminar, la lista está vacía.")
            return None
        if posicion < 0 or posicion >= self.tamaño:
            print("Posición inválida.")
            return None
        if posicion == 0:
            return self.eliminar_inicio()
        if posicion == self.tamaño - 1:
            return self.EliminmarFinal()
 
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
 
        valor_eliminado = actual.valor
        anterior = actual.anterior
        siguiente = actual.siguiente
 
        anterior.siguiente = siguiente
        siguiente.anterior = anterior  
 
        self.tamaño -= 1
        return valor_eliminado
 
    def vaciar(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0
 
    # ---------- consultas ----------
 
    def buscarElemento(self, valor):
        if self.esta_vacia():
            print("La lista está vacía.")
            return None
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1
 
    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.tamaño:
            print("Posición inválida.")
            return None
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        return actual.valor
 
    def actualizar(self, posicion, valor):
        if posicion < 0 or posicion >= self.tamaño:
            print("Posición inválida.")
            return False
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        actual.valor = valor
        return True
 
    def invertir(self):
        actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior  
 
    # ---------- recorridos / impresión ----------
 
    def recorrer_adelante(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" ")
            actual = actual.siguiente
        print()
 
    def imprimirAtras(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        actual = self.cola
        while actual:
            print(actual.valor, end=" ")
            actual = actual.anterior
        print("None")
 
 
if __name__ == "__main__":
    lista = ListaDobleEnlazada()
 
    print("¿Vacía?", lista.esta_vacia())
    lista.agregara_al_inicio(5)
    lista.agregara_al_inicio(10)
    lista.agregara_al_inicio(15)
    print()
    print("Adelante: ", end="")
    print()
    lista.recorrer_adelante()
    print()
    print("Atrás: ", end="")
    print()
    lista.imprimirAtras()
    print(f"La lista tiene {lista.cantidadDeelementos()} elementos.")
    print()
    lista.EliminmarFinal()
    print("Tras eliminar final: ", end="")
    print()
    lista.recorrer_adelante()
    print()
    print("Posición de 10:", lista.buscarElemento(10))
    print()
    lista.insertard_final(100)
    print()
    lista.insertar_medio(99, 1)
    print()
    print("Tras insertar_medio y insertard_final: ", end="")
    print()
    lista.recorrer_adelante()
    print()
 
    print("obtener(1):", lista.obtener(1))
    lista.actualizar(1, 999)
    print()
    print("Tras actualizar(1, 999): ", end="")
    lista.recorrer_adelante()
    print()
    print("eliminar_medio(1):", lista.eliminar_medio(1))
    print("Tras eliminar_medio(1): ", end="")
    print()
    lista.recorrer_adelante()
    print()
    lista.invertir()
    print("Tras invertir: ", end="")
    lista.recorrer_adelante()
    print()
 
    lista.vaciar()
    print("¿Vacía tras vaciar()?", lista.esta_vacia())
    print()
 
