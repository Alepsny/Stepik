'''
Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. ИМТ показывает весит человек больше или меньше нормы для своего роста. 
ИМТ человека рассчитывают по формуле:

ИМТ = масса (кг)/(рост(м)×рост(м)),

где масса измеряется в килограммах, а рост — в метрах.

Масса человека считается оптимальной, если его ИМТ находится между 18.518.5 и 2525. Если ИМТ меньше 18.518.5, то считается, что человек весит ниже нормы.
Если значение ИМТ больше 2525, то считается, что человек весит больше нормы.

Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.518.5 и 2525 (включительно). "Недостаточная масса", если ИМТ меньше 18.518.5 и 
"Избыточная масса", если значение ИМТ больше 2525.

Формат входных данных
На вход программе подается два числа: масса и рост человека, каждое на отдельной строке. Все входные числа являются вещественными, используйте для них тип данных float.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

65
1.75
Sample Output 1:

Оптимальная масса
Sample Input 2:

80
2.23
Sample Output 2:

Недостаточная масса
Sample Input 3:

80
1.6
Sample Output 3:

Избыточная масса
'''


w, g = float(input()), float(input())
imt = w / g ** 2
if imt < 18.5:
    print('Недостаточная масса')
elif imt <= 25:
    print('Оптимальная масса')
else:
    print('Избыточная масса')

