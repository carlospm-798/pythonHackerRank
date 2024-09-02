#   Given x, y, z and N, we should print all results that are not
#   a sum equal to N. It must be shorter or larger than N.

def permutation(xyz, n):

    solutions = []
    i = 0; j = 0; k = 0; sum = 0

    while (i <= xyz[0]):
        while (j <= xyz[1]):
            while (k <= xyz[2]):
                sum = i + j + k

                if sum < n or sum > n:
                    perm = [i, j, k]
                    solutions.append(perm)

                k += 1
            k = 0
            j += 1
        j = 0
        k = 0
        i += 1
    
    print(solutions)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print("\n\n")

    xyz = [x, y, z]
    permutation(xyz, n)


'''
Sample Input 0

1
1
1
2

Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

'''