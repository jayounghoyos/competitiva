def median(tamaño,pasos,arr):
    medianum = arr[(tamaño//2)]
    while pasos >= 0:
        arr.sort()
        medianum = arr[(tamaño//2)]
        if pasos == 0:
            break
        else:
            arr[(tamaño//2)] +=1
            pasos-=1
    return medianum

def main():
    tamaño, pasos = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"Pasos: {pasos}, lista: {arr}, tamaño: {tamaño}, el de la mitad: {arr[(tamaño//2)]}")
    print(median(tamaño,pasos, arr))

if __name__ == '__main__':
    main()