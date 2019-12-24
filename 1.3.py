a = 11
b = a % 2

if int(b) == 1:
    print('Нечет')
else:
    print('Чет')



a = 475
b = 893
c = 123

if a > b:
    tmp = b
    b = a
    a = tmp

if b > c:
    tmp = c
    c = b
    b = tmp

if a > b:
    tmp = b
    b = a
    a = tmp

print(b)

a = 12
b = 4

if a % b == 0:
    print('YES')
else:
    print('NO')
