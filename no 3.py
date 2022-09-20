def pangkat(x, y):
    if y > 1:
        return x * pangkat(x, y-1)

    return x
print(pangkat(3, 2))
print(pangkat(5, 3))

