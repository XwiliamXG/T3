lab = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]
]

res = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

filas = 9
columnas = 9
inicio = (8, 0)
fin = (0, 0)
puntaje_objetivo = 23
puntaje_final = 0


def valida(f, c):
    if f < 0:
        return False
    if f >= filas:
        return False
    if c < 0:
        return False
    if c >= columnas:
        return False
    if lab[f][c] == 0:
        return False
    if res[f][c] == 1:
        return False
    return True


def imprimir_res():
    for fila in res:
        for celda in fila:
            print(celda, end=" ")
        print()
    print()


def labbas(fil, col, puntaje):
    global puntaje_final

    if not valida(fil, col):
        return False

    if lab[fil][col] == 3 or lab[fil][col] == 4:
        puntaje += lab[fil][col]

    res[fil][col] = 1
    imprimir_res()

    if (fil, col) == fin:
        if puntaje >= puntaje_objetivo:
            puntaje_final = puntaje
            return True
        else:
            res[fil][col] = 0
            return False

    if labbas(fil - 1, col, puntaje):
        return True
    if labbas(fil, col + 1, puntaje):
        return True
    if labbas(fil + 1, col, puntaje):
        return True
    if labbas(fil, col - 1, puntaje):
        return True

    res[fil][col] = 0  
    return False


encontrado = labbas(inicio[0], inicio[1], 0)


print("Resultado final del recorrido:")
imprimir_res()

if encontrado:
    print("Camino encontrado con", puntaje_final, "puntos.")
else:
    print("No se encontró un camino válido con al menos 23 puntos.")
