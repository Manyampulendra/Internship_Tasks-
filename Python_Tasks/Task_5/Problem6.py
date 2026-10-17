Problem 6:
Hackerank:https://www.hackerrank.com/challenges/py-introduction-to-sets/copy-from/485330839

def average(array):
    unique_numbers = set(array)
    result = sum(unique_numbers) / len(unique_numbers)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
