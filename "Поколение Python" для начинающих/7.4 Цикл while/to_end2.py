'''
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). Напишите программу, которая выводит члены данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести члены данной последовательности.

Тестовые данные 🟢
Sample Input 1:

JavaScript
C++
C#
Ruby
PHP
КОНЕЦ
Python
Sample Output 1:

JavaScript
C++
C#
Ruby
PHP
Sample Input 2:

Великобритания
США
Китай
КОНЕЦ
Ватикан
Sample Output 2:

Великобритания
США
Китай
Sample Input 3:

for
while
конец
for while
Sample Output 3:

for
while
'''


text = input()
while text != "КОНЕЦ" and text != "конец":
    print(text)
    text = input()
