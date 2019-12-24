n = 5
m = 5
data = [[0 for y in range(m)] for x in range(n)]
print(data)

for a in data:
    for b in a:
        print(b, end=' ')
    print()
print()

print('--------------------')
print('Task 1')

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
result = [x * y for x in first for y in second]
print(result)

# a = 12
# b = 23
# maximum = b if b > a else a  # тернарный оператор сравнения


print('---------------------')
print('Task 2')
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


for i in range(1, 4):
    for j in range(1, 4):
                if mines[i][j] == 0:
                    count = abs((mines[j-1][i-1] + mines[j-1][i] + mines[j-1][i+1]) + (mines[j][i-1] + mines[j][i+1]) + (mines[j+1][i-1] + mines[j+1][i] + mines[j+1][i+1]))
                    zeros[i][j] = count
                else:
                    zeros[i][j] = -1

for a in zeros:
    for b in a:
        print(b, end=' ')
    print()
print()




if mines[1][1] == 0:
    count = mines[0][0] + mines[0][1] + mines[0][2] + mines[1][0] + mines[1][2] + mines[2][0] + mines[2][1] + mines[2][2]
    count11 = abs(count)
else:
    count11 = -1
print(count11)

if mines[1][2] == 0:
    count = mines[0][1] + mines[0][2] + mines[0][3] + mines[1][1] + mines[1][3] + mines[2][1] + mines[2][2] + mines[2][3]
    count12 = abs(count)
else:
    count12 = -1
print(count12)

if mines[1][3] == 0:
    count = mines[0][2] + mines[0][3] + mines[0][4] + mines[1][2] + mines[1][4] + mines[2][2] + mines[2][3] + mines[2][4]
    count13 = abs(count)
else:
    count13 = -1
print(count13)

print('--------------------')
print('Task 3')
# напечатать табличку змейкой
# дано N
# 1 2 3
# 6 5 4
# 7 8 9

N = 3

# создаем матрицу N x N, состоящую из нулей,
# т.к. записать через индекс я должен в уже существующую матрицу

snake = [[0 for y in range(N)] for x in range(N)]

# создаю переменную для записи значений возрастающей прогрессии, т.к. просто сумма номер строки и колонки не даёт искомого результата
count = 1

# C	   row	column	result
# 1		0	0		1
# 1		0	1		2
# 1		0	2		3
# 3		1	0			4
# 3		1	1			5
# 3		1	2			6
# 5		2	0				7
# 5		2	1				8
# 5		2	2				9

for row in range(N):
    for column in range(N):
        if row % 2 == 0: # условие при котором четные строки рассчитываются обычным образом
            snake[row][column] = count + row + column
        else: # а нечетные строки располагаются в обратном порядке (реверс)
            snake[row][column] = count + row + column
            snake[row].reverse()
    count = count + (N - 1)

for a in snake:
    for b in a:
        print(b, end=' ')
    print()
print()

print('--------------------')
print('Task 4')
# напечать табличку "спиралью"
# 1 2 3
# 8 9 4
# 7 6 5

N = 3
spiral = [[0 for y in range(N)] for x in range(N)]


count = 1

for row in range(N):
    for col in range(N):
        if spiral[0][col] == 0:
            spiral[row][col] = count
            count += 1


for a in spiral:
    for b in a:
        print(b, end=' ')
    print()
print()

#  необходимо научиться переворачивать матрицу на 90 градусов

spiral2 = [[0 for y in range(N)] for x in range(N)]

for row in range(N):
    for col in range(N):
        spiral2[row][col] = spiral[col][N -1 - row]

for a in spiral2:
    for b in a:
        print(b, end=' ')
    print()
print()

