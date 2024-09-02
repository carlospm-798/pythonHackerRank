def runnerUp(arr):

    n = []

    for element in arr:
        if element not in n:
            n.append(element)
    
    n.sort()
    print(n[-2])

    

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    runnerUp(list(arr))