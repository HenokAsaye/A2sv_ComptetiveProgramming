# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    students = []  
    for _ in range(int(input().strip())):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])  
    u_scores = sorted(set(score for _, score in students))
    second_lowest = u_scores[1]
    second_lowest_students = sorted([name for name, score in students if score == second_lowest])
    for student in second_lowest_students:
        print(student)