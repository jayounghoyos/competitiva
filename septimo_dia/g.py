def solve(coins):
    up_coins = coins.count("U")
    return "YES" if up_coins % 2 != 0 and up_coins != 0 else "NO"

def main():
    cases = int(input())
    while cases:
        _ = input()
        coins = input()
        print(solve(coins))
        cases -= 1

main()