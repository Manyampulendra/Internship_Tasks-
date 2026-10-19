Problem 14:
Hackerank:
def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    first = s[:n // 2]
    second = s[n // 2:]

    count = [0] * 26

    for ch in first:
        count[ord(ch) - ord('a')] += 1

    for ch in second:
        count[ord(ch) - ord('a')] -= 1

    return sum(max(0, x) for x in count)
