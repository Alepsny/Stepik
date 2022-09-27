'''
Футбольная команда набирает девочек от 10 до 15 лет включительно. Напишите программу, которая запрашивает возраст и пол претендента, используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) и определяет подходит ли претендент для вступления в команду или нет. Если претендент подходит, то выведите «YES», иначе выведите «NO».

Формат входных данных
На вход программе подаётся натуральное число – возраст претендента и буква обозначающая пол m (мужчина) или f (женщина).

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

10
f
Sample Output 1:

YES
Sample Input 2:

11
m
Sample Output 2:

NO
'''


a, g = int(input()), input()
if 10 <= a <= 15 and g == "f":
    print("YES")
else:
    print("NO")
