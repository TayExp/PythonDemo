import itertools

def isAdditiveNumber(self, num):
    n = len(num)
    for i, j in itertools.combination(range(1,n),2):
        a = num[:i]
        b = num[i:j]
        if(b != str(int(b))):
            continue
        while(j < n):
            c = str(int(a) + int(b))
            if not num.startswith(c,j):
                break
            j += len(c)
            a, b = b, c
        if j == n:
            return True
    return False


def main():
    pass


if "__name__" == "__main__":
    main()