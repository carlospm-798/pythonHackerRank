#   Given a string S and width W, your task is to wrap the string into 
#   a paragraph of width W.
import textwrap

def wrap(string, max_width):

    result = ''
    result = '\n'.join(textwrap.wrap("".join(string), width=max_width))
    return result

'''
def wrap(string, max_width):
    
    result = []
    elements = []
    for i in range(len(string)):
        elements.append(string[i])
    
    n = 0
    while (n < len(elements)):
        nextString = ''
        for i in range(max_width):
            if (n + max_width < len(elements)):
                nextString = nextString + elements[n + i]
        if(nextString != ''):
            result.append(nextString)
        n += max_width

    nextString = ''
    nextString = ''.join(elements[(n-max_width):])
    result.append(nextString)

    return result
'''


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

'''

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''