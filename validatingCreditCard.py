# Carlos Paredes Márquez
# August 7th, 2024
# Problem: a credit card has the following characteristics: 
# 1: It must start with a 4,5 or 6
# 2: It must contain 16 digits
# 3: It must only consist of digits 0-9
# 4: It may have digits in groups of 4 separeted by "-"
# 5: It must not use other separator
# 6: It must not have 4 or more consecutive repeated digits

import re

def solveCalculation(element):      # Check the conditions: start number, only numbers, not 4 or more repeat numbers.
    firstElement = r"^[456]"        # condition to validate the start number
    justNumbers = r"^[0-9]+$"       # condition of only numbers
    notRepeat = r"(\d)\1{3,}"       # condition of not 4 or more repeat numbers

    if re.match(firstElement, element):             # first element check
        if re.match(justNumbers, element):          # only numbers validation
            if re.search(notRepeat, element):       # not 4 or more repeat numbers
                return "Invalid"
            else:
                return "Valid"
        else:
            return "Invalid"
    else:
        return "Invalid"

def solved(element):
    separated = r"^\d{4}-\d{4}-\d{4}-\d{4}$"        # condition of '-' and 16 numbers

    if (len(element) == 16):                        # indirect validation to the second condition
        return solveCalculation(str(element))       # go and validate all the element
        
    elif (len(element) > 16):                               # indirect validation of the 4th condition
        if re.match(separated, element):                    # validating the 4th condition
            n_element = element.replace("-", "")            # replacing '-' with void space
            return solveCalculation(n_element)              # go and validate all the new element
        else:
            return "Invalid"
    
    else:
        return "Invalid"

if __name__ == '__main__':
    n = int(input().strip())    # input of 'n' credit cards
    numbers = []                # list of 'credit cards' numbers
    results = []                # list of all the results
    
    for i in range(n):          # saving 'credit cards' in a list
        numbers.append(str(input()))
    
    for element in numbers:     # solving 'credit cards' results
        results.append(solved(element))
    
    for element in results:     # printing the saved results
        print(element)

'''
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Valid
Valid
Invalid
Valid
Invalid
Invalid

'''