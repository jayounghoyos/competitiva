import math

def solve2(n, m):
    if n == m:
        return n
    # Buscar el máximo GCD comenzando desde la mitad del rango
    max_gcd = 1
    for k in range(m // 2, 0, -1):
        if m // k - (n - 1) // k > 1:
            max_gcd = k
            break
    return max_gcd

def main():
    n, m = map(int, input().split())
    print(solve2(n, m))

if __name__ == '__main__':
    main()