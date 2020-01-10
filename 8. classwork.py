"""
Определить, какой тип будет иметь результат операции (переменная c)
"""
a = 3
b = 4
c = a / b

print(type(c))

"""
Посчитать сумму чисел от 1 до 100
"""

count = 0
for i in range(0, 101):
    count = count + i
print(count)


"""
Проверить, что число является четным
"""
number = 4
if number % 2 == 0:
    print('ok')
else:
    print('ne ok')

"""
Будет ли работать данный код?
name = "Svetozar"
age = 24
name_and_age = name + age
"""

"""
Проверить, если ли заданное число в списке
"""
number = 3
data = [1, 4, 2]

print(data.count(3))

"""
Написать функцию, которая проверяет, делится ли одно число на другое без остатка
"""

def delenie(a, b):
    if a % b == 0:
        print('ok')
        return True
    else:
        print('not ok')
        return False


