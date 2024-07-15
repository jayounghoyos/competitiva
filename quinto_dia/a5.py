def main():
    n_listas = int(input())
    lista_total = []

    for _ in range(0, n_listas):
        # tamaño en el momento
        string = input()
        lista_total.append(string)

    lista_total.sort(key=lambda s: len(s))

    cumple = True
    for i in range(0, n_listas - 1):
        current = lista_total[i]
        next = lista_total[i + 1]

        if next.find(current) == -1:
            cumple = False
            break

    if cumple:
        print("YES")
        print(*lista_total, sep="\n")
    else:
        print("NO")


if __name__ == "__main__":
    main()
