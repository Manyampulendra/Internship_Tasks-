Problem 16:
Hackerank:https://www.hackerrank.com/challenges/collections-counter/copy-from/485334708

from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))

shoe_count = Counter(shoe_sizes)

n = int(input())
total_earnings = 0

for _ in range(n):
    size, price = map(int, input().split())

    if shoe_count[size] > 0:
        total_earnings += price
        shoe_count[size] -= 1

print(total_earnings)
