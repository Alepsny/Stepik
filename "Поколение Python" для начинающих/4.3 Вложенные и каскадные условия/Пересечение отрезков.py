'''
На числовой прямой даны два отрезка: [a_1; \,  b_1][a 
1
​
 ;  b 
1
​
 ] и [a_2; \, b_2][a 
2
​
 ; b 
2
​
 ]. Напишите программу, которая находит их пересечение.

Пересечением двух отрезков может быть:

отрезок;
точка;
пустое множество.
Формат входных данных
На вход программе подаются 4 целых числа a_1, \, b_1, \, a_2, \, b_2a 
1
​
 ,b 
1
​
 ,a 
2
​
 ,b 
2
​
 , каждое на отдельной строке. Гарантируется, что a_1 < b_1a 
1
​
 <b 
1
​
 ​ и a_2 < b_2a 
2
​
 <b 
2
​
 ​.

Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».

Тестовые данные 🟢
Sample Input 1:

1
3
2
4
Sample Output 1:

2 3
Sample Input 2:

1
2
3
4
Sample Output 2:

пустое множество
Sample Input 3:

5
6
6
8
Sample Output 3:

6
'''


a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 < a2 and b1 < b2 and b1 < a2 or a2 < a1 and b2 < b1 and b2 < a1:
    print("пустое множество")
elif a1 == b2:
    print(a1)
elif a2 == b1:
    print(a2)
elif a1 <= a2 and b2 <= b1:
    print(a2, b2)
elif a2 <= a1 and b1 <= b2:
    print(a1, b1)
elif a2 <= b1 <= b2:
    print(a2, b1)
elif a1 <= b2 <= b1:
    print(a1, b2)
