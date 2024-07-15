import math


def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def solve(n):
    end = [1, 1]

    if is_square(n) == True:
        return round((math.sqrt(n) - 1) + (math.sqrt(n) - 1))
    else:
        for i in range(2, n + 1):
            if n % i == 0 and end == [1, 1]:
                for j in range(2, n + 1):
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
