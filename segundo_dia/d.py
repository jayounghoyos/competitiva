_ = input()
n = list(set(map(int, input().split())))
n.sort()

if len(n) == 1:
    print("NO")
else:
    print(n[1])