#   Carlos Paredes Márquez
#   Birthday Cake Candles
#   Task: You are in charge of the cake for 
#   a child's birthday. You have decided the 
#   cake will have one candle for each year 
#   of their total age. They will only be able 
#   to blow out the tallest of the candles. 
#   Count how many candles are tallest.

def birthdayCakeCandles(candles):
    candles.sort()
    return candles.count(candles[-1])


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()


'''
Sample Input 0

4
3 2 1 3

Sample Output 0

2
'''