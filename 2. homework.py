# Task 1

string = 'aaabbbccjjjj'
print(len(string))
count = 0
for i in range(len(string)):
    if string[i] == 'a':
        count += 1
print((count / len(string)) * 100, '%')

# Task 2

string2 = 'abnvcme'
print(string2)
a = string2[0]  # выделяем первый символ из строки
b = string2[-1]  # выделяем последний символ из строки
c = string2[1:-1]  # выделяем строку без первого и последнего символа
print(b + c + a)  # печатаем новую строку с поменянными первым и последним символами

# Task 3

str3 = 'aabbbccc'

# for i in range(len(str3)):
#     if str3[i] != 'a' or str3[i] != 'b' or str3[i] != 'c':
#         print('No')

# task 4

str4 = 'avcva'

# task 5


# Подсчитать сумму элементов списка чисел

data = [1, 2, 4, 5, 69]

summa = 0

# for i in data:
#     summa = data[i] + summa
# print(summa)

# Подсчитать количество положительных элементов в списке чисел

data = [1, -2, 20, -20, 90]

x = 0
for i in range(len(data)):
    if data[i] >= 0:
        x += 1
print(x)

# напечатать все четные элементы из списка
print('             Task 3')

data = [2, 22, 11, 12, 0, 2323, 234324, 234, 5432, 43]

for i in range(len(data)):
    if data[i] % 2 == 0:
        print(data[i])

# Напечатать все элементы списка чисел, находящиеся на четных позициях (0, 2, 4, ...)
print('Напечатать все элементы списка чисел, находящиеся на четных позициях (0, 2, 4, ...')
data = [1, 2, 3, 4, 5, 6, 7, 123]

for i in range(len(data)):
    if i % 2 == 0:
        print(data[i])

# Найти среднее арифметическое значение списка чисел.
print('Найти среднее арифметическое значение списка чисел.')

data = [12, 123, 323, 45, 20, 233, 435, 454, 67, 57, 4545, 23]

print(sum(data) / len(data))

#  Напечатать все строки из списка, длина которых больше 5.
print('Напечатать все строки из списка, длина которых больше 5.')

data = ['hello', 'very long', 'world', 'esheeshe', 'allo garazh!', 'net']

for i in range(len(data)):
    if len(data[i]) > 5:
        print(data[i])

# Убрать из строки все повторяющиеся символы (любые печатные), заменив их на один символ.
# 'Hello my friend...' -> 'Helo my friend.'
print('Убрать из строки все повторяющиеся символы (любые печатные), заменив их на один символ.')

str5 = 'Hello my dear Kelly!'
print(str5)

a = []  # создаю список

for i in range(len(str5)):
    a.append(str5[i])
print(a)

a2 = ''  # new string

for i in range(len(a)):
    if a[i] != a[-i - 1]:
        a2 = a2 + a[i]
print(a2)

# Заменить все буквы в нижнем регистре на заглавные и наоборот. * (таблица символов и функция ord() очень помогут)
print(
    'Заменить все буквы в нижнем регистре на заглавные и наоборот. * (таблица символов и функция ord() очень помогут)')

str6 = 'Hello, world!'
print(str6)

a3 = []
for i in range(len(str6)):
    a3.append(ord(str6[i]))
print('Лист кодов:',a3)

# заменяем заглавные на мелкие
a4 = []
for i in range(len(a3)):
    if a3[i] >= 65 and a3[i] <= 90:
        a4.insert(i, chr(int(a3[i]) + 32))

print(a4)

# заменяем мелкие на заглавные
# for i in range(len(a3)):
#     if a3[i] >= 97 and a3[i] <= 122:
#         a3.pop(i)
#         a3.insert(i, chr(a3[i] + 32))
#
# print(a3)
#
# a4 = ''
# for i in range(len(a3)):
#     a4 = a4 + (chr(a3[i]))
# print(a4)

# Проверить, что список числе соответствует правилу a1 < a2 > a3 < a4 > a5 ... Другими словами, каждый элемент либо строго больше соседей, либо строго меньше.p
# print('Проверить, что список числе соответствует правилу a1 < a2 > a3 < a4 > a5 ... Другими словами, каждый элемент либо строго больше соседей, либо строго меньше.')
#
# data = [1, 2, -1, 4, 3, 6]

# for i in range(len(data)):
#     if (data[i] > data [i+1] and data [i] < data [i-1]) or (data[i] < data [i+1] and data[i] > data[i-1]:
#         print('Ok')
#     else:
#         print('Not ok')

# Проверить, что список чисел упорядочен по невозрастанию.
        # [3, 2, 1] -> yes [1, 2, 1] -> no

# data = [3, 2, 1]

# for i in range(len(data)):
#     if data[i] > data[i-1]
#         print('Ok')
