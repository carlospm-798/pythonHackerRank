#   Given the names and grades for each student in a class of N students,
#   store them in a nested list and print the name(s) of any student(s)
#   having the second lowest grade. If there are multiple students with 
#   the second lowest grade, order their names alphabetically and print
#   each name on a new line.

def lowestGrade(students):

    grades = []
    names = []
    for student in students:
        if student[1] not in grades:
            grades.append(student[1])
    
    grades.sort(reverse=True)
    secondLast = grades[-2]     # Second lowest grade

    for student in students:
        if student[1] == secondLast:
            names.append(student[0])
    
    names = sorted(names)
    for i in range(len(names)):
        print(names[i])

if __name__ == '__main__':

    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])

    lowestGrade(students)


'''

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry

'''