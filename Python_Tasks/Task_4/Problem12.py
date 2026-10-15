Problem 12:
# HackerRank:- https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique_numbers = set(array)
    result = sum(unique_numbers) / len(unique_numbers)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
