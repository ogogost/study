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
