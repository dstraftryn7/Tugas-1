def triangular(x):
    if x == 1:
        return (1)
    else:
        return (x + triangular(x-1))

tri = triangular(5)
print("Hasil = ", tri)

