'''
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

thing
night
Sample Output 1:

YES
Sample Input 2:

cat
rat
Sample Output 2:

NO
Sample Input 3:

tea
eat
Sample Output 3:

YES
'''


word1, word2 = [i for i in input()], [i for i in input()]
for i in range(len(word1) - 1, -1, - 1):
    if word1[i] in word2:
        del word2[word2.index(word1[i])]
        del word1[i]
if word1 == word2 == []:
    print('YES')
else:
    print('NO')
