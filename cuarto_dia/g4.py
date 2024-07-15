tamaño_casos = int(input())
for i in range(0,tamaño_casos):
    jugadores = list(map(int, input().split(" ")))
    aux = jugadores.copy()
    aux.sort()
    mayor = aux[-1]
    segundomayor = aux[-2]
    if jugadores[0] == mayor and jugadores[1] != segundomayor:
        print("YES")
    elif jugadores[0] == segundomayor and jugadores[1] != mayor:
        print("YES")
    elif jugadores[1] == mayor and jugadores[0] != segundomayor:
        print("YES")
    elif jugadores[1] == segundomayor and jugadores[0] != mayor:
        print("YES")
    else:
        print("NO")