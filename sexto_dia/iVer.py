def solve(n):
    initial = [1,1]
    end = [1, 1]
    ## puedo reducir el ciclo a la mitad
    for i in range(2,6):
        if n % i == 0 and end == [1,1]:
            for j in range(5, 1, -1):
                if n % j == 0:
                    end[0] = j
                    break
            end[1] = n // end[0]
            break


    ans = (end[0] - 1) + (end[1] - 1)
    if ans == 0:
        return n - 1
    else:
        return ans


def main():
    n = int(input())

    print(solve(n))

main()