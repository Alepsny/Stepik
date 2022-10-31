'''
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
должен выводить:

this_is_camel_cased
is_prime_number
Тестовые данные 🟢
Sample Input:

ThisIsCamelCased
Sample Output:

this_is_camel_cased
'''


# объявление функции
def convert_to_python_case(text):
    txt = ""
    for i in range(len(text)):
        if text[i] == text[i].upper() and i == 0 or text[i].isalpha() == False:
            txt += text[i].lower()
        elif text[i] == text[i].upper():
            txt += "_" + text[i].lower()
        else:
            txt += text[i]
    return txt

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
