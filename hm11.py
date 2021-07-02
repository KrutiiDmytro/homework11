# Задача 1
# Дано список словорей
# Создать список кортежей [('red', 'high'), ('yellow', 'low')]
t = [{'color': 'red', 'value': 'high'},
     {'color': 'yellow', 'value': 'low'}]
t = [4]
print(t)
# Задача 2
# Дано словарь
# преобразовать его в список кортежей
a_dictionary = {"a": 1, "b": 2, "c": 3, }
ls = list(dict.items(a_dictionary))
print(ls)

# Задача 3
# Дано два списка
# Создать из них список кортежей
list_a = [1, 2, 3, 4, ]
list_b = [5, 6, 7, 8, ]
list_c = list(zip(list_a, list_b)) 
print(list_c)

# Задача 4
# Создать кортеж занчений для первих трьох єлементов словоря
h = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4', }
list(reversed(h.items()))
h.pop(4)
print(h)
# Задача 5
# Дано список
# Создать кортеж
d = ['bar', 'baz', 'qux', 'etc', ]
d.insert(0, 'foo',)
print(d)
