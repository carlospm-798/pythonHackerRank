def gradingStudents(grades):

    solutions = []

    for grade in grades:
    
        roundGrade = round(grade/5) * 5
        roundResult = roundGrade - grade

        if (roundResult > 0 and roundResult < 3) and (roundGrade >= 40):
            solutions.append(int(roundGrade))
        else:
            solutions.append(int(grade))
    
    return solutions

if __name__ == '__main__':

    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))

'''

Sample Input 0

4
73
67
38
33

Sample Output 0

75
67
40
33

'''