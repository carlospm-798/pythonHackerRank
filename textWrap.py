#   Given a string S and width W, your task is to wrap the string into 
#   a paragraph of width W.
import textwrap

def wrap(string, max_width):

    result = ''
    result = '\n'.join(textwrap.wrap("".join(string), width=max_width))
    return result


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