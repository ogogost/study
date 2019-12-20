a = 10
b = 20
values = [x ** 2 for x in range(a, b + 1)]
print(values)

# 1

values = [x for x in range(a, b+1)]
print(values)
print(x for x in range(a, b+1))


# 2
n = 10
values = [2 ** x for x in range(n)]
print(values)

# 3
print('Task 3')

values = ['HELLO', 'world']
# values = [  for x in values]


# values = [x for x in value if ord(x) > 97 ]
# print(values)

# 4
print('Task 4')
values = [x + x for x in range(a, n)]

print(values)