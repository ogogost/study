n = 4
m = 5
data = [[0 for y in range(m)] for x in range(n)]
print(data)

print(len(data))

for a in data:
    for b in a:
        print(b, end=' ')
    print()
print()

# for a in range(len(data)):
#     print(a, end = '__')


# дано число N, сгенерировать таблицу умножения NxN и сохранить в список
n = 9
data = [[0 for y in range(n)] for x in range(n)]

print(len(data))
print(data)

for row in range(len(data)):
    for column in range(len(data[row])):
        data[row][column] = (row + 1) * (column + 1)
        print(data[row][column], end='   ')
    print()

print(data)

print('---------------------')

first = [1, 2, 3]
second = [4, 5, 6]
result = [x + y for x in first for y in second]
print(result)

# a = 12
# b = 23
# maximum = b if b > a else a  # тернарный оператор сравнения


# сгененировать поле для игры "Сапёр"
# [[0, -1, 0],
#  [0, 0, 0],
#  [-1, 0, 0]]

# напечатать табличку змейкой
# дано N
# 1 2 3
# 6 5 4
# 7 8 9

# напечать табиличку "спиралью"
# 1 2 3
# 8 9 4
# 7 6 5