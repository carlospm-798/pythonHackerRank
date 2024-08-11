#   Carlos Paredes Márquez
#   Staircase
#   Task: Print a staircase with equal base and height, 
#   both equal to n. It is drawn using # symbols and spaces

def staircase(n):

    cont = 0
    while (cont < n):
        result = ''
        cont += 1
        for i in range(n - cont):
            result += ' '
        for i in range(cont):
            result += '#'
        
        print(result)

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)

'''
This is a staircase of size n = 4:

   #
  ##
 ###
####
'''