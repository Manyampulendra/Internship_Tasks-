Problem 2:
Hackerank:

K = int(input())
rooms = list(map(int, input().split()))

unique_rooms = set(rooms)

print((sum(unique_rooms) * K - sum(rooms)) // (K - 1))
