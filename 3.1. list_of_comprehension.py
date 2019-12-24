a = 10
b = 20
values = [x ** 3 for x in range(a, b + 1)]
print(values)

# 1

values = [x for x in range(a, b+1)]
print(values)
# print(x for x in range(a, b+1))


# 2
n = 10
values = [2 ** x for x in range(n)]
print(values)

values = [x for x in values if x % 2 == 0]
print(values)
# 3
print('Task 3')

# оставить в списке только строки полностью в верхнем регистре
value = 'Dkjkj'
upper_case = value.upper()
print(value, upper_case)


values = ['HELLO', 'world', 'F']
values = [x for x in values if x == x.upper()]
# values = [x for x in values if x.isupper()]
print(values)

#  сгенерировать список вида [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ...]
print('Task 4')

values = [x for x in range(10) for i in range(x)]

print(values)