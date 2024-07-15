def main():
    cases = int(input())
    while cases:
        _ = input()
        ans = 'D' * 12 + 'L' * 12 + 'U' * 12 + 'RRDD'
        cases -= 1
        print(len(ans))
        print(ans)

main()