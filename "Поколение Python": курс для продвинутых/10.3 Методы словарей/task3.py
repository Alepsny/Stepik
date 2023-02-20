'''
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.
'''


text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
set_t = set(text)
result = {}
for i in set_t:
    result.setdefault(i, text.count(i))
    
    
