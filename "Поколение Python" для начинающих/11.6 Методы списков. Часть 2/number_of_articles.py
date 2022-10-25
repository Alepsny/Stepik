'''
На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

Формат входных данных
На вход программе подается строка, содержащая английский текст. Слова текста разделены символом пробела.

Формат выходных данных
Программа должна вывести общее количество артиклей 'a', 'an', 'the' вместе с поясняющим текстом.

Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.

Тестовые данные 🟢
Sample Input:

William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.
Sample Output:

Общее количество артиклей: 7
'''


text = input().lower().split()
article = text.count("a") + text.count("an") + text.count("the")
print("Общее количество артиклей:", article)
