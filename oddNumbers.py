#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers(l, r):
    
    results = []
    
    for i in range(l,r+1):
        
        if (i%2 != 0):
            results.append(i)
        else:
            continue
    
    return results

if __name__ == '__main__':

    l = int(input().strip())
    r = int(input().strip())

    result = oddNumbers(l, r)
    print('\n'.join(map(str, result)))