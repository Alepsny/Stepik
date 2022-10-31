'''
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра 
Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными.

Формат входных данных 
На вход программе подается строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.

Тестовые данные 🟢
Sample Input 1:

Day, mice. "Year" is a mistake!
Sample Output 1:

Gdb, qmgi. "Ciev" ku b tpzahrl!
Sample Input 2:

my name is Python!
Sample Output 2:

oa reqi ku Veznut!
'''


def cesar(s, n):
    new = ''
    for i in s:
        if 97 <= ord(i) <= 122:
            if ord(i) + n > 122:
                new += chr(97 + (ord(i) + n) % 122 - 1)
            else:
                new += chr(ord(i) + n)
        elif 65 <= ord(i) <= 90:
            if ord(i) + n > 90:
                new += chr(65 + (ord(i) + n) % 90 - 1)
            else:
                new += chr(ord(i) + n)
        else:
            new += i
    return new

s = input()
new, temp = '', ''
for i in s:
    if i.isalpha():
        temp += i
    elif temp != '':
        new += cesar(temp, len(temp))
        new += i
        temp = ''
    else:
        new += i
print(new + cesar(temp, len(temp)))
