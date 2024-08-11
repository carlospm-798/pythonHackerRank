#   Carlos Paredes Márquez
#   Diagonal Difference
#   Task: Given a Square matrix, calculate the absolute 
#   difference between the sums of its diagonals

def diagonalDifference(arr):

    cont = 0
    a = 0
    while (cont < len(arr)):
        a += int(arr[cont][cont])
        cont += 1
    
    cont = 0
    b = 0
    while (cont < len(arr)):
        b += arr[int(len(arr) - 1) - cont][cont]
        cont += 1
    
    return abs(a-b)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()


'''

Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output

15

Explanation

The primary diagonal is:

11
   5
     -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15     

'''