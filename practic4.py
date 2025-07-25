def main():
    n = int(input().strip())
    if n == 1:
        print(1)
    else:
        k = n // 3
        r = n % 3
        if r == 0:
            print(3 ** k)
        elif r == 1:
            print((3 ** (k - 1)) * 4)
        else:  