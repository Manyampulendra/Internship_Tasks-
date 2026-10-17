Problem 7:
Hackerank:https://www.hackerrank.com/challenges/symmetric-difference/copy-from/485331203

if __name__ == '__main__':
    M = int(input())
    set_m = set(map(int, input().split()))

    N = int(input())
    set_n = set(map(int, input().split()))

    result = set_m.symmetric_difference(set_n)

    for num in sorted(result):
        print(num)
