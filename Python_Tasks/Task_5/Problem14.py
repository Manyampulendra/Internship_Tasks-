Problem 14:
Hackerank:https://www.hackerrank.com/challenges/finding-the-percentage/copy-from/437824178

if __name__ == '__main__':
    n = int(input())

student_marks = {}

for _ in range(n):
    line = input().split()
    name = line[0]
    scores = list(map(float, line[1:]))
    student_marks[name] = scores

query_name = input()
avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{avg_score:.2f}")
