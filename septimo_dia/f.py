def main():

    stringA = list(input())
    stringB = list(input())

    # lcs -> Longest common string
    lcs = []

    # minimo con el que vamos a recorrer
    if len(stringB) >= len(stringA):
        maximo = stringB
        minimo = stringA
    else:
        minimo = stringB
        maximo = stringA
    maximo.sort()
    print("---" * 10)

    valores = []

    for i in minimo:
        count = 0
        for j in minimo:
            if i == j:
                count += 1
        valores.append((i, count))

        # print(f"{i} -> {j}")

        print("__" * 10)

    if len(lcs) == 0:
        print(" ")
    print(lcs)
    for item in valores:
        print(valores)


if __name__ == "__main__":
    main()
