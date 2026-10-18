Problem 17:
Hackerank:https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(map(int, input().split()))
n = int(input())

result = True

for i in range(n):
    other_set = set(map(int, input().split()))

    if not A.issuperset(other_set) or A == other_set:
        result = False
        break

print(result)
