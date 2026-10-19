Problem 17:
Hackerank:
def separateNumbers(s):
    n = len(s)

    for i in range(1, n // 2 + 1):
        first = s[:i]

        if first[0] == '0':
            continue

        num = int(first)
        expected = first

        while len(expected) < n:
            num += 1
            expected += str(num)

        if expected == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
