print(ord('a'))
print(chr(97))

symbol = 'b'

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
        a3[i] = chr(a3[i] + 32)
    elif a3[i] > 122 and a3[i] < 65:
            a3[i] = a3[i]
    else:
        a3[i] = chr(a3[i] - 32)


print(a3)

# заменяем мелкие на заглавные
# for i in range(len(a3)):
#     if a3[i] >= 97 and a3[i] <= 122:
#         a3.pop(i)
#         a3.insert(i, chr(a3[i] + 32))
#
# print(a3)

# a4 = ''
# for i in range(len(a3)):
#     a4 = a4 + (chr(a3[i]))
# print(a4)

data = [3, 2, 1, 2]

result = True

for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        result = False

print(result)