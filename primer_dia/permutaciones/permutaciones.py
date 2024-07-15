n = list(range(1, int(input())+1))

print(n, "\n")

if n in range(2,4):
    print("NO SOLUTION")
elif n == 1:
    print(n)
else:
    for i in n:
        n[i] = 0
        print(n)