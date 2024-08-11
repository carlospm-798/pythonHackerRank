#   Carlos Paredes Márquez
#   Plus Minus
#   Task: Given an array of integers, calculate the ratios
#   of its elements that are positive, negative, and zero.
#   print the decimal value of each fraction on a new line
#   with 6 places after the decimal

def plusMinus(arr):
    n = len(arr)

    positive = 0
    negative = 0
    zero = 0

    for i in range(n):
        if (int(arr[i]) > 0):
            positive += 1
        elif (int(arr[i]) < 0):
            negative += 1
        elif (int(arr[i]) == 0):
            zero += 1
    
    result = positive/n
    print(f"{result:.6f}")
    result = negative/n
    print(f"{result:.6f}")
    result = zero/n
    print(f"{result:.6f}")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)