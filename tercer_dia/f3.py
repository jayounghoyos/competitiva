def median(tamaño,pasos,arr):

    mitad = (tamaño//2)
    while pasos >= 0:
        medianum = arr[mitad]
        if pasos == 0:
            break
        else:
            arr[mitad] +=1
            if (len(arr) > 1) and (not (arr[mitad]) < arr[mitad+1]):
                aux = arr.pop(mitad)
                arr.append(aux)
        pasos-=1
    return medianum

def main():
    tamaño, pasos = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(median(tamaño,pasos, arr))

if __name__ == '__main__':
    main()