'''
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль 
является действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False
'''


# объявление функции
def is_simple(digit):
    for i in range(2, digit):
        if digit % i == 0:
            return False
    return True

def is_valid_password(password):
    return len(password) == 3 and password[0] == password[0][::-1] and \
is_simple(int(password[1])) == True and int(password[2]) % 2 == 0

            
# считываем данные
psw = input().split(":")

# вызываем функцию
print(is_valid_password(psw))
