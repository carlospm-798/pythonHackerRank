#   Carlos Paredes Márquez
#   Chocolate fest
#   Task: Complete the chocolateFeast function

#   I do not complete all the cases by myself, in 
#   this specific I look for some other solutions.

def chocolateFeast(n, c, m):
    result = n//c

    wrappers = result
    while (wrappers >= m):
        newChocolates = wrappers//m
        module = wrappers%m
        
        wrappers = newChocolates + module
        result += newChocolates
    
    return result
        


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)
        print(result)
        #fptr.write(str(result) + '\n')
    #fptr.close()