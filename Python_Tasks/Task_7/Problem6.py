Problem 6:
Hackerank:
def pangrams(s):
    letters = set(s.lower())

    if len(letters.intersection(set("abcdefghijklmnopqrstuvwxyz"))) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
