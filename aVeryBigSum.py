#   Carlos Paredes Márquez
#   a very big sum
#   Task: In this challenge, you are required 
#   to calculate and print the sum of the elements 
#   in an array, keeping in mind that some of those 
#   integers may be quite large.

def aVeryBigSum(ar):
    result = 0

    for i in range(len(ar)):
        result += int(ar[i])

    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()

'''

Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005

Output

5000000015

'''