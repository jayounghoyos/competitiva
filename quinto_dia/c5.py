from pprint import pprint 

def main():
    num_lakes = int(input())

    for _ in range(0, num_lakes):
        n, m = list(map(int, input().split(" ")))
        current_lake = []
        for n in range(0, n):
            current_lake.append(list(map(int, input().split(" "))))
        
        print("Current Lake")
        pprint(current_lake)
        print("__"*10)


        for i in current_lake:
            for j in i:
                print(i)
                print(j)
        
        print("____"*10)



if __name__ == "__main__":
    main()


"""Este ejercicio lo dejó hasta terminar el I(secret combination)"""