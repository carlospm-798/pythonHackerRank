#   Amazon is offerng a discount on every purchase of a pair of 
#   products whose cost sum is divisible by x. Given the cost of 
#   n products in the store, find the number of pairs (i,j) where i<j 
#   and cost[i] + cost[j] is divisible by x.

def getPairs(x, cost):

    result = 0
    l = len(cost)

    for i in range(l):
        for j in range(i+1, l):
            sum = cost[i] + cost[j]
            if sum%x == 0:
                result += 1
    
    return result

if __name__ == '__main__':

    x = int(input().strip())
    cost_count = int(input().strip())

    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    result = getPairs(x, cost)
    print(result)