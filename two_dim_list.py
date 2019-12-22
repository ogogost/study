n = 5
m = 5
data = [[0 for y in range(m)] for x in range(n)]
print(data)

for a in data:
    for b in a:
        print(b, end=' ')
    print()
print()

# дано число N, сгенерировать таблицу умножения NxN и сохранить в список
n = 9
data = [[0 for y in range(n)] for x in range(n)]

for row in range(len(data)):
    for column in range(len(data[row])):
        data[row][column] = (row + 1) * (column + 1)
        print(data[row][column], end='   ')
    print()

print('---------------------')

first = [1, 2, 3]
second = [4, 5, 6]
result = [x + y for x in first for y in second]
print(result)

# a = 12
# b = 23
# maximum = b if b > a else a  # тернарный оператор сравнения


print('---------------------')

# сгененировать поле для игры "Сапёр"
# [[0, -1, 0],
#  [0, 0, 0],
#  [-1, 0, 0]]

print(' Дана матрица расположения мин:')
mines = [[0, -1, 0],
         [0, 0, 0],
         [-1, 0, 0]]

for a in mines: # удобное отображение матрицы
    for b in a:
        print(b, end=' ')
    print()
print()

print('Для решения  задачи добавляем пустые строки и столбцы по краям')
mines.append([0, 0, 0])  # добавление пустых строк в матрицу
mines.reverse()
mines.append([0, 0, 0])
mines.reverse()

for i in range(5): # добавление пустых столбцов
    mines[i].append(0)
    mines[i].reverse()
    mines[i].append(0)
    mines[i].reverse()

for a in mines: # удобное отображение расширенной матрицы
    for b in a:
        print(b, end=' ')
    print()
print()

print('Создаем пустую матрицу с будущей информацией о минах')

zeros = [[0 for y in range(5)] for x in range(5)]

for a in zeros:
    for b in a:
        print(b, end=' ')
    print()
print()
# Вычисляем количество мин в смежных ячейках


for i in range(1,4):
    for j in range(1,4):
                if mines[i][j] == 0:
                    zeros[i][j] = abs((mines[j-1][i-1] + mines[j-1][i] + mines[j-1][i+1]) + (mines[j][i-1] + mines[j][i+1]) + (mines[j+1][i-1] + mines[j+1][i] + mines[j+1][i+1]))
                else:
                    zeros[i][j] = -1

for a in zeros:
    for b in a:
        print(b, end=' ')
    print()
print()



#
# if mines[1][1] == 0:
#     count11 = mines[0][0] + mines[0][1] + mines[0][2] + mines[1][0] + mines[1][2] + mines[2][0] + mines[2][1] + mines[2][2]
#     count11 = abs(count11)
# else:
#     count11 = -1
# print(count11)
#
# if mines[1][2] == 0:
#     count12 = mines[0][1] + mines[0][2] + mines[0][3] + mines[1][1] + mines[1][3] + mines[2][1] + mines[2][2] + mines[2][3]
#     count12 = abs(count12)
# else:
#     count12 = -1
# print(count12)
#
# if mines[1][3] == 0:
#     count13 = mines[0][2] + mines[0][3] + mines[0][4] + mines[1][2] + mines[1][4] + mines[2][2] + mines[2][3] + mines[2][4]
#     count13 = abs(count13)
# else:
#     count13 = -1
# print(count13)
#


# напечатать табличку змейкой
# дано N
# 1 2 3
# 6 5 4
# 7 8 9

# напечать табиличку "спиралью"
# 1 2 3
# 8 9 4
# 7 6 5
