def multiplication(a, n):
    if n == 0:
        return 1
    return multiplication(a, n-1) * a

print(multiplication(4, 4))