Problem 8:
Hackerank:https://www.hackerrank.com/challenges/py-set-add/copy-from/485332339

n = int(input())
countries = set()

for i in range(n):
    country = input()
    countries.add(country)

print(len(countries))
