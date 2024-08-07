# Carlos Paredes Márquez
# August 7th, 2024
# Task, write a number in the input, and then
# print all non-negatice integers i < n, i^2

def solution(n):

    for i in range(n):
        print(i**2)
    

if __name__ == '__main__':
    n = int(input())
    solution(n)