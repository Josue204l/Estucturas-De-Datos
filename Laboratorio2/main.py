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
    """Crea (o sobrescribe) Reporte.txt en la misma carpeta del script."""
    with open("Reporte.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Reporte de Clima - Costa Rica\n")
        archivo.write("Laboratorio #2 - Estructura de Datos\n")
        archivo.write("Integrantes:\n")
        for nombre in INTEGRANTES:
            archivo.write(f"- {nombre}\n")
        archivo.write("\n")
        archivo.write(f"Cantidad de datos analizados: {cantidad}\n")
        archivo.write(f"Temperatura promedio: {promedio:.2f}\n")
        archivo.write(f"Temperatura mayor: {mayor}\n")
        archivo.write(f"Temperatura menor: {menor}\n")


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
