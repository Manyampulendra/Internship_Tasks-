Problem 15:
Hackerank:
from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)

    if odd_count <= 1:
        return "YES"
    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
