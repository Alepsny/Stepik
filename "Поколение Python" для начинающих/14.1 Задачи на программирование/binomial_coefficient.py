'''
Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает значение биномиального коэффициента, 
равного n!/(k!(n−k)!).

Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 1 до n, то есть 
n!=1⋅2⋅3⋅…⋅n

Примечание 2. Реализуйте вспомогательную функцию factorial(n), вычисляющую факториал числа или воспользуйтесь уже готовой функцией из модуля math.
'''


# объявление функции
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def compute_binom(n, k):
    return int(factorial(n) / factorial(k) / factorial(n - k))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
