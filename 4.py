value = 'abcba'
symbol = 'a'
count = 0

for char in value:
    if char == symbol:
        print('Found!')
        count += 1 # count = count + 1

print(count)

print(count / len(value))

# дана строка, поменять в ней первый и последний символ

a = value [0]
b = value [-1]
c = value [1:-1]

print(a+c+b)

print(value[-1] + value[1:-1] + value[0])

# проверить, что строка состоит только из символов 'a", 'b', 'c'
# 'abc' -> yes
# 'abwerd' -> no

result = True
for char in value:
    if char not in 'abc': # if char != 'a' or char != 'b' or char != 'c'
        result = False
        break

# проверить симметрию относительно середины строки (палиндром)
value = 'abcba'
result = True

for i in range(len(value)//2):
    if value[i] != value[-i - 1]:
        result = False
        break
print(result)

print(value == value[::-1])

# сжать строку по правилу, все последовательности повторяющихся символов длины больше 1 заменить на символ + кол-во повторений

value = 'aaaabbbbdddd'

coint = 0
for i in range(len(value)):
    if value[i] = value[i +1]
        count = count + 1
        print(value[i], count)

# сжать строку по правилу, все последовательности повторяющихся символов длины больше 1 заменить на символ + кол-во повторений

value = 'aaaaccccccbbbbbbb' + '@'

count = 0

result = ''

for i in range(len(value) - 1):
    if value[i] != value[i + 1]:
        current_value = (value[count: i + 1])
        result += value[i] + str(len(current_value))
        count = i + 1
print(result)