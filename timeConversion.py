#   Carlos Paredes Márquez
#   Time Conversion
#   Task: Given a time in -hour AM/PM format, 
#   convert it to military (24-hour) time.
#   - 12:00:00AM on a 12-hour clock is 00:00:00 
#   on a 24-hour clock.
#   - 12:00:00PM on a 12-hour clock is 12:00:00 
#   on a 24-hour clock.

def timeConversion(s):
    timeZone = s[-2:]

    if (timeZone == 'PM' and int(s[:2]) < 12):
        hour = int(s[:2]) + 12
        result = str(hour) + str(s[2:-2])
    elif (timeZone == 'PM' and int(s[:2]) >= 12):
        result = s[:-2]
    elif (timeZone == 'AM' and int(s[:2]) == 12):
        result = '00' + str(s[2:-2])
    else:
        result = s[:-2]

    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)
    print(result)
    #fptr.write(result + '\n')
    #fptr.close()

'''
Input (stdin)
12:45:54PM

Expected Output
12:45:54

'''