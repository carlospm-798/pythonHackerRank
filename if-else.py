# Carlos Paredes Márquez
# August 7th, 2024
# Task: given an integer, n, 
# perform the following conditional actions 
# if n is odd, print Weird 
# if n is even and is in the range of 2-5 print Not Weird 
# if n is even and is in the range of 6-20 print print Weird
# if n is even and greater than 20 print Not Weird

def case(n):

    if (n%2 != 0):
        # Odd case
        print("Weird")
    elif (n%2 == 0 and n in range(2,5)):
        # Even case in range 2,5
        print("Not Weird")
    elif (n%2 == 0 and n in range(6,21)):
        # Even case in range 6,20
        print("Weird")
    elif (n%2 == 0 and n > 20):
        # Even case bigger than 20
        print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    case(n)