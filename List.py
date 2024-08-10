#   Carlos Paredes Márquez
#   August 09 2024
#   Lists

#   Consider a list (list = []). You can perform the following commands:
#   insert i e: Insert integer  at position .
#   print: Print the list.
#   remove e: Delete the first occurrence of integer .
#   append e: Insert integer  at the end of the list.
#   sort: Sort the list.
#   pop: Pop the last element from the list.
#   reverse: Reverse the list.

def tripleValue(actualList, index, value):
    
    actualList.insert(int(index), int(value))
    return actualList
        

def doubleValue(instruction, actualList, value):
    instruction = str(instruction)

    match (instruction):

        case 'append':
            actualList.append(int(value))
            return actualList
        
        case 'remove':
            actualList.remove(int(value))
            return actualList

def simpleValue(instruction, actualList):
    instruction = str(instruction)

    match (instruction):
        
        case 'sort':
            actualList.sort()
            return actualList

        case 'reverse':
            actualList = actualList[::-1]
            return actualList
        
        case 'pop':
            actualList.pop()
            return actualList


if __name__ == '__main__':
    N = int(input())
    printResult = []
    printList = []
    
    for i in range(int(N)):
        read = str(input()).split()
        readen = [element for element in read]

        if (len(readen) == 1 and str(readen[0]) != 'print'):
            printList = simpleValue(readen[0], printList)
        elif (len(readen) == 2):
            printList = doubleValue(readen[0], printList, readen[1])
        elif (len(readen) == 3):
            printList = tripleValue(printList, readen[1], readen[2])
        elif (readen[0] == 'print'):
            printResult.append(str(printList))
    
    for element in printResult:
        print(element)


        
        


'''
Sample Input:

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''