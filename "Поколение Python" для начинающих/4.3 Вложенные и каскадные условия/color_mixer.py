'''
Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. При смешивании двух основных цветов получается вторичный цвет:

если смешать красный и синий, то получится фиолетовый;
если смешать красный и желтый, то получится оранжевый;
если смешать синий и желтый, то получится зеленый.
Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, который получится в результате.

Формат входных данных
На вход программе подаются две строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.

Примечание 1. Если смешать красный и красный, то получится красный и т.д.

Примечание 2. Поиграйтесь с настоящим цветовым микшером 🙂

Тестовые данные 🟢
Sample Input 1:

красный
синий
Sample Output 1:

фиолетовый
Sample Input 2:

красный
блаблабла
Sample Output 2:

ошибка цвета
'''


c1, c2 = input(), input()
if  c1 == c2 and (c1== "красный" or c1 == "синий" or c1 == "желтый"):
    print(c1)
elif c1 == "красный" and c2 == "синий" or c2 == "красный" and c1 == "синий":
    print("фиолетовый")
elif c1 == "красный" and c2 == "желтый" or c2 == "красный" and c1 == "желтый":
    print("оранжевый")
elif c1 == "синий" and c2 == "желтый" or c2 == "синий" and c1 == "желтый":
    print("зеленый")
else:
    print("ошибка цвета")
    
    
