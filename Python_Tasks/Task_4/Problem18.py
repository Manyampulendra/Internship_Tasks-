Problem 18:
Hackerank:https://www.hackerrank.com/challenges/python-lists/copy-from/456314845
lst = []
n = int(input())
# Process each command
for _ in range(n):
    command = input().split()

    if command[0] == "insert":
        i = int(command[1])
        e = int(command[2])
        lst.insert(i, e)

    elif command[0] == "print":
        print(lst)

    elif command[0] == "remove":
        e = int(command[1])
        lst.remove(e)

    elif command[0] == "append":
        e = int(command[1])
        lst.append(e)

    elif command[0] == "sort":
        lst.sort()

    elif command[0] == "pop":
        lst.pop()

    elif command[0] == "reverse":
        lst.reverse()
