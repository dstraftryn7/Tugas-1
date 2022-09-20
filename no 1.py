def sum_squares(x):
    sum = 0
    for i in x:
        sum = i ** 2 + sum
    print('hasilnya = ', sum)

sum_squares([4, 5, 6])

