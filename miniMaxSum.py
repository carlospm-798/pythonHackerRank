#   Carlos Paredes Márquez
#   Mini-Max Sum
#   Task: Given five positive integers, find the minimum
#   and maximum values that can be calculated by summing
#   exactly four of the five integers. Then print the 
#   respective minimum and maximum values as a single line
#   of two space-separated long integers.

def miniMaxSum(arr):
    arr = list(arr)
    arr.sort()
    
    minSum = 0
    maxSum = 0

    for i in range(0, len(arr) - 1):
        minSum += int(arr[i])
    
    for i in range(1, len(arr)):
        maxSum += int(arr[i])

    print(f"{minSum} {maxSum}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

'''
Example
arr = [1,3,5,7,9]
The minimum sum is  and the maximum sum is . The function prints

16 24
'''