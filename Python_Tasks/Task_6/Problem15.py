Problem 15:
Hackerank:https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

result = english.difference(french)

print(len(result))
