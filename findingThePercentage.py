#   Print the average of the marks array for the student name provided
#   showing 2 places after the decimal point

def solution(student_marks, query_name):

    if query_name in student_marks:
        list_values = student_marks[query_name]

        result = 0
        for value in list_values:
            result += value
        
        average = 0
        average = result/len(list_values)

        print(f"{average:.2f}")

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    solution(student_marks, query_name)

'''

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output 1

26.50

'''