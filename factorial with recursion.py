def recursiveFactorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * recursiveFactorial(n-1)

