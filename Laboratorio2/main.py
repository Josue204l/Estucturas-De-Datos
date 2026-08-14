from Clase3 import ListaDoblementeEnlazada

INTEGRANTES = [
    "Jonathan Josué Rojas Estrada",
    "Danny Isaac Pérez Zamora",
]


def leer_datos(nombre_archivo, lista):
    """Lee el archivo de temperaturas (una por línea) y las inserta
    al final de la lista doblemente enlazada."""
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                lista.insertarFinal(int(linea))


def calcular_promedio(lista):
    """Recorre la lista y calcula el promedio de las temperaturas."""
    if lista.estaVacia():
        return 0
    suma = 0
    actual = lista.inicio
    while actual is not None:
        suma += actual.dato
        actual = actual.siguiente
    return suma / lista.contarElementos()


def temperatura_mayor(lista):
    """Recorre la lista y devuelve la temperatura más alta."""
    if lista.estaVacia():
        return None
    mayor = lista.inicio.dato
    actual = lista.inicio.siguiente
    while actual is not None:
        if actual.dato > mayor:
            mayor = actual.dato
        actual = actual.siguiente
    return mayor


def temperatura_menor(lista):
    """Recorre la lista y devuelve la temperatura más baja."""
    if lista.estaVacia():
        return None
    menor = lista.inicio.dato
    actual = lista.inicio.siguiente
    while actual is not None:
        if actual.dato < menor:
            menor = actual.dato
        actual = actual.siguiente
    return menor


from Clase3 import ListaDoblementeEnlazada

INTEGRANTES = [
    "Jonathan Josué Rojas Estrada",
    "Danny Isaac Pérez Zamora",
]


def leer_datos(nombre_archivo, lista):
    """Lee el archivo de temperaturas (una por línea) y las inserta
    al final de la lista doblemente enlazada."""
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                lista.insertarFinal(int(linea))


def calcular_promedio(lista):
    """Recorre la lista y calcula el promedio de las temperaturas."""
    if lista.estaVacia():
        return 0
    suma = 0
    actual = lista.inicio
    while actual is not None:
        suma += actual.dato
        actual = actual.siguiente
    return suma / lista.contarElementos()


def temperatura_mayor(lista):
    """Recorre la lista y devuelve la temperatura más alta."""
    if lista.estaVacia():
        return None
    mayor = lista.inicio.dato
    actual = lista.inicio.siguiente
    while actual is not None:
        if actual.dato > mayor:
            mayor = actual.dato
        actual = actual.siguiente
    return mayor


def temperatura_menor(lista):
    """Recorre la lista y devuelve la temperatura más baja."""
    if lista.estaVacia():
        return None
    menor = lista.inicio.dato
    actual = lista.inicio.siguiente
    while actual is not None:
        if actual.dato < menor:
            menor = actual.dato
        actual = actual.siguiente
    return menor


def generar_reporte(promedio, mayor, menor, cantidad):
    with open("Reporte.txt", "w", encoding="utf-8") as archivo:
        archivo.write("====================================\n")
        archivo.write(" REPORTE DE TEMPERATURAS\n")
        archivo.write("====================================\n\n")

        archivo.write("Cantidad de temperaturas: " + str(cantidad) + "\n")
        archivo.write("Nombre: Jonathan Josué Rojas Estrada\n")
        archivo.write("Nombre: Danny Isaac Pérez Zamora\n")

        archivo.write("Temperatura promedio: " + str(promedio) + "\n")
        archivo.write("Temperatura mayor: " + str(mayor) + "\n")
        archivo.write("Temperatura menor: " + str(menor) + "\n")


if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()

    leer_datos("datos.txt", lista)

    promedio = calcular_promedio(lista)
    mayor = temperatura_mayor(lista)
    menor = temperatura_menor(lista)

    generar_reporte(promedio, mayor, menor, lista.contarElementos())

    print("Reporte generado exitosamente como Reporte.txt")
    print(f"Cantidad de datos: {lista.contarElementos()}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mayor: {mayor}")
    print(f"Menor: {menor}")


if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()

    leer_datos("datos.txt", lista)

    promedio = calcular_promedio(lista)
    mayor = temperatura_mayor(lista)
    menor = temperatura_menor(lista)

    generar_reporte(promedio, mayor, menor, lista.contarElementos())

    print("Reporte generado exitosamente como Reporte.txt")
    print(f"Cantidad de datos: {lista.contarElementos()}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mayor: {mayor}")
    print(f"Menor: {menor}")
