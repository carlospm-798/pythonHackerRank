# Carlos Paredes Márquez
# August 7th, 2024
# Readen an integer, n, representate the consecutive 
# values in between. Exmple: n=5, output: 12345

def between(n):

    output = ''
    for i in range(1, n+1):
        output += str(i)
    
    return output

if __name__ == '__main__':
    n = int(input())
    print(between(n))
