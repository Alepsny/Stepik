'''
Дополните приведенный код, чтобы он вывел сумму квадратов элементов множества numbers.
'''


numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
sum_q = 0
for i in numbers:
    sum_q += i ** 2
print(sum_q)
