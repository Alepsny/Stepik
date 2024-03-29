'''
Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв, слова разделены одним пробелом или несколькими.

Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с учетом регистра. Для первого вхождения слова 
программа выведет 1, для второго вхождения того же слова — 2 и т. д.

Формат входных данных
Программа получает на вход единственную строку текста, состоящую только из русских букв и символов пробела. 

Формат выходных данных
Для каждого слова исходного текста программа выводит одно целое число — номер вхождения этого слова в текст. Числа необходимо вывести на одной строке через пробел.

Примечание. Количество чисел должно совпадать с количеством слов исходного текста.

Тестовые данные 🟢
Sample Input 1:

прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон
Sample Output 1:

1 1 2 1 1 2 1 2 3 1
Sample Input 2:

Привет что делаешь что нового что с работой как там с деньгами
Sample Output 2:

1 1 1 2 1 3 1 1 1 1 2 1
'''


s = input().split()
dic = {}
for i in s:
    dic.setdefault(i, [str(j + 1) for j in range(s.count(i))])
for i in s:
    print(dic[i][0], end = ' ')
    del dic[i][0]
