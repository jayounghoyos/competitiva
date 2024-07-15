def solve():
    tuple = list(map(int, input().split(' ')))
    tuple.sort()
    print(tuple)
    cont_teams = 0
    while tuple[0] > 0 and tuple[1] > 0:
        if tuple[0] >= 1 and tuple[1] >= 3:
            tuple[0] -= 1
            tuple[1] -= 3
            tuple.sort()
            cont_teams += 1
        elif tuple[0] >= 2 and tuple[1] >= 2:
            tuple[0] -= 2
            tuple[1] -= 2
            tuple.sort()
            cont_teams += 1
        elif tuple[0] >= 3 and tuple[0] >= 1:
            tuple[0] -= 3
            tuple[1] -= 1
            tuple.sort()
            cont_teams += 1
        else:
            break
    return cont_teams

def main():
    for _ in range(0, int(input())):
        print(solve())


main()