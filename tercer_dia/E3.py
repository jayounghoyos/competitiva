cases = int(input())

def functionE():
    for i in range(cases):
        n1, n2 = input().split()
        n1, n2 = int(n1), int(n2)
        iguales = True

        if n1 % 2 != 0 and n2 % 2 == 0 or n1 % 2 == 0 and n2 % 2 != 0:
            iguales = False

        if n2 <= n1 and iguales:
            print("Yes")
        elif n2 <= n1 and iguales is False:
            print("No")
        elif n2 > n1:
            print("No")


if __name__ == '__main__':
    functionE()