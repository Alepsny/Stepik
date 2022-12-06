'''
Руководитель онлайн-школы BEEGEEK и его помощник составили списки учеников их школы.

Напишите программу, которая выведет все фамилии учеников, которые вспомнили руководитель и его помощник.

Формат входных данных
На вход программе в первой строке подаются фамилии, записанные руководителем школы, а на второй строке - помощником руководителя. Фамилии указываются через пробел.

Формат выходных данных
Программа должна вывести все фамилии учеников, отсортированных в лексикографическом порядке, записанные руководителем и его помощником.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

Тестовые данные 🟢
Sample Input 1:

Блинов Жданов
Бобров Жданов Некрасов Блинов
Sample Output 1:

Блинов Бобров Жданов Некрасов
Sample Input 2:

Рыбаков
Сафонов Игнатов
Sample Output 2:

Игнатов Рыбаков Сафонов
Sample Input 3:

Демин Рыбаков Сафонов Игнатов Мухин
Сафонов Игнатов Демин Рыбаков
Sample Output 3:

Демин Игнатов Мухин Рыбаков Сафонов
'''


d, h = set(input().split()), set(input().split())
print(*sorted(d.union(h)))
