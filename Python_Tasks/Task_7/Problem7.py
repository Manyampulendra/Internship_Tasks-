Problem 7:
Hackerank:
def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase[:size]
    width = 4 * size - 3
    lines = []

    for i in range(size - 1, -1, -1):
        row = list(alphabet[i:size])
        row = row[::-1] + row[1:]
        lines.append("-".join(row).center(width, "-"))

    print("\n".join(lines + lines[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
